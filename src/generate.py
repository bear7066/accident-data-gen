from pathlib import Path
import json, argparse
from static.prompts import build_prompt
from utils import llm_generate
output_path = Path("output/records.json")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--action-label", required=True)
    parser.add_argument("--num-videos", type=int, default=1)
    # fixed -> parser.add_argument("--output",type=Path, default=Path("outputs/generation_records.json"))
    # automatically random -> parser.add_argument("--seed", type=int, default=None) 
    # fixed 5 seconds -> parser.add_argument("--duration", type=int, default=5) 
    args = parser.parse_args()
    records = []

    for i in range(args.num_videos):
        prompt = build_prompt(args.action_label)
        response = llm_generate(prompt)

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
