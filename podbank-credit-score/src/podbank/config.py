from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from datetime import date

@dataclass(frozen=True)
class Config:
    project_root: Path
    raw_dir: Path
    bronze_dir: Path
    silver_dir: Path
    abt_dir: Path
    ingest_date: str

def default_config(project_root: Path | None = None) -> Config:
    root = project_root or Path(".").resolve()
    data = root / "data"
    today = date.today().isoformat()  # YYYY-MM-DD
    return Config(
        project_root=root,
        raw_dir=data / "00-raw",
        bronze_dir=data / "01-bronze",
        silver_dir=data / "02-silver",
        abt_dir=data / "03-abt",
        ingest_date=today,
    )