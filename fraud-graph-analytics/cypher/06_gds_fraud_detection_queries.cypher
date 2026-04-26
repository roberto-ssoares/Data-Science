// Graph Data Science — Consultas complementares para Fraud Graph Analytics
// Este script complementa o Notebook 05.
// A execução depende da instalação do Neo4j Graph Data Science.

// 1. Verificar grafos existentes
CALL gds.graph.list()
YIELD graphName, nodeCount, relationshipCount
RETURN graphName, nodeCount, relationshipCount;

// 2. Remover projeção anterior, caso exista
CALL gds.graph.drop('fraud_graph_bipartite', false)
YIELD graphName;

// 3. Projetar grafo Conta-Dispositivo-Beneficiario-IP
CALL gds.graph.project(
    'fraud_graph_bipartite',
    ['Conta', 'Dispositivo', 'Beneficiario', 'IP'],
    {
        USOU_DISPOSITIVO: {
            type: 'USOU_DISPOSITIVO',
            orientation: 'UNDIRECTED',
            properties: ['qtd_alertas', 'score_medio', 'valor_total']
        },
        ENVIOU_PARA_BENEFICIARIO: {
            type: 'ENVIOU_PARA_BENEFICIARIO',
            orientation: 'UNDIRECTED',
            properties: ['qtd_alertas', 'score_medio', 'valor_total']
        },
        USOU_IP: {
            type: 'USOU_IP',
            orientation: 'UNDIRECTED',
            properties: ['qtd_alertas', 'score_medio', 'valor_total']
        }
    }
);

// 4. Degree Centrality
CALL gds.degree.stream('fraud_graph_bipartite')
YIELD nodeId, score
RETURN
    labels(gds.util.asNode(nodeId)) AS labels,
    coalesce(
        gds.util.asNode(nodeId).conta_id,
        gds.util.asNode(nodeId).device_id,
        gds.util.asNode(nodeId).beneficiario_id,
        gds.util.asNode(nodeId).ip_id
    ) AS entity_id,
    score AS degree_score
ORDER BY degree_score DESC
LIMIT 50;

// 5. PageRank
CALL gds.pageRank.stream('fraud_graph_bipartite')
YIELD nodeId, score
RETURN
    labels(gds.util.asNode(nodeId)) AS labels,
    coalesce(
        gds.util.asNode(nodeId).conta_id,
        gds.util.asNode(nodeId).device_id,
        gds.util.asNode(nodeId).beneficiario_id,
        gds.util.asNode(nodeId).ip_id
    ) AS entity_id,
    score AS pagerank_score
ORDER BY pagerank_score DESC
LIMIT 50;

// 6. Weakly Connected Components
CALL gds.wcc.stream('fraud_graph_bipartite')
YIELD nodeId, componentId
RETURN
    componentId,
    count(*) AS component_size
ORDER BY component_size DESC
LIMIT 25;

// 7. Louvain Community Detection
CALL gds.louvain.stream('fraud_graph_bipartite')
YIELD nodeId, communityId
RETURN
    communityId,
    count(*) AS community_size
ORDER BY community_size DESC
LIMIT 25;

// 8. Amostra de entidades por comunidade
CALL gds.louvain.stream('fraud_graph_bipartite')
YIELD nodeId, communityId
WITH communityId, gds.util.asNode(nodeId) AS n
RETURN
    communityId,
    labels(n) AS labels,
    coalesce(n.conta_id, n.device_id, n.beneficiario_id, n.ip_id) AS entity_id
ORDER BY communityId
LIMIT 100;