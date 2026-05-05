from pathlib import Path
import sys

import pandas as pd
import numpy as np
import duckdb
import pyarrow


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]

    print("=" * 70)
    print("Doctor — Spotify Global Music Intelligence")
    print("=" * 70)

    print(f"Project root: {project_root}")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Pandas version: {pd.__version__}")
    print(f"NumPy version: {np.__version__}")
    print(f"DuckDB version: {duckdb.__version__}")
    print(f"PyArrow version: {pyarrow.__version__}")

    required_paths = [
        "data/00_raw",
        "data/01_bronze",
        "data/02_silver",
        "data/03_gold",
        "notebooks",
        "src/spotify_intelligence",
        "reports/figures",
        "reports/html",
        "README.md",
        "pyproject.toml",
    ]

    print("\nEstrutura do projeto:")
    for item in required_paths:
        path = project_root / item
        status = "OK" if path.exists() else "MISSING"
        print(f"[{status}] {item}")

    print("\nDiagnóstico concluído.")


if __name__ == "__main__":
    main()
