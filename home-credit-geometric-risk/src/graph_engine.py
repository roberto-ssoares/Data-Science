from tqdm import tqdm
import networkx as nx

def compute_ricci_batch_with_progress(G, orc_instance):
    """Calcula a curvatura exibindo uma barra de progresso para as arestas."""
    # O OllivierRicci processa as arestas. Vamos monitorar o progresso:
    edges = list(G.edges())
    
    print(f"🚀 Processando Geometria em {len(edges)} arestas...")
    
    # Usamos o tqdm para envolver o processo (ajuste conforme a chamada da lib)
    for _ in tqdm(range(1), desc="Calculando Ricci Curvature"):
        orc_instance.compute_ricci_curvature()
        
    print("✅ Cálculo concluído com sucesso!")
