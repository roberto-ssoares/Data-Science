# Fraud Graph Analytics

MVP de prevenção a fraudes transacionais com **Knowledge Graph**, **regras explicáveis**, **análise de redes** e **CRISP-DM+**.

## Objetivo do Projeto

Construir um projeto analítico para simular, detectar e explicar padrões suspeitos em transações financeiras, combinando:

- dados sintéticos orientados ao domínio de prevenção a fraudes;
- regras antifraude explicáveis;
- modelagem em grafo;
- algoritmos de centralidade e detecção de comunidades;
- score de risco transacional;
- documentação executiva para portfólio.

## Contexto de Negócio

Fraudes transacionais geralmente não aparecem apenas em uma transação isolada. Elas podem surgir a partir de padrões relacionais, como:

- múltiplas contas usando o mesmo dispositivo;
- beneficiários recebendo valores de várias origens;
- contas novas realizando transações de alto valor;
- transações em rajada em curtos intervalos de tempo;
- grupos de contas conectadas por IP, dispositivo, cartão ou beneficiário;
- comunidades suspeitas com comportamento coordenado.

O projeto busca demonstrar como técnicas de **Data Analytics**, **Graph Analytics** e **explicabilidade operacional** podem apoiar a investigação e priorização de alertas em prevenção a fraudes.

## Metodologia

Este projeto segue uma abordagem baseada em **CRISP-DM+**, enriquecida com:

- Ontologia;
- Business Language Model;
- Taxonomia de fraude;
- Knowledge Graph;
- análise de padrões transacionais;
- regras de negócio explicáveis;
- interpretação executiva dos resultados.

## Estrutura Inicial

```text
fraud-graph-analytics/
├── data/
│   ├── 00-raw/
│   ├── 01-bronze/
│   ├── 02-silver/
│   ├── 03-gold/
│   └── synthetic/
├── notebooks/
├── src/
├── cypher/
├── app/
├── docs/
├── artifacts/
├── tests/
├── README.md
├── pyproject.toml
└── .gitignore
```



## Notebooks Planejados

| Notebook                                      | Descrição                                                     |
| --------------------------------------------- | ------------------------------------------------------------- |
| `00_domain_understanding_crisp_dm_plus.ipynb` | Entendimento do domínio, ontologia, BLM e taxonomia de fraude |
| `01_generate_synthetic_transactions.ipynb`    | Geração de dados sintéticos transacionais                     |
| `02_eda_transactional_fraud.ipynb`            | Análise exploratória dos padrões transacionais                |
| `03_rules_engine_antifraud.ipynb`             | Construção de regras antifraude explicáveis                   |
| `04_graph_modeling_neo4j.ipynb`               | Modelagem do grafo e carga no Neo4j                           |
| `05_graph_algorithms_fraud_detection.ipynb`   | Aplicação de centralidade, comunidades e análise estrutural   |
| `06_fraud_risk_score_explainability.ipynb`    | Score de risco e explicabilidade                              |
| `07_executive_conclusion_portfolio.ipynb`     | Conclusão executiva e empacotamento para portfólio            |

## Stack Técnica

- Python
- DuckDB
- Pandas / Polars
- Neo4j
- Cypher
- NetworkX
- Plotly
- Streamlit
- CRISP-DM+
- Knowledge Graph

## Status

Projeto em desenvolvimento.
