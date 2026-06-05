import os
from pathlib import Path


def load_dotenv(env_path: str | Path | None = None) -> None:
    if env_path is None:
        env_path = Path(__file__).resolve().parents[1] / ".env"
    else:
        env_path = Path(env_path)

    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
