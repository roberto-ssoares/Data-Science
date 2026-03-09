import polars as pl
from pathlib import Path

# Configurações de caminhos
BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = BASE_DIR / "data" / "00-raw" / "Dados_PRF_2023_utf8.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "01-processed" / "acidentes.parquet"


def clean_column_names(name: str) -> str:
    """Padroniza nomes de colunas para snake_case."""
    return name.strip().lower()


def run_ingestion():
    print(f"🚀 Iniciando ingestão de: {RAW_DATA_PATH}")

    # 1. Leitura Lazy com separador ;
    try:
        lf = pl.scan_csv(
            RAW_DATA_PATH, separator=";", infer_schema_length=10000, ignore_errors=True
        )
    except Exception as e:
        print(f"❌ Erro ao ler CSV: {e}")
        return

    # 2. Renomear colunas para snake_case
    lf = lf.rename({col: clean_column_names(col) for col in lf.columns})

    # 3. Tratamento de Tipos e Limpeza
    # - Converter km para float (vírgula para ponto se necessário)
    # - Converter data_inversa para Date
    # - Preencher nulos em colunas críticas

    lf = (
        lf.with_columns(
            [
                # Tratamento de KM (substitui vírgula por ponto e converte)
                pl.col("km").str.replace(",", ".").cast(pl.Float64, strict=False),
                # Tratamento de Latitude e Longitude
                pl.col("latitude").str.replace(",", ".").cast(pl.Float64, strict=False),
                pl.col("longitude")
                .str.replace(",", ".")
                .cast(pl.Float64, strict=False),
                # Tratamento de Data
                pl.col("data_inversa").str.to_date("%Y-%m-%d", strict=False),
            ]
        ).fill_null(strategy="forward")  # Exemplo simples de preenchimento
    )

    # 4. Validação Básica (Data Quality)
    df_check = lf.select(
        [
            pl.col("id").null_count().alias("null_ids"),
            pl.col("data_inversa").null_count().alias("null_datas"),
            pl.col("km").null_count().alias("null_km"),
        ]
    ).collect()

    print("📊 Check de Qualidade (Nulos):")
    print(df_check)

    # 5. Persistência em Parquet
    print(f"💾 Salvando dados em: {PROCESSED_DATA_PATH}")
    lf.sink_parquet(PROCESSED_DATA_PATH)

    print("✅ Ingestão finalizada com sucesso!")


if __name__ == "__main__":
    # Garantir que a pasta de destino existe
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    run_ingestion()
