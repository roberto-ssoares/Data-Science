// Cliente possui Conta
LOAD CSV WITH HEADERS FROM 'file:///rel_cliente_conta.csv' AS row
MATCH (c:Cliente {cliente_id: row.cliente_id})
MATCH (a:Conta {conta_id: row.conta_id})
MERGE (c)-[:POSSUI]->(a);

// Conta realizou Transação
LOAD CSV WITH HEADERS FROM 'file:///rel_conta_transacao.csv' AS row
MATCH (a:Conta {conta_id: row.conta_origem_id})
MATCH (t:Transacao {transacao_id: row.transacao_id})
MERGE (a)-[r:REALIZOU]->(t)
SET
    r.valor = toFloat(row.valor),
    r.data_hora = datetime(row.data_hora),
    r.tipo_transacao = row.tipo_transacao,
    r.canal = row.canal,
    r.rule_score = toFloat(row.rule_score),
    r.risk_band = row.risk_band,
    r.alerta_gerado = toBoolean(row.alerta_gerado);

// Transação enviada para Beneficiário
LOAD CSV WITH HEADERS FROM 'file:///rel_transacao_beneficiario.csv' AS row
MATCH (t:Transacao {transacao_id: row.transacao_id})
MATCH (b:Beneficiario {beneficiario_id: row.beneficiario_id})
MERGE (t)-[r:ENVIOU_PARA]->(b)
SET
    r.valor = toFloat(row.valor),
    r.data_hora = datetime(row.data_hora),
    r.tipo_transacao = row.tipo_transacao,
    r.rule_score = toFloat(row.rule_score),
    r.risk_band = row.risk_band;

// Transação usou Dispositivo
LOAD CSV WITH HEADERS FROM 'file:///rel_transacao_device.csv' AS row
MATCH (t:Transacao {transacao_id: row.transacao_id})
MATCH (d:Dispositivo {device_id: row.device_id})
MERGE (t)-[r:USOU]->(d)
SET
    r.data_hora = datetime(row.data_hora),
    r.tipo_transacao = row.tipo_transacao,
    r.rule_score = toFloat(row.rule_score),
    r.risk_band = row.risk_band;

// Transação originou de IP
LOAD CSV WITH HEADERS FROM 'file:///rel_transacao_ip.csv' AS row
MATCH (t:Transacao {transacao_id: row.transacao_id})
MATCH (ip:IP {ip_id: row.ip_id})
MERGE (t)-[r:ORIGINOU_DE]->(ip)
SET
    r.data_hora = datetime(row.data_hora),
    r.tipo_transacao = row.tipo_transacao,
    r.rule_score = toFloat(row.rule_score),
    r.risk_band = row.risk_band;

// Transação utilizou Cartão
LOAD CSV WITH HEADERS FROM 'file:///rel_transacao_cartao.csv' AS row
MATCH (t:Transacao {transacao_id: row.transacao_id})
MATCH (c:Cartao {cartao_id: row.cartao_id})
MERGE (t)-[r:UTILIZOU]->(c)
SET
    r.data_hora = datetime(row.data_hora),
    r.tipo_transacao = row.tipo_transacao,
    r.rule_score = toFloat(row.rule_score),
    r.risk_band = row.risk_band;

// Transação acionou Regra
LOAD CSV WITH HEADERS FROM 'file:///rel_transacao_regra.csv' AS row
MATCH (t:Transacao {transacao_id: row.transacao_id})
MATCH (reg:Regra {rule_id: row.rule_id})
MERGE (t)-[r:ACIONOU]->(reg)
SET
    r.rule_name = row.rule_name,
    r.pontos_regra = toInteger(row.pontos_regra),
    r.severidade = row.severidade,
    r.rule_score = toFloat(row.rule_score),
    r.risk_band = row.risk_band,
    r.fraud_scenario = row.fraud_scenario;

// Relação agregada Conta-Dispositivo
LOAD CSV WITH HEADERS FROM 'file:///rel_conta_device_agg.csv' AS row
MATCH (a:Conta {conta_id: row.conta_origem_id})
MATCH (d:Dispositivo {device_id: row.device_id})
MERGE (a)-[r:USOU_DISPOSITIVO]->(d)
SET
    r.qtd_transacoes = toInteger(row.qtd_transacoes),
    r.valor_total = toFloat(row.valor_total),
    r.valor_medio = toFloat(row.valor_medio),
    r.score_max = toFloat(row.score_max),
    r.score_medio = toFloat(row.score_medio),
    r.taxa_fraude_sintetica = toFloat(row.taxa_fraude_sintetica),
    r.qtd_alertas = toInteger(row.qtd_alertas);

// Relação agregada Conta-Beneficiário
LOAD CSV WITH HEADERS FROM 'file:///rel_conta_beneficiario_agg.csv' AS row
MATCH (a:Conta {conta_id: row.conta_origem_id})
MATCH (b:Beneficiario {beneficiario_id: row.beneficiario_id})
MERGE (a)-[r:ENVIOU_PARA_BENEFICIARIO]->(b)
SET
    r.qtd_transacoes = toInteger(row.qtd_transacoes),
    r.valor_total = toFloat(row.valor_total),
    r.valor_medio = toFloat(row.valor_medio),
    r.score_max = toFloat(row.score_max),
    r.score_medio = toFloat(row.score_medio),
    r.taxa_fraude_sintetica = toFloat(row.taxa_fraude_sintetica),
    r.qtd_alertas = toInteger(row.qtd_alertas);

// Relação agregada Conta-IP
LOAD CSV WITH HEADERS FROM 'file:///rel_conta_ip_agg.csv' AS row
MATCH (a:Conta {conta_id: row.conta_origem_id})
MATCH (ip:IP {ip_id: row.ip_id})
MERGE (a)-[r:USOU_IP]->(ip)
SET
    r.qtd_transacoes = toInteger(row.qtd_transacoes),
    r.valor_total = toFloat(row.valor_total),
    r.valor_medio = toFloat(row.valor_medio),
    r.score_max = toFloat(row.score_max),
    r.score_medio = toFloat(row.score_medio),
    r.taxa_fraude_sintetica = toFloat(row.taxa_fraude_sintetica),
    r.qtd_alertas = toInteger(row.qtd_alertas);