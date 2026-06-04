from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests


BASE_URL = "https://openrouter.ai/api/v1/"
DEFAULT_MODEL = "openai/sora-2-pro"
DEFAULT_OUTPUT = Path("outputs/sora2_fall_from_chair_5s.mp4")
DEFAULT_PROMPT = (
   "wide-angle security camera view, slightly fisheye distortion. Scene: a modest living room with a sofa and coffee table, dim evening lighting with a single lamp on. Subject: an elderly man in his 70s wearing casual clothes. Action: person sitting on a chair loses balance and falls to the floor. Duration: 8 seconds. Style: typical CCTV video with realistic noise. No music, no text overlay, no dramatic camera movement. The camera is completely static throughout."
)


class OpenRouterVideoError(RuntimeError):
    """Raised when OpenRouter video generation cannot complete."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a fainting-fall video through OpenRouter Sora 2 Pro."
    )
    parser.add_argument("--model", default=DEFAULT_MODEL, help="OpenRouter video model slug")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT, help="Text prompt for the video")
    parser.add_argument("--duration", type=int, default=4, help="Final video duration in seconds")
    parser.add_argument("--resolution", default="720p", help="Requested OpenRouter resolution")
    parser.add_argument("--aspect-ratio", default="16:9", help="Requested aspect ratio")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Final MP4 path")
    parser.add_argument(
        "--poll-interval",
        type=int,
        default=15,
        help="Seconds between status checks",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=900,
        help="Maximum seconds to wait for generation",
    )
    parser.add_argument(
        "--no-audio",
        action="store_true",
        help="Request video without generated audio",
    )
    parser.add_argument(
        "--keep-raw",
        action="store_true",
        help="Keep the untrimmed downloaded video when trimming is needed",
    )
    return parser


def make_session(api_key: str) -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://openrouter.ai/",
            "X-Title": "Sora2 Fainting Fall Generator",
        }
    )
    return session


def request_json(
    session: requests.Session,
    method: str,
    url: str,
    **kwargs: Any,
) -> dict[str, Any]:
    response = session.request(method, url, timeout=60, **kwargs)
    try:
        data = response.json()
    except ValueError as exc:
        raise OpenRouterVideoError(
            f"{method} {url} returned non-JSON response: HTTP {response.status_code}"
        ) from exc

    if response.status_code >= 400:
        detail = data.get("error", data)
        raise OpenRouterVideoError(f"{method} {url} failed: HTTP {response.status_code}: {detail}")

    return data


def get_model_info(session: requests.Session, model: str) -> dict[str, Any] | None:
    data = request_json(session, "GET", urljoin(BASE_URL, "videos/models"))
    models = data.get("data", [])
    for item in models:
        if item.get("id") == model or item.get("canonical_slug") == model:
            return item
    return None


def choose_generation_duration(model_info: dict[str, Any] | None, final_duration: int) -> int:
    if not model_info:
        return final_duration

    supported = sorted(
        int(value)
        for value in model_info.get("supported_durations") or []
        if isinstance(value, int)
    )
    if not supported or final_duration in supported:
        return final_duration

    longer_or_equal = [value for value in supported if value >= final_duration]
    if longer_or_equal:
        chosen = longer_or_equal[0]
    else:
        chosen = supported[-1]

    print(
        f"Requested {final_duration}s, but {model_info.get('id')} supports "
        f"{supported}; generating {chosen}s first.",
        file=sys.stderr,
    )
    return chosen


def submit_video_job(
    session: requests.Session,
    *,
    model: str,
    prompt: str,
    duration: int,
    resolution: str,
    aspect_ratio: str,
    generate_audio: bool,
) -> dict[str, Any]:
    payload = {
        "model": model,
        "prompt": prompt,
        "duration": duration,
        "resolution": resolution,
        "aspect_ratio": aspect_ratio,
        "generate_audio": generate_audio,
    }
    return request_json(session, "POST", urljoin(BASE_URL, "videos"), json=payload)


def poll_until_done(
    session: requests.Session,
    polling_url: str,
    *,
    poll_interval: int,
    timeout: int,
) -> dict[str, Any]:
    deadline = time.monotonic() + timeout
    polling_url = urljoin(BASE_URL, polling_url)

    while True:
        status = request_json(session, "GET", polling_url)
        state = status.get("status")
        print(f"Job status: {state}", file=sys.stderr)

        if state == "completed":
            return status
        if state in {"failed", "cancelled", "expired"}:
            raise OpenRouterVideoError(
                f"Video job ended with status {state}: {status.get('error', status)}"
            )
        if time.monotonic() >= deadline:
            raise OpenRouterVideoError(f"Timed out after {timeout}s waiting for video generation")

        time.sleep(poll_interval)


def download_video(session: requests.Session, status: dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    content_urls = status.get("unsigned_urls") or []
    if content_urls:
        content_url = urljoin(BASE_URL, content_urls[0])
    else:
        job_id = status["id"]
        content_url = urljoin(BASE_URL, f"videos/{job_id}/content?index=0")

    with session.get(content_url, stream=True, timeout=300) as response:
        response.raise_for_status()
        with output_path.open("wb") as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)


def trim_video(input_path: Path, output_path: Path, duration: int) -> bool:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        return False

    output_path.parent.mkdir(parents=True, exist_ok=True)
    command = [
        ffmpeg,
        "-y",
        "-i",
        str(input_path),
        "-t",
        str(duration),
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "18",
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-movflags",
        "+faststart",
        str(output_path),
    ]
    subprocess.run(command, check=True)
    return True


def save_metadata(output_path: Path, metadata: dict[str, Any]) -> None:
    metadata_path = output_path.with_suffix(output_path.suffix + ".json")
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    args = build_parser().parse_args()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Missing OPENROUTER_API_KEY environment variable.", file=sys.stderr)
        return 2

    session = make_session(api_key)
    model_info = get_model_info(session, args.model)
    generation_duration = choose_generation_duration(model_info, args.duration)

    job = submit_video_job(
        session,
        model=args.model,
        prompt=args.prompt,
        duration=generation_duration,
        resolution=args.resolution,
        aspect_ratio=args.aspect_ratio,
        generate_audio=not args.no_audio,
    )
    print(f"Submitted job: {job.get('id')}", file=sys.stderr)

    status = poll_until_done(
        session,
        job["polling_url"],
        poll_interval=args.poll_interval,
        timeout=args.timeout,
    )

    raw_path = args.output
    needs_trim = generation_duration != args.duration
    if needs_trim:
        raw_path = args.output.with_name(
            f"{args.output.stem}_{generation_duration}s_raw{args.output.suffix}"
        )

    download_video(session, status, raw_path)

    final_path = raw_path
    if needs_trim:
        if trim_video(raw_path, args.output, args.duration):
            final_path = args.output
            if not args.keep_raw:
                raw_path.unlink(missing_ok=True)
        else:
            print(
                f"ffmpeg is not available; kept untrimmed {generation_duration}s video at {raw_path}",
                file=sys.stderr,
            )

    save_metadata(
        final_path,
        {
            "model": args.model,
            "prompt": args.prompt,
            "requested_duration": args.duration,
            "generation_duration": generation_duration,
            "resolution": args.resolution,
            "aspect_ratio": args.aspect_ratio,
            "job": status,
        },
    )
    print(f"Saved video: {final_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
