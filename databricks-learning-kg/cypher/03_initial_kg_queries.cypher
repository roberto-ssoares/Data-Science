// Cypher Reference — Databricks Learning KG

// 1. Visualizar certificação, domínios e tópicos
MATCH path = (c:Certification)-[:HAS_DOMAIN]->(d:ExamDomain)-[:COVERS]->(t:Topic)
RETURN path
LIMIT 100;

// 2. Tópicos por domínio
MATCH (d:ExamDomain)-[:COVERS]->(t:Topic)
RETURN d.name AS domain, count(t) AS total_topics
ORDER BY total_topics DESC;

// 3. Tópicos sem notebook prático
MATCH (t:Topic)
WHERE NOT EXISTS {
    MATCH (:Notebook)-[:PRACTICES]->(t)
}
RETURN t.node_id AS topic_id, t.name AS topic, t.category AS category, t.priority AS priority
ORDER BY t.priority DESC, t.category, t.name;

// 4. Pré-requisitos mais estruturantes
MATCH (t:Topic)-[:PREREQUISITE_FOR]->(next:Topic)
RETURN t.name AS topic, count(next) AS unlocks_topics
ORDER BY unlocks_topics DESC;

// 5. Notebooks conectados a skills
MATCH path = (:Notebook)-[:PRACTICES]->(:Topic)<-[:SUPPORTED_BY]-(:Skill)
RETURN path
LIMIT 100;

// 6. Snapshot inicial de progresso
MATCH path = (:Snapshot)-[:CAPTURES_STATUS_OF]->(:Topic)
RETURN path
LIMIT 100;
