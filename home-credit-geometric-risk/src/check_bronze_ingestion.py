import polars as pl
import os

def check_bronze_ingestion(file_name="application_train.parquet", bronze_dir="data/bronze/"):
    """Valida a integridade e o esquema do arquivo Parquet na camada Bronze."""
    path = os.path.join(bronze_dir, file_name)
    
    if not os.path.exists(path):
        print(f"❌ Erro: Arquivo {file_name} não encontrado em {bronze_dir}")
        return
    
    # Leitura ultra-rápida de metadados com Polars
    df = pl.read_parquet(path)
    
    print(f"✅ Validação de Ingestão: {file_name}")
    print("-" * 40)
    print(f"📊 Shape: {df.shape[0]:,} linhas x {df.shape[1]} colunas")
    print(f"💾 Memória estimada: {df.estimated_size('mb'):.2f} MB")
    print("-" * 40)
    print("📋 Resumo dos Tipos de Dados (Schema):")
    print(df.schema)
    print("-" * 40)
    print("👀 Amostra das primeiras 5 linhas:")
    print(df.head(5))

# Execução do teste de sanidade da Fase 1:
# check_bronze_ingestion()
