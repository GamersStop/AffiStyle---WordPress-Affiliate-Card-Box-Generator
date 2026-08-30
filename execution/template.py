"""
Execution Script Template

Deterministic Python script template following the AGENTS.md 3-layer architecture:
- Reads environment variables from .env
- Processes inputs reliably
- Outputs temporary data into .tmp/
- Raises clear errors with stack traces for self-annealing
"""

import os
import sys
from pathlib import Path

# Paths
ROOT_DIR = Path(__file__).resolve().parent.parent
TMP_DIR = ROOT_DIR / ".tmp"
ENV_FILE = ROOT_DIR / ".env"

def load_env(env_path: Path):
    """Simple .env loader if python-dotenv is not installed."""
    if not env_path.exists():
        return
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip())

def main():
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    load_env(ENV_FILE)
    
    print("[EXECUTION] Execution environment initialized.")
    # Implement deterministic task logic here

if __name__ == "__main__":
    main()
