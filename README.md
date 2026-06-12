# Accident Data Gen

Generates synthetic CCTV-style fall/accident videos by prompting the Sora model
(`openai/sora-2-pro`) through the OpenRouter API.

## Setup

```bash
uv sync
cp .envtemplate .env   # set OPENROUTER_API_KEY
```

## Usage

- `src/generate.py` — batch-generate videos for an action label. Prompts are
  built from `static/prompts.py` and `static/action_label.py`, with scene,
  lighting, and camera variation pulled from `static/variables.py`.

  ```bash
  uv run src/generate.py --action-label fall_from_chair --num-videos 3 \
    --video-output-dir output/videos --video-json-output-dir output/records
  ```

- `src/single-gen.py` — generate a single video from an arbitrary prompt,
  without the labeling/prompt-building pipeline.

  ```bash
  uv run src/single-gen.py --prompt "A person trips and falls in a hallway." \
    --video-output output/single.mp4
  ```

- `run.sh` — runs `generate.py` in parallel across multiple action labels
  (configure labels and counts inside the script).

## Layout

- `src/` — generation scripts
- `static/` — prompt templates, action label definitions, scene/variable pools
- `utils/` — `.env` loading and the OpenRouter/Sora API helper (`utils/llm.py`)
