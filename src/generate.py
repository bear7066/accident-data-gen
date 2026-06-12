from pathlib import Path
import json, argparse, sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "static"))

from static.prompts import build_prompt
from utils.llm import llm_generate
output_path = Path("output/")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--action-label", required=True)
    parser.add_argument("--num-videos", type=int, default=1)
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--video-json-output-dir", type=Path, default=output_path)
    parser.add_argument("--video-output-dir", type=Path, default=output_path)
    # fixed -> parser.add_argument("--output",type=Path, default=Path("outputs/generation_records.json"))
    # automatically random -> parser.add_argument("--seed", type=int, default=None) 
    # fixed 5 seconds -> parser.add_argument("--duration", type=int, default=5) 
    args = parser.parse_args()

    for i in range(args.start_index, args.start_index + args.num_videos):
        print(f"{args.action_label}_{i}:", i)
        prompt = build_prompt(args.action_label)
        video_path = args.video_output_dir / f"{args.action_label}_{i}.mp4"
        try:
            response = llm_generate(prompt, video_path)
            error = None
        except Exception as exc:
            response = None
            error = str(exc)
            print("error:", error)

        record = {
            "index": i,
            "action_label": args.action_label,  
            "video_path": str(video_path),
            "prompt": prompt,
            "response": response,
            "error": error,
          }

        json_path = args.video_json_output_dir / f"{args.action_label}_{i}.json"
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(
            json.dumps(record, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


if __name__ == '__main__':
    main()
