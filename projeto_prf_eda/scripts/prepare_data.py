#prepare_data.py

from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]

if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

from src.pipeline.ingestion import main as run_ingestion


if __name__ == "__main__":
    run_ingestion()
    