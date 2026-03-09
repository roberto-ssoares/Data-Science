from __future__ import annotations
from pathlib import Path
import duckdb

from podbank.config import Config

RAW_TABLES = [
    "application_train",
    "application_test",
    "bureau",
    "bureau_balance",
    "credit_card_balance",
    "installments_payments",
    "POS_CASH_balance",
    "previous_application",
]

def _csv_path(raw_dir: Path, name: str) -> Path:
    return raw_dir / f"{name}.csv"

def promote_all_raw_to_bronze(cfg: Config) -> None:
    cfg.bronze_dir.mkdir(parents=True, exist_ok=True)

    con = duckdb.connect()  # in-memory é suficiente p/ esse step
    con.execute("PRAGMA threads=4;")

    for name in RAW_TABLES:
        src = _csv_path(cfg.raw_dir, name)
        if not src.exists():
            raise FileNotFoundError(f"Não encontrei: {src}")

        out_dir = cfg.bronze_dir / name / f"ingest_date={cfg.ingest_date}"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{name}.parquet"

        # leitura robusta (DuckDB infere schema; header = true)
        # ALL_VARCHAR=0 mantém tipagem (útil no começo), mas pode falhar em colunas “sujas”.
        # Se der problema de tipo, a gente troca para ALL_VARCHAR=1 e tipa depois no Silver.
        con.execute(
            f"""
            COPY (
              SELECT
                *,
                '{cfg.ingest_date}'::DATE AS ingest_date
              FROM read_csv_auto('{src.as_posix()}', HEADER=TRUE, SAMPLE_SIZE=-1)
            )
            TO '{out_file.as_posix()}'
            (FORMAT PARQUET, COMPRESSION ZSTD);
            """
        )

        # auditoria rápida
        cnt = con.execute(
            f"SELECT COUNT(*) FROM read_parquet('{out_file.as_posix()}')"
        ).fetchone()[0]
        print(f"[BRONZE] {name}: {cnt:,} linhas -> {out_file}")

    con.close()