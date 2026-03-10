from pathlib import Path
import subprocess
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
APP_FILE = BASE_DIR / "app" / "main.py"

if __name__ == "__main__":
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", str(APP_FILE)],
        check=True,
    )

    