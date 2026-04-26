CREATE CONSTRAINT cliente_id_unique IF NOT EXISTS
FOR (n:Cliente) REQUIRE n.cliente_id IS UNIQUE;

CREATE CONSTRAINT conta_id_unique IF NOT EXISTS
FOR (n:Conta) REQUIRE n.conta_id IS UNIQUE;

CREATE CONSTRAINT transacao_id_unique IF NOT EXISTS
FOR (n:Transacao) REQUIRE n.transacao_id IS UNIQUE;

CREATE CONSTRAINT beneficiario_id_unique IF NOT EXISTS
FOR (n:Beneficiario) REQUIRE n.beneficiario_id IS UNIQUE;

CREATE CONSTRAINT device_id_unique IF NOT EXISTS
FOR (n:Dispositivo) REQUIRE n.device_id IS UNIQUE;

CREATE CONSTRAINT ip_id_unique IF NOT EXISTS
FOR (n:IP) REQUIRE n.ip_id IS UNIQUE;

CREATE CONSTRAINT cartao_id_unique IF NOT EXISTS
FOR (n:Cartao) REQUIRE n.cartao_id IS UNIQUE;

CREATE CONSTRAINT regra_id_unique IF NOT EXISTS
FOR (n:Regra) REQUIRE n.rule_id IS UNIQUE;

CREATE INDEX transacao_risk_band IF NOT EXISTS
FOR (n:Transacao) ON (n.risk_band);

CREATE INDEX transacao_rule_score IF NOT EXISTS
FOR (n:Transacao) ON (n.rule_score);

CREATE INDEX regra_severidade IF NOT EXISTS
FOR (n:Regra) ON (n.severidade);