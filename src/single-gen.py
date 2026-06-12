"""Generate a single video by calling the Sora model via OpenRouter.

This is a standalone script: given a prompt, it submits one video
generation job, polls until it completes, and saves the resulting video
to disk.

Example:
    uv run src/single-gen.py --prompt "A cat falls off a sofa." \\
        --video-output output/single.mp4
"""

import argparse
import os
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from utils.load_env import load_dotenv

API_BASE = "https://openrouter.ai"
VIDEOS_ENDPOINT = urljoin(API_BASE, "/api/v1/videos")
DEFAULT_MODEL = "openai/sora-2-pro"
DEFAULT_RESOLUTION = "720p"
DEFAULT_ASPECT_RATIO = "16:9"
DEFAULT_POLL_INTERVAL = 15


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line flags for a single video generation.

    Args:
        argv: Argument list to parse. Defaults to ``sys.argv[1:]`` when
            ``None``.

    Returns:
        The parsed arguments namespace.
    """
    parser = argparse.ArgumentParser(
        description="Generate a single video with the Sora model.",
    )
    parser.add_argument("--prompt", required=True, help="Prompt describing the video to generate.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Sora model identifier passed to OpenRouter.")
    parser.add_argument("--resolution", default=DEFAULT_RESOLUTION, help="Output video resolution, e.g. '720p'.")
    parser.add_argument("--aspect-ratio", default=DEFAULT_ASPECT_RATIO, help="Output video aspect ratio, e.g. '16:9'.")
    parser.add_argument("--no-audio", action="store_true", help="Disable audio generation.")
    parser.add_argument("--poll-interval", type=int, default=DEFAULT_POLL_INTERVAL, help="Seconds to wait between job status polls.")
    parser.add_argument("--video-output", type=Path, required=True, help="Path to save the generated video.")

    return parser.parse_args(argv)


def submit_video_job(
    prompt: str,
    api_key: str,
    model: str = DEFAULT_MODEL,
    resolution: str = DEFAULT_RESOLUTION,
    aspect_ratio: str = DEFAULT_ASPECT_RATIO,
    generate_audio: bool = True,
) -> dict:
    """Submit a video generation job to OpenRouter.

    Args:
        prompt: The text prompt describing the video to generate.
        api_key: OpenRouter API key.
        model: Sora model identifier, e.g. ``"openai/sora-2-pro"``.
        resolution: Output resolution, e.g. ``"720p"``.
        aspect_ratio: Output aspect ratio, e.g. ``"16:9"``.
        generate_audio: Whether to generate audio for the video.

    Returns:
        The JSON response from the videos endpoint, expected to contain
        a ``polling_url`` key.

    Raises:
        RuntimeError: If the response does not contain a ``polling_url``.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "prompt": prompt,
        "resolution": resolution,
        "aspect_ratio": aspect_ratio,
        "generate_audio": generate_audio,
    }

    response = requests.post(VIDEOS_ENDPOINT, headers=headers, json=payload, timeout=60)
    job = response.json()
    print("submit job:", job)

    if "polling_url" not in job:
        raise RuntimeError(job)

    return job


def poll_job(polling_url: str, api_key: str, poll_interval: int = DEFAULT_POLL_INTERVAL) -> dict:
    """Poll a video generation job until it finishes.

    Args:
        polling_url: Relative or absolute polling URL returned by
            :func:`submit_video_job`.
        api_key: OpenRouter API key.
        poll_interval: Seconds to sleep between polls.

    Returns:
        The final job status response, with ``status`` equal to
        ``"completed"``.

    Raises:
        RuntimeError: If the job status becomes ``"failed"``,
            ``"cancelled"``, or ``"expired"``.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    url = urljoin(API_BASE, polling_url)

    while True:
        status = requests.get(url, headers=headers, timeout=60).json()
        print("poll status:", status.get("status"))

        if status["status"] == "completed":
            return status
        if status["status"] in ("failed", "cancelled", "expired"):
            raise RuntimeError(status)

        time.sleep(poll_interval)


def download_video(job_id: str, api_key: str, output_path: Path) -> None:
    """Download a completed video and save it to disk.

    Args:
        job_id: The completed job's identifier.
        api_key: OpenRouter API key.
        output_path: File path to write the downloaded video bytes to.
            Parent directories are created if they do not exist.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    video_url = urljoin(API_BASE, f"/api/v1/videos/{job_id}/content?index=0")
    print("download video:", video_url)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    video = requests.get(video_url, headers=headers, timeout=300)
    output_path.write_bytes(video.content)
    print("saved:", output_path)


def main() -> None:
    """Parse flags and generate a single video from a prompt."""
    args = parse_args()

    load_dotenv()
    api_key = os.environ["OPENROUTER_API_KEY"]

    job = submit_video_job(
        args.prompt,
        api_key,
        model=args.model,
        resolution=args.resolution,
        aspect_ratio=args.aspect_ratio,
        generate_audio=not args.no_audio,
    )
    status = poll_job(job["polling_url"], api_key, poll_interval=args.poll_interval)
    download_video(status["id"], api_key, args.video_output)


if __name__ == "__main__":
    main()
