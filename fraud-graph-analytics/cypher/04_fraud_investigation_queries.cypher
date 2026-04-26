// 1. Top transações críticas
MATCH (t:Transacao)
WHERE t.risk_band = 'critico'
RETURN
    t.transacao_id AS transacao_id,
    t.valor AS valor,
    t.rule_score AS rule_score,
    t.fraud_scenario AS fraud_scenario,
    t.qtd_regras_acionadas AS qtd_regras_acionadas
ORDER BY t.rule_score DESC, t.valor DESC
LIMIT 25;

// 2. Beneficiários concentradores por quantidade de contas de origem
MATCH (a:Conta)-[r:ENVIOU_PARA_BENEFICIARIO]->(b:Beneficiario)
RETURN
    b.beneficiario_id AS beneficiario_id,
    count(DISTINCT a) AS contas_origem,
    sum(r.qtd_transacoes) AS qtd_transacoes,
    sum(r.valor_total) AS valor_total,
    avg(r.score_medio) AS score_medio
ORDER BY contas_origem DESC, valor_total DESC
LIMIT 25;

// 3. Dispositivos compartilhados por múltiplas contas
MATCH (a:Conta)-[r:USOU_DISPOSITIVO]->(d:Dispositivo)
RETURN
    d.device_id AS device_id,
    d.fingerprint_risco AS fingerprint_risco,
    count(DISTINCT a) AS contas_distintas,
    sum(r.qtd_transacoes) AS qtd_transacoes,
    sum(r.qtd_alertas) AS qtd_alertas,
    avg(r.score_medio) AS score_medio
ORDER BY contas_distintas DESC, qtd_alertas DESC
LIMIT 25;

// 4. IPs usados por múltiplas contas
MATCH (a:Conta)-[r:USOU_IP]->(ip:IP)
RETURN
    ip.ip_id AS ip_id,
    ip.risco_rede AS risco_rede,
    ip.tipo_rede AS tipo_rede,
    count(DISTINCT a) AS contas_distintas,
    sum(r.qtd_transacoes) AS qtd_transacoes,
    sum(r.qtd_alertas) AS qtd_alertas,
    avg(r.score_medio) AS score_medio
ORDER BY contas_distintas DESC, qtd_alertas DESC
LIMIT 25;

// 5. Regras mais acionadas
MATCH (t:Transacao)-[r:ACIONOU]->(reg:Regra)
RETURN
    reg.rule_id AS rule_id,
    reg.rule_name AS rule_name,
    reg.severidade AS severidade,
    count(DISTINCT t) AS qtd_transacoes,
    avg(t.rule_score) AS score_medio,
    count(DISTINCT t.fraud_scenario) AS qtd_cenarios
ORDER BY qtd_transacoes DESC
LIMIT 25;

// 6. Caminho investigativo de uma transação crítica
MATCH path = (a:Conta)-[:REALIZOU]->(t:Transacao)-[:ENVIOU_PARA|USOU|ORIGINOU_DE|ACIONOU]->(n)
WHERE t.risk_band = 'critico'
RETURN path
LIMIT 25;

// 7. Contas com múltiplas conexões suspeitas
MATCH (a:Conta)
OPTIONAL MATCH (a)-[rd:USOU_DISPOSITIVO]->(d:Dispositivo)
OPTIONAL MATCH (a)-[rb:ENVIOU_PARA_BENEFICIARIO]->(b:Beneficiario)
OPTIONAL MATCH (a)-[ri:USOU_IP]->(ip:IP)
RETURN
    a.conta_id AS conta_id,
    count(DISTINCT d) AS dispositivos,
    count(DISTINCT b) AS beneficiarios,
    count(DISTINCT ip) AS ips,
    sum(coalesce(rd.qtd_alertas, 0)) + sum(coalesce(rb.qtd_alertas, 0)) + sum(coalesce(ri.qtd_alertas, 0)) AS sinais_alerta
ORDER BY sinais_alerta DESC
LIMIT 25;