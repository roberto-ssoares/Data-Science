# Graph Modeling Neo4j — Resumo Executivo

Este documento consolida os principais resultados do Notebook 04.

## Objetivo

Transformar os dados sintéticos, transações com score e alertas antifraude em uma estrutura de Knowledge Graph compatível com Neo4j.

## Síntese do Modelo

| componente      |   quantidade_tabelas |   quantidade_registros | interpretacao                                              |
|:----------------|---------------------:|-----------------------:|:-----------------------------------------------------------|
| Nós             |                    8 |                 106010 | Entidades principais do domínio antifraude.                |
| Relacionamentos |                   10 |                 791621 | Conexões event-driven e agregadas entre entidades.         |
| Regras como nós |                    1 |                     10 | Permite explicar transações por regras acionadas.          |
| Scripts Cypher  |                    5 |                      5 | Automatizam constraints, carga e consultas investigativas. |

## Nós Gerados

| node_table          |   linhas |   colunas |
|:--------------------|---------:|----------:|
| nodes_clientes      |     5000 |         6 |
| nodes_contas        |     6000 |         6 |
| nodes_transacoes    |    80000 |        17 |
| nodes_beneficiarios |     3500 |         4 |
| nodes_dispositivos  |     4500 |         4 |
| nodes_ips           |     3000 |         4 |
| nodes_cartoes       |     4000 |         5 |
| nodes_regras        |       10 |         5 |

## Relacionamentos Gerados

| relationship_table         |   linhas |   colunas |
|:---------------------------|---------:|----------:|
| rel_cliente_conta          |     6000 |         2 |
| rel_conta_transacao        |    80000 |         9 |
| rel_transacao_beneficiario |    80000 |         7 |
| rel_transacao_device       |    80000 |         6 |
| rel_transacao_ip           |    80000 |         6 |
| rel_transacao_cartao       |     6278 |         6 |
| rel_transacao_regra        |   221277 |         8 |
| rel_conta_device_agg       |    79329 |         9 |
| rel_conta_beneficiario_agg |    79411 |         9 |
| rel_conta_ip_agg           |    79326 |         9 |

## Scripts Cypher

|   ordem | arquivo                               | descricao                               |
|--------:|:--------------------------------------|:----------------------------------------|
|       1 | 01_constraints_indexes.cypher         | Cria constraints e índices.             |
|       2 | 02_load_nodes.cypher                  | Carrega os nós do grafo.                |
|       3 | 03_load_relationships.cypher          | Carrega os relacionamentos do grafo.    |
|       4 | 04_fraud_investigation_queries.cypher | Consultas investigativas iniciais.      |
|       5 | 05_gds_algorithms.cypher              | Esboço inicial para Graph Data Science. |

## Valor Analítico

- Permite investigar conexões indiretas entre contas, dispositivos, IPs e beneficiários.
- Permite explicar transações por meio das regras antifraude acionadas.
- Prepara a base para algoritmos de centralidade e comunidades no Neo4j Graph Data Science.
- Cria uma ponte entre regras explicáveis e análise estrutural de redes.

## Próximo Passo

O próximo notebook será dedicado à aplicação de algoritmos de grafo, como Degree Centrality, PageRank, Louvain e componentes conectados.
