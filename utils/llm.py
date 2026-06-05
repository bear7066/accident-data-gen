import os, sys, time, requests
from pathlib import Path
from urllib.parse import urljoin


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "static"))

from static.prompts import build_prompt
from utils.load_env import load_dotenv


def llm_generate(prompt: str, output_path: Path) -> dict:
    load_dotenv()
    api_key = os.environ["OPENROUTER_API_KEY"]
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "openai/sora-2-pro",
        "prompt": prompt,
        # "duration": 4,
        "resolution": "720p",
        "aspect_ratio": "16:9",
        "generate_audio": True,
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/videos",
        headers=headers,
        json=payload,
        timeout=60,
    )
    job = response.json()
    print("submit job:", job)

    if "polling_url" not in job:
        raise RuntimeError(job)
        
    polling_url = urljoin("https://openrouter.ai", job["polling_url"])
    while True:
        status = requests.get(polling_url, headers=headers, timeout=60).json()
        print("poll status:", status.get("status"))
        
        if status["status"] == "completed":
            break
        if status["status"] in ["failed", "cancelled", "expired"]:
            raise RuntimeError(status)

        time.sleep(15)
    
    video_url = urljoin("https://openrouter.ai/api/v1/", f"videos/{status['id']}/content?index=0")
    print("download video:", video_url)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    video = requests.get(video_url, headers=headers, timeout=300)
    output_path.write_bytes(video.content)
    print("saved:", output_path)

    return {
        "job_id": status["id"],
        "status": status["status"],
        "output_path": str(output_path),
    }


if __name__ == '__main__':
    action_label = "fall_from_chair"
    print("action_label:", action_label)
    prompt = build_prompt(action_label)
    print(llm_generate(prompt, Path("outputs/test.mp4")))
