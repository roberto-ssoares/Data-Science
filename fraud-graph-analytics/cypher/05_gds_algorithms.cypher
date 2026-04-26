// Projeção sugerida para o próximo notebook.
//
// Observação:
// O Notebook 05 será dedicado a Graph Data Science.
// As queries abaixo são um ponto de partida para projeções futuras.

// Exemplo conceitual de projeção Conta-Dispositivo-Beneficiário-IP
// Ajustar conforme versão instalada do Neo4j GDS.

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

// Degree centrality
CALL gds.degree.stream('fraud_graph_bipartite')
YIELD nodeId, score
RETURN
    gds.util.asNode(nodeId).conta_id AS conta_id,
    gds.util.asNode(nodeId).device_id AS device_id,
    gds.util.asNode(nodeId).beneficiario_id AS beneficiario_id,
    gds.util.asNode(nodeId).ip_id AS ip_id,
    labels(gds.util.asNode(nodeId)) AS labels,
    score
ORDER BY score DESC
LIMIT 50;

// Louvain community detection
CALL gds.louvain.stream('fraud_graph_bipartite')
YIELD nodeId, communityId
RETURN
    labels(gds.util.asNode(nodeId)) AS labels,
    gds.util.asNode(nodeId).conta_id AS conta_id,
    gds.util.asNode(nodeId).device_id AS device_id,
    gds.util.asNode(nodeId).beneficiario_id AS beneficiario_id,
    gds.util.asNode(nodeId).ip_id AS ip_id,
    communityId
ORDER BY communityId
LIMIT 100;