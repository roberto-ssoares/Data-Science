import pandas as pd
import glob
import os

def raw_to_bronze(raw_path="data/raw/", bronze_path="data/bronze/"):
    """Converte todos os CSVs para Parquet com tipagem otimizada."""
    if not os.path.exists(bronze_path):
        os.makedirs(bronze_path)
    
    csv_files = glob.glob(os.path.join(raw_path, "*.csv"))
    
    for file in csv_files:
        filename = os.path.basename(file).replace(".csv", ".parquet")
        print(f"📦 Convertendo {os.path.basename(file)}...")
        
        # Lendo com baixo uso de memória
        df = pd.read_csv(file, low_memory=False)
        
        # Salvando em Parquet (Engine PyArrow é a mais rápida)
        df.to_parquet(os.path.join(bronze_path, filename), engine='pyarrow', index=False)
    
    print("✅ Camada Bronze populada com sucesso!")

# Execução única no início do projeto
# raw_to_bronze()
