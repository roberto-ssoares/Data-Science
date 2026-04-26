// Clientes
LOAD CSV WITH HEADERS FROM 'file:///nodes_clientes.csv' AS row
MERGE (n:Cliente {cliente_id: row.cliente_id})
SET
    n.idade = toInteger(row.idade),
    n.uf = row.uf,
    n.segmento = row.segmento,
    n.data_cadastro = date(row.data_cadastro),
    n.score_cadastral = toInteger(row.score_cadastral);

// Contas
LOAD CSV WITH HEADERS FROM 'file:///nodes_contas.csv' AS row
MERGE (n:Conta {conta_id: row.conta_id})
SET
    n.cliente_id = row.cliente_id,
    n.tipo_conta = row.tipo_conta,
    n.data_abertura = date(row.data_abertura),
    n.status_conta = row.status_conta,
    n.limite_transacional_diario = toFloat(row.limite_transacional_diario);

// Transações
LOAD CSV WITH HEADERS FROM 'file:///nodes_transacoes.csv' AS row
MERGE (n:Transacao {transacao_id: row.transacao_id})
SET
    n.conta_origem_id = row.conta_origem_id,
    n.beneficiario_id = row.beneficiario_id,
    n.device_id = row.device_id,
    n.ip_id = row.ip_id,
    n.cartao_id = row.cartao_id,
    n.valor = toFloat(row.valor),
    n.data_hora = datetime(row.data_hora),
    n.tipo_transacao = row.tipo_transacao,
    n.canal = row.canal,
    n.status_transacao = row.status_transacao,
    n.is_fraud = toBoolean(row.is_fraud),
    n.fraud_scenario = row.fraud_scenario,
    n.qtd_regras_acionadas = toInteger(row.qtd_regras_acionadas),
    n.rule_score = toFloat(row.rule_score),
    n.risk_band = row.risk_band,
    n.alerta_gerado = toBoolean(row.alerta_gerado);

// Beneficiários
LOAD CSV WITH HEADERS FROM 'file:///nodes_beneficiarios.csv' AS row
MERGE (n:Beneficiario {beneficiario_id: row.beneficiario_id})
SET
    n.tipo_beneficiario = row.tipo_beneficiario,
    n.banco_destino = row.banco_destino,
    n.uf_destino = row.uf_destino;

// Dispositivos
LOAD CSV WITH HEADERS FROM 'file:///nodes_dispositivos.csv' AS row
MERGE (n:Dispositivo {device_id: row.device_id})
SET
    n.tipo_device = row.tipo_device,
    n.sistema_operacional = row.sistema_operacional,
    n.fingerprint_risco = row.fingerprint_risco;

// IPs
LOAD CSV WITH HEADERS FROM 'file:///nodes_ips.csv' AS row
MERGE (n:IP {ip_id: row.ip_id})
SET
    n.uf_origem = row.uf_origem,
    n.tipo_rede = row.tipo_rede,
    n.risco_rede = row.risco_rede;

// Cartões
LOAD CSV WITH HEADERS FROM 'file:///nodes_cartoes.csv' AS row
MERGE (n:Cartao {cartao_id: row.cartao_id})
SET
    n.conta_id = row.conta_id,
    n.tipo_cartao = row.tipo_cartao,
    n.status_cartao = row.status_cartao,
    n.data_emissao = date(row.data_emissao);

// Regras
LOAD CSV WITH HEADERS FROM 'file:///nodes_regras.csv' AS row
MERGE (n:Regra {rule_id: row.rule_id})
SET
    n.rule_name = row.rule_name,
    n.severidade = row.severidade,
    n.pontos = toInteger(row.pontos),
    n.tipo_sinal = row.tipo_sinal;