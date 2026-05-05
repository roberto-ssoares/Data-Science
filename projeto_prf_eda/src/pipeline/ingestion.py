from pathlib import Path
from datetime import datetime
import polars as pl


BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DIR = BASE_DIR / "data" / "00-raw"
PROCESSED_DIR = BASE_DIR / "data" / "01-processed"

OUTPUT_PATH = PROCESSED_DIR / "acidentes.parquet"
CONTROL_PATH = PROCESSED_DIR / "ingestion_control.parquet"

ENCODINGS_TO_TRY = ["utf8", "cp1252", "latin1"]


def clean_column_names(name: str) -> str:
    """Padroniza nomes de colunas."""
    return name.strip().lower()


def list_raw_files() -> list[Path]:
    """Lista todos os arquivos CSV da camada raw."""
    files = sorted(RAW_DIR.glob("*.csv"))

    if not files:
        raise FileNotFoundError("Nenhum arquivo CSV encontrado em data/00-raw")

    return files


def build_file_inventory(files: list[Path]) -> pl.DataFrame:
    """Cria inventário técnico dos arquivos raw."""
    rows = []

    for file in files:
        stat = file.stat()
        rows.append(
            {
                "file_name": file.name,
                "file_path": str(file.resolve()),
                "modified_time": float(stat.st_mtime),
                "file_size": int(stat.st_size),
            }
        )

    return pl.DataFrame(rows)


def load_control_table() -> pl.DataFrame:
    """Carrega tabela de controle da ingestão, se existir."""
    if CONTROL_PATH.exists():
        return pl.read_parquet(CONTROL_PATH)

    return pl.DataFrame(
        schema={
            "file_name": pl.Utf8,
            "file_path": pl.Utf8,
            "modified_time": pl.Float64,
            "file_size": pl.Int64,
            "processed_at": pl.Utf8,
            "status": pl.Utf8,
        }
    )


def get_files_to_process(
    inventory_df: pl.DataFrame,
    control_df: pl.DataFrame,
) -> pl.DataFrame:
    """Identifica arquivos novos ou alterados."""
    if control_df.height == 0:
        return inventory_df

    joined = inventory_df.join(
        control_df.select(["file_name", "modified_time", "file_size"]),
        on="file_name",
        how="left",
        suffix="_ctrl",
    )

    to_process = joined.filter(
        (pl.col("modified_time_ctrl").is_null())
        | (pl.col("modified_time") != pl.col("modified_time_ctrl"))
        | (pl.col("file_size") != pl.col("file_size_ctrl"))
    )

    return to_process.select(["file_name", "file_path", "modified_time", "file_size"])


def read_csv_with_fallback(file_path: str) -> pl.DataFrame:
    """
    Lê um CSV tentando múltiplos encodings.
    Retorna DataFrame Polars.
    """
    last_error = None

    for encoding in ENCODINGS_TO_TRY:
        try:
            print(f"📄 Tentando ler {Path(file_path).name} com encoding={encoding}")

            df = pl.read_csv(
                file_path,
                separator=";",
                encoding=encoding,
                infer_schema_length=10000,
                ignore_errors=True,
            )

            print(f"✅ Arquivo {Path(file_path).name} lido com encoding={encoding}")
            return df

        except Exception as e:
            last_error = e
            print(f"⚠️ Falha ao ler {Path(file_path).name} com encoding={encoding}: {e}")

    raise ValueError(
        f"Não foi possível ler o arquivo {file_path} com os encodings testados. "
        f"Último erro: {last_error}"
    )


def normalize_dataframe(df: pl.DataFrame) -> pl.DataFrame:
    """Padroniza nomes e tipos das colunas."""
    df = df.rename({col: clean_column_names(col) for col in df.columns})

    cols = set(df.columns)

    exprs = []

    if "km" in cols:
        exprs.append(
            pl.col("km")
            .cast(pl.Utf8)
            .str.replace(",", ".")
            .cast(pl.Float64, strict=False)
        )

    if "latitude" in cols:
        exprs.append(
            pl.col("latitude")
            .cast(pl.Utf8)
            .str.replace(",", ".")
            .cast(pl.Float64, strict=False)
        )

    if "longitude" in cols:
        exprs.append(
            pl.col("longitude")
            .cast(pl.Utf8)
            .str.replace(",", ".")
            .cast(pl.Float64, strict=False)
        )

    if "data_inversa" in cols:
        exprs.append(
            pl.col("data_inversa")
            .cast(pl.Utf8)
            .str.to_date("%Y-%m-%d", strict=False)
        )

    if "uf" in cols:
        exprs.append(
            pl.col("uf")
            .cast(pl.Utf8)
            .str.to_uppercase()
        )

    if exprs:
        df = df.with_columns(exprs)

    if "data_inversa" in df.columns:
        df = df.with_columns(
            pl.col("data_inversa").dt.year().alias("ano")
        )

    return df


def transform_files(file_paths: list[str]) -> pl.DataFrame:
    """Lê, trata e consolida os arquivos raw."""
    dfs = []

    for file_path in file_paths:
        df = read_csv_with_fallback(file_path)
        df = normalize_dataframe(df)
        dfs.append(df)

    if not dfs:
        raise ValueError("Nenhum dataframe foi carregado na transformação.")

    df_final = pl.concat(dfs, how="diagonal_relaxed")

    expected_cols = {"id", "data_inversa", "km"}
    available_cols = set(df_final.columns)
    common_cols = list(expected_cols.intersection(available_cols))

    if common_cols:
        quality_df = df_final.select(
            [pl.col(col).null_count().alias(f"null_{col}") for col in common_cols]
        )

        print("📊 Check de Qualidade (Nulos):")
        print(quality_df)

    return df_final


def save_control_table(inventory_df: pl.DataFrame) -> None:
    """Atualiza tabela de controle da ingestão."""
    processed_at = datetime.now().isoformat()

    control_df = inventory_df.with_columns(
        [
            pl.lit(processed_at).alias("processed_at"),
            pl.lit("processed").alias("status"),
        ]
    )

    control_df.write_parquet(CONTROL_PATH)


def needs_rebuild() -> bool:
    """Indica se o dataset precisa ser reconstruído."""
    raw_files = list_raw_files()
    inventory_df = build_file_inventory(raw_files)
    control_df = load_control_table()

    if not OUTPUT_PATH.exists():
        return True

    files_to_process_df = get_files_to_process(inventory_df, control_df)
    return files_to_process_df.height > 0


def run_ingestion(force_rebuild: bool = False) -> None:
    """
    Executa a ingestão consolidada.

    Estratégia:
    - detecta arquivos novos ou alterados
    - se houver mudança, reconstrói o consolidado inteiro
    - atualiza tabela de controle
    """
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    raw_files = list_raw_files()
    inventory_df = build_file_inventory(raw_files)
    control_df = load_control_table()

    files_to_process_df = get_files_to_process(inventory_df, control_df)

    if not force_rebuild and files_to_process_df.height == 0 and OUTPUT_PATH.exists():
        print("✅ Nenhum arquivo novo ou alterado. Dataset já está atualizado.")
        return

    if force_rebuild:
        print("♻️ Reconstrução forçada do dataset consolidado.")
    else:
        print("📦 Arquivos novos/alterados detectados:")
        print(files_to_process_df)

    all_file_paths = [str(file.resolve()) for file in raw_files]

    print("🚀 Iniciando transformação dos arquivos raw...")
    df_final = transform_files(all_file_paths)

    print(f"💾 Salvando dataset consolidado em: {OUTPUT_PATH}")
    df_final.write_parquet(OUTPUT_PATH)

    print(f"📝 Atualizando tabela de controle em: {CONTROL_PATH}")
    save_control_table(inventory_df)

    print("✅ Ingestão finalizada com sucesso!")


if __name__ == "__main__":
    run_ingestion(force_rebuild=True)

    