from pathlib import Path
import json, argparse, sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "static"))

from static.prompts import build_prompt
from utils.llm import llm_generate
output_path = Path("output/records.json")
output_video_path = Path("output/")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--action-label", required=True)
    parser.add_argument("--num-videos", type=int, default=1)
    parser.add_argument("--output", type=Path, default=output_path)
    # fixed -> parser.add_argument("--output",type=Path, default=Path("outputs/generation_records.json"))
    # automatically random -> parser.add_argument("--seed", type=int, default=None) 
    # fixed 5 seconds -> parser.add_argument("--duration", type=int, default=5) 
    args = parser.parse_args()
    records = []

    for i in range(args.num_videos):
        print("action_label:", args.action_label)
        prompt = build_prompt(args.action_label)
        video_path = output_video_path / f"{args.action_label}_{i}.mp4"
        response = llm_generate(prompt, video_path)

        record = {
            "index": i,
            "action_label": args.action_label,  
            "prompt": prompt,
            "response": response,
          }

        records.append(record)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(records, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == '__main__':
    main()
