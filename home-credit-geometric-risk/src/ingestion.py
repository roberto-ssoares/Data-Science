import duckdb
import os
import glob
import time

def raw_to_bronze_duckdb(raw_dir="data/raw/", bronze_dir="data/bronze/"):
    """
    Converte CSVs para Parquet usando o motor SQL do DuckDB.
    Performance: Até 10x mais rápido que Pandas.
    """
    # 1. Setup de diretórios
    if not os.path.exists(bronze_dir):
        os.makedirs(bronze_dir)
        
    con = duckdb.connect()
    csv_files = glob.glob(os.path.join(raw_dir, "*.csv"))
    
    print(f"🚀 Iniciando ingestão de {len(csv_files)} arquivos...")
    start_all = time.time()

    for file_path in csv_files:
        start_file = time.time()
        file_name = os.path.basename(file_path)
        parquet_name = file_name.replace(".csv", ".parquet")
        target_path = os.path.join(bronze_dir, parquet_name)
        
        print(f"📦 Processando: {file_name}...", end=" ", flush=True)
        
        # O comando 'COPY' do DuckDB é mágico: ele autodetecta tipos e escreve direto
        # O parâmetro (FORMAT PARQUET) garante a compressão eficiente
        #query = f"COPY (SELECT * FROM read_csv_auto('{file_path}')) TO '{target_path}' (FORMAT PARQUET);"
        # Esta linha instrui o DuckDB a ler o CSV auto-detectando delimitadores e o encoding (ex: Latin-1 ou UTF-8)
		query = f"COPY (SELECT * FROM read_csv_auto('{file_path}', ALL_VARCHAR=FALSE)) TO '{target_path}' (FORMAT PARQUET);"
        con.execute(query)
        
        elapsed = time.time() - start_file
        print(f"Concluído em {elapsed:.2f}s")

    print(f"\n✅ Camada Bronze finalizada em {time.time() - start_all:.2f}s!")
    con.close()

# Execução:
# raw_to_bronze_duckdb()






