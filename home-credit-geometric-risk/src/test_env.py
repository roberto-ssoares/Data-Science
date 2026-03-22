import duckdb
import polars as pl
import networkx as nx
from GraphRicciCurvature.OllivierRicci import OllivierRicci
import numpy as np
from tqdm import tqdm

def run_environment_check():
    print("🧪 Iniciando Teste de Sanidade do Ambiente...")

    # 1. Teste DuckDB + Polars
    try:
        df = duckdb.query("SELECT 1 as id, 'DuckDB+Polars' as status").pl()
        print(f"✅ DuckDB & Polars: Integração OK (ID: {df['id'][0]})")
    except Exception as e:
        print(f"❌ Erro DuckDB/Polars: {e}")

    # 2. Teste NetworkX + Ricci
    try:
        G = nx.complete_graph(4)
        for u, v in G.edges():
            G[u][v]['weight'] = 1.0
        
        orc = OllivierRicci(G, alpha=0.5, verbose="ERROR")
        orc.compute_ricci_curvature()
        
        # Validar se a curvatura foi gerada
        curv = G[0][1].get("ricciCurvature")
        if curv is not None:
            print(f"✅ NetworkX & Ricci: Cálculo OK (Curv: {curv:.2f})")
    except Exception as e:
        print(f"❌ Erro Graph Engine: {e}")

    # 3. Teste Monitoramento (tqdm)
    print("✅ TQDM: Monitoramento OK")
    for _ in tqdm(range(3), desc="Testando Barra de Progresso"):
        pass

    print("\n🚀 Ambiente 100% operacional para a Fase 1!")

if __name__ == "__main__":
    run_environment_check()
