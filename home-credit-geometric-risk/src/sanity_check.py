import networkx as nx
import numpy as np

def run_graph_sanity_check(G, threshold_isolation=0.05):
    """
    Realiza verificações críticas no grafo antes do cálculo de Ricci.
    
    Args:
        G (nx.Graph): O grafo construído via K-NN.
        threshold_isolation (float): % máxima aceitável de nós isolados.
    
    Returns:
        bool: True se o grafo passar nos testes, False caso contrário.
    """
    print("🔍 Iniciando Sanity Check do Grafo...")
    
    # 1. Verificação de Conectividade
    n_nodes = G.number_of_nodes()
    n_edges = G.number_of_edges()
    isolates = list(nx.isolates(G))
    perc_isolated = len(isolates) / n_nodes
    
    print(f" - Nós: {n_nodes} | Arestas: {n_edges}")
    print(f" - Densidade: {nx.density(G):.5f}")
    print(f" - Nós isolados: {len(isolates)} ({perc_isolated:.2%})")
    
    if perc_isolated > threshold_isolation:
        print("❌ ERRO: Muitos nós isolados. Aumente o 'n_neighbors' no K-NN.")
        return False

    # 2. Verificação de Componentes
    n_components = nx.number_connected_components(G)
    largest_cc = len(max(nx.connected_components(G), key=len))
    print(f" - Componentes Conectados: {n_components}")
    print(f" - Tamanho do Maior Componente: {largest_cc} ({largest_cc/n_nodes:.2%})")
    
    if n_components > (n_nodes * 0.1): # Regra de bolso: mais de 10% de fragmentação é ruim
        print("⚠️ AVISO: Grafo muito fragmentado. Curvaturas podem ser enviesadas.")

    # 3. Verificação de Pesos e Atributos
    sample_edge = list(G.edges(data=True))[0]
    print(f" - Amostra de Aresta: {sample_edge}")
    
    if n_edges < n_nodes:
        print("❌ ERRO: O grafo tem poucas arestas para um cálculo robusto de Ricci.")
        return False

    print("✅ Grafo aprovado para processamento geométrico!")
    return True

# Exemplo de uso no pipeline:
# if run_graph_sanity_check(G):
#     orc.compute_ricci_curvature()
