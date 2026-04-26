# Neo4j Graph Modeling — Manifesto de Carga

Este documento registra os artefatos gerados pelo Notebook 04.

## Arquivos CSV Gerados

| arquivo                        | tipo         | nome_logico                |   linhas |
|:-------------------------------|:-------------|:---------------------------|---------:|
| nodes_beneficiarios.csv        | node         | nodes_beneficiarios        |     3500 |
| nodes_cartoes.csv              | node         | nodes_cartoes              |     4000 |
| nodes_clientes.csv             | node         | nodes_clientes             |     5000 |
| nodes_contas.csv               | node         | nodes_contas               |     6000 |
| nodes_dispositivos.csv         | node         | nodes_dispositivos         |     4500 |
| nodes_ips.csv                  | node         | nodes_ips                  |     3000 |
| nodes_regras.csv               | node         | nodes_regras               |       10 |
| nodes_transacoes.csv           | node         | nodes_transacoes           |    80000 |
| rel_cliente_conta.csv          | relationship | rel_cliente_conta          |     6000 |
| rel_conta_beneficiario_agg.csv | relationship | rel_conta_beneficiario_agg |    79411 |
| rel_conta_device_agg.csv       | relationship | rel_conta_device_agg       |    79329 |
| rel_conta_ip_agg.csv           | relationship | rel_conta_ip_agg           |    79326 |
| rel_conta_transacao.csv        | relationship | rel_conta_transacao        |    80000 |
| rel_transacao_beneficiario.csv | relationship | rel_transacao_beneficiario |    80000 |
| rel_transacao_cartao.csv       | relationship | rel_transacao_cartao       |     6278 |
| rel_transacao_device.csv       | relationship | rel_transacao_device       |    80000 |
| rel_transacao_ip.csv           | relationship | rel_transacao_ip           |    80000 |
| rel_transacao_regra.csv        | relationship | rel_transacao_regra        |   221277 |

## Scripts Cypher Gerados

|   ordem | arquivo                               | descricao                               |
|--------:|:--------------------------------------|:----------------------------------------|
|       1 | 01_constraints_indexes.cypher         | Cria constraints e índices.             |
|       2 | 02_load_nodes.cypher                  | Carrega os nós do grafo.                |
|       3 | 03_load_relationships.cypher          | Carrega os relacionamentos do grafo.    |
|       4 | 04_fraud_investigation_queries.cypher | Consultas investigativas iniciais.      |
|       5 | 05_gds_algorithms.cypher              | Esboço inicial para Graph Data Science. |

## Ordem Recomendada de Execução no Neo4j

1. Copiar os arquivos CSV de `data/03-gold/neo4j_import/` para a pasta `import` do Neo4j.
2. Executar `cypher/01_constraints_indexes.cypher`.
3. Executar `cypher/02_load_nodes.cypher`.
4. Executar `cypher/03_load_relationships.cypher`.
5. Validar a carga com consultas de contagem.
6. Executar `cypher/04_fraud_investigation_queries.cypher`.
7. Usar `cypher/05_gds_algorithms.cypher` como base para o Notebook 05.

## Observação

Os CSVs são derivados dos dados sintéticos e podem ser recriados executando o notebook.
Os scripts Cypher são versionáveis e documentam a estrutura de carga do Knowledge Graph.
