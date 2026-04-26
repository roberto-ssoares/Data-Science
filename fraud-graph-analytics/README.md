# Fraud Graph Analytics

## Prevenção a Fraudes Transacionais com Knowledge Graph, Regras Explicáveis e Graph Analytics

![Status](https://img.shields.io/badge/status-MVP%20conclu%C3%ADdo-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Graph Analytics](https://img.shields.io/badge/Graph%20Analytics-NetworkX%20%7C%20Neo4j-purple)
![Methodology](https://img.shields.io/badge/Methodology-CRISP--DM%2B-orange)
![Data](https://img.shields.io/badge/Data-Synthetic-lightgrey)

---

## 1. Visão Geral

O **Fraud Graph Analytics** é um MVP analítico para **prevenção a fraudes transacionais**, desenvolvido para demonstrar como combinar **regras antifraude explicáveis**, **Knowledge Graph**, **algoritmos de grafo** e **score final de risco** em uma solução reprodutível de portfólio.

O projeto simula um ambiente financeiro com clientes, contas, transações, dispositivos, IPs, beneficiários, cartões e regras antifraude. A partir dessa base sintética, são criadas camadas analíticas para investigar padrões como:

* dispositivos compartilhados por múltiplas contas;
* beneficiários concentradores;
* contas novas com transações de alto valor;
* transações em rajada;
* IPs recorrentes;
* contas ponte;
* comunidades suspeitas;
* transações com múltiplas regras acionadas.

A proposta não é criar um sistema produtivo de bloqueio antifraude, mas sim um **case técnico e executivo** que conecta negócio, dados, regras, grafos, explicabilidade e narrativa de portfólio.

---

## 2. Problema de Negócio

Fraudes transacionais raramente aparecem como eventos isolados. Em muitos casos, o risco surge a partir de **relações indiretas** entre entidades, como contas, dispositivos, beneficiários, IPs e padrões de movimentação.

Uma análise puramente tabular pode identificar transações atípicas, mas tende a perder relações estruturais como:

* várias contas usando o mesmo dispositivo;
* diferentes clientes transacionando para o mesmo beneficiário;
* grupos de contas conectados por IPs e dispositivos comuns;
* contas intermediárias conectando regiões distintas da rede;
* comunidades com alta concentração de alertas.

Este projeto propõe uma abordagem híbrida:

> **Regras explicáveis para capturar sinais transacionais + Graph Analytics para capturar risco relacional.**

---

## 3. Objetivo do Projeto

Construir um MVP de prevenção a fraudes transacionais capaz de:

1. gerar dados sintéticos orientados ao domínio antifraude;
2. aplicar análise exploratória para identificar padrões de risco;
3. construir um motor de regras antifraude explicável;
4. modelar entidades e relações em formato de Knowledge Graph;
5. aplicar algoritmos de grafo para detectar entidades e comunidades suspeitas;
6. combinar regras e sinais estruturais em um **Fraud Risk Score final**;
7. produzir explicações textuais para priorização de alertas;
8. empacotar o projeto em narrativa executiva para GitHub, portfólio e entrevistas.

---

## 4. Metodologia — CRISP-DM+

O projeto segue uma abordagem inspirada no **CRISP-DM**, enriquecida com uma etapa inicial de entendimento semântico do domínio.

Essa abordagem foi chamada de **CRISP-DM+**.

### Etapa 0 — Domain Understanding Semântico

Antes da geração dos dados e da modelagem, o projeto define:

* ontologia inicial do domínio antifraude;
* Business Language Model;
* taxonomia de fraudes;
* hipóteses investigativas;
* desenho conceitual do Knowledge Graph.

Essa etapa ajuda a transformar conhecimento de negócio em estruturas que orientam dados, regras, features e grafos.

### Jornada Analítica

| Etapa                     | Descrição                                            |
| ------------------------- | ---------------------------------------------------- |
| 00 — Domain Understanding | Ontologia, BLM, taxonomia e hipóteses investigativas |
| 01 — Synthetic Data       | Geração de dados sintéticos transacionais            |
| 02 — EDA                  | Análise exploratória dos padrões de fraude           |
| 03 — Rules Engine         | Motor de regras antifraude explicável                |
| 04 — Graph Modeling       | Modelagem do Knowledge Graph para Neo4j              |
| 05 — Graph Algorithms     | Centralidade, comunidades e ranking estrutural       |
| 06 — Risk Score           | Score final com explicabilidade                      |
| 07 — Portfolio Packaging  | Conclusão executiva e empacotamento                  |

---

## 5. Arquitetura Analítica

```text
Synthetic Data
     ↓
EDA Transacional
     ↓
Motor de Regras Antifraude
     ↓
Knowledge Graph Modeling
     ↓
Graph Algorithms
     ↓
Fraud Risk Score
     ↓
Explicabilidade e Portfólio
```

### Camadas do MVP

| Camada                      | Descrição                                         | Saída                       |
| --------------------------- | ------------------------------------------------- | --------------------------- |
| Domain Understanding        | Ontologia, BLM e taxonomia                        | Base conceitual do projeto  |
| Synthetic Data Layer        | Dados sintéticos de clientes, contas e transações | Arquivos Parquet recriáveis |
| EDA & Feature Understanding | Exploração de padrões transacionais               | Achados e regras candidatas |
| Rules Engine                | Regras antifraude explicáveis                     | Rule score e alertas        |
| Knowledge Graph Modeling    | Nós e relacionamentos para Neo4j                  | CSVs e scripts Cypher       |
| Graph Algorithms            | Centralidade, comunidades e risco estrutural      | Entity Graph Risk Score     |
| Final Risk Score            | Combinação de regras e grafo                      | Fraud Risk Score final      |
| Portfolio Packaging         | Documentação e narrativa executiva                | README, docs e reports      |

---

## 6. Dados Sintéticos

O projeto utiliza exclusivamente **dados sintéticos**, criados para fins educacionais, analíticos e de portfólio.

Nenhum dado real de cliente, banco, instituição financeira ou transação foi utilizado.

### Entidades simuladas

| Entidade     | Descrição                              |
| ------------ | -------------------------------------- |
| Cliente      | Pessoa física simulada                 |
| Conta        | Conta transacional vinculada a cliente |
| Transação    | Evento financeiro sintético            |
| Dispositivo  | Dispositivo usado na transação         |
| IP           | Origem técnica da operação             |
| Beneficiário | Recebedor da transação                 |
| Cartão       | Cartão vinculado a conta               |
| Regra        | Regra antifraude acionada              |

### Cenários de fraude simulados

| Cenário                    | Descrição                                      |
| -------------------------- | ---------------------------------------------- |
| `shared_device_ring`       | Várias contas usando o mesmo dispositivo       |
| `beneficiary_concentrator` | Muitos envios para o mesmo beneficiário        |
| `new_account_high_value`   | Conta nova realizando transações de alto valor |
| `burst_transactions`       | Múltiplas transações em curto intervalo        |
| `bridge_account`           | Conta atuando como intermediária               |
| `coordinated_network`      | Rede coordenada com entidades compartilhadas   |
| `normal`                   | Transações sem marcação sintética de fraude    |

---

## 7. Motor de Regras Antifraude

O motor de regras transforma achados da EDA em sinais explicáveis.

Cada regra possui:

* identificador;
* nome;
* descrição;
* racional de negócio;
* severidade;
* pontuação;
* tipo de sinal.

### Regras implementadas

| Regra | Nome                                  | Sinal capturado                             |
| ----- | ------------------------------------- | ------------------------------------------- |
| R001  | Alto valor transacional               | Valor acima do percentil 95                 |
| R002  | Valor acima do limite diário          | Uso elevado do limite transacional          |
| R003  | Conta nova com alto valor             | Conta recente movimentando valor alto       |
| R004  | Dispositivo compartilhado             | Device usado por múltiplas contas           |
| R005  | Beneficiário concentrador             | Recebedor com muitas contas de origem       |
| R006  | Rede ou device de alto risco          | IP ou fingerprint com risco técnico         |
| R007  | Rajada transacional horária           | Muitas transações na mesma hora             |
| R008  | Muitos beneficiários no dia           | Pulverização de destinos                    |
| R009  | IP compartilhado por múltiplas contas | Origem técnica recorrente                   |
| R010  | Canal digital com alto valor          | Alto valor via app, internet banking ou API |

O resultado dessa etapa é um **Rule Score** por transação, acompanhado de explicação textual.

---

## 8. Knowledge Graph

A modelagem em grafo permite representar relações entre entidades do domínio antifraude.

### Principais nós

```text
(:Cliente)
(:Conta)
(:Transacao)
(:Beneficiario)
(:Dispositivo)
(:IP)
(:Cartao)
(:Regra)
```

### Principais relacionamentos

```text
(:Cliente)-[:POSSUI]->(:Conta)
(:Conta)-[:REALIZOU]->(:Transacao)
(:Transacao)-[:ENVIOU_PARA]->(:Beneficiario)
(:Transacao)-[:USOU]->(:Dispositivo)
(:Transacao)-[:ORIGINOU_DE]->(:IP)
(:Transacao)-[:UTILIZOU]->(:Cartao)
(:Transacao)-[:ACIONOU]->(:Regra)
(:Conta)-[:USOU_DISPOSITIVO]->(:Dispositivo)
(:Conta)-[:ENVIOU_PARA_BENEFICIARIO]->(:Beneficiario)
(:Conta)-[:USOU_IP]->(:IP)
```

A pasta [`cypher/`](cypher/) contém scripts para:

* criação de constraints e índices;
* carga de nós;
* carga de relacionamentos;
* consultas investigativas;
* consultas conceituais para Neo4j Graph Data Science.

---

## 9. Algoritmos de Grafo

O projeto aplica algoritmos de grafo para identificar entidades e comunidades suspeitas.

| Algoritmo / Métrica     | Objetivo antifraude                                 |
| ----------------------- | --------------------------------------------------- |
| Degree Centrality       | Identificar entidades muito conectadas              |
| Weighted Degree         | Priorizar conexões com maior peso, score ou alertas |
| PageRank                | Encontrar entidades estruturalmente relevantes      |
| Connected Components    | Mapear grupos conectados                            |
| Community Detection     | Detectar comunidades suspeitas                      |
| Betweenness aproximado  | Identificar possíveis contas ponte                  |
| Community Risk Score    | Priorizar grupos conectados com maior risco         |
| Entity Graph Risk Score | Medir risco estrutural por entidade                 |

Essa camada complementa o motor de regras ao adicionar contexto relacional.

---

## 10. Fraud Risk Score Final

O score final combina risco transacional e risco estrutural.

### Fórmula conceitual

```text
fraud_risk_score =
    0.45  * rule_score
  + 0.20  * account_graph_risk_score
  + 0.125 * device_graph_risk_score
  + 0.125 * beneficiary_graph_risk_score
  + 0.05  * ip_graph_risk_score
  + 0.05  * max_community_risk_score
```

### Faixas de risco

| Faixa   | Critério         |
| ------- | ---------------- |
| Crítico | score >= 80      |
| Alto    | 60 <= score < 80 |
| Médio   | 35 <= score < 60 |
| Baixo   | score < 35       |

Cada transação recebe uma explicação textual combinando:

* regras acionadas;
* score de regras;
* sinais estruturais de conta, dispositivo, beneficiário e IP;
* risco da comunidade associada;
* faixa final de risco.

Exemplo conceitual:

```text
Score final 82.4/100 — risco crítico.
Score de regras: 75.0/100.
Regras acionadas: dispositivo compartilhado; beneficiário concentrador; rajada transacional horária.
Sinais de grafo: dispositivo com alto risco estrutural; comunidade associada com alto risco.
```

---

## 11. Estrutura do Projeto

```text
fraud-graph-analytics/
│
├── notebooks/
│   ├── 00_domain_understanding_crisp_dm_plus.ipynb
│   ├── 01_generate_synthetic_transactions.ipynb
│   ├── 02_eda_transactional_fraud.ipynb
│   ├── 03_rules_engine_antifraud.ipynb
│   ├── 04_graph_modeling_neo4j.ipynb
│   ├── 05_graph_algorithms_fraud_detection.ipynb
│   ├── 06_fraud_risk_score_explainability.ipynb
│   └── 07_executive_conclusion_portfolio.ipynb
│
├── docs/
│   ├── business_glossary.md
│   ├── fraud_taxonomy.md
│   ├── antifraud_rules_catalog.md
│   ├── score_methodology.md
│   ├── graph_modeling_neo4j_summary.md
│   ├── graph_algorithms_fraud_detection_summary.md
│   ├── fraud_risk_score_explainability_summary.md
│   └── executive_conclusion_portfolio.md
│
├── cypher/
│   ├── 01_constraints_indexes.cypher
│   ├── 02_load_nodes.cypher
│   ├── 03_load_relationships.cypher
│   ├── 04_fraud_investigation_queries.cypher
│   ├── 05_gds_algorithms.cypher
│   └── 06_gds_fraud_detection_queries.cypher
│
├── artifacts/
│   ├── figures/
│   └── reports/
│
├── data/
│   ├── 00-raw/
│   ├── 01-bronze/
│   ├── 02-silver/
│   ├── 03-gold/
│   └── synthetic/
│
├── src/
├── tests/
├── pyproject.toml
├── .gitignore
└── README.md
```

> Observação: os arquivos de dados em `data/` são derivados e recriáveis pelos notebooks. Por isso, ficam fora do versionamento principal.

---

## 12. Notebooks

| Notebook | Descrição                                                      | Link                                                           |
| -------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| 00       | Domain Understanding com CRISP-DM+, Ontologia, BLM e Taxonomia | [abrir](notebooks/00_domain_understanding_crisp_dm_plus.ipynb) |
| 01       | Geração de dados sintéticos transacionais                      | [abrir](notebooks/01_generate_synthetic_transactions.ipynb)    |
| 02       | Análise exploratória de fraude transacional                    | [abrir](notebooks/02_eda_transactional_fraud.ipynb)            |
| 03       | Motor de regras antifraude explicável                          | [abrir](notebooks/03_rules_engine_antifraud.ipynb)             |
| 04       | Modelagem do Knowledge Graph para Neo4j                        | [abrir](notebooks/04_graph_modeling_neo4j.ipynb)               |
| 05       | Algoritmos de grafo para detecção de risco                     | [abrir](notebooks/05_graph_algorithms_fraud_detection.ipynb)   |
| 06       | Fraud Risk Score com explicabilidade                           | [abrir](notebooks/06_fraud_risk_score_explainability.ipynb)    |
| 07       | Conclusão executiva e empacotamento                            | [abrir](notebooks/07_executive_conclusion_portfolio.ipynb)     |

---

## 13. Principais Artefatos

### Documentação

| Artefato                                                                           | Descrição                                     |
| ---------------------------------------------------------------------------------- | --------------------------------------------- |
| [`docs/business_glossary.md`](docs/business_glossary.md)                           | Business Language Model do domínio antifraude |
| [`docs/fraud_taxonomy.md`](docs/fraud_taxonomy.md)                                 | Taxonomia inicial de fraudes                  |
| [`docs/antifraud_rules_catalog.md`](docs/antifraud_rules_catalog.md)               | Catálogo de regras antifraude                 |
| [`docs/score_methodology.md`](docs/score_methodology.md)                           | Metodologia do score final                    |
| [`docs/executive_conclusion_portfolio.md`](docs/executive_conclusion_portfolio.md) | Conclusão executiva do projeto                |

### Scripts Cypher

| Script                                                                                         | Finalidade                              |
| ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| [`cypher/01_constraints_indexes.cypher`](cypher/01_constraints_indexes.cypher)                 | Constraints e índices                   |
| [`cypher/02_load_nodes.cypher`](cypher/02_load_nodes.cypher)                                   | Carga de nós                            |
| [`cypher/03_load_relationships.cypher`](cypher/03_load_relationships.cypher)                   | Carga de relacionamentos                |
| [`cypher/04_fraud_investigation_queries.cypher`](cypher/04_fraud_investigation_queries.cypher) | Consultas investigativas                |
| [`cypher/06_gds_fraud_detection_queries.cypher`](cypher/06_gds_fraud_detection_queries.cypher) | Consultas complementares para Neo4j GDS |

---

## 14. Como Reproduzir o Projeto

### 14.1 Pré-requisitos

* Python 3.12+
* Git
* Jupyter Lab ou VS Code
* Opcional: Neo4j Desktop ou Neo4j em Docker

### 14.2 Clonar o repositório

```bash
git clone https://github.com/roberto-ssoares/Data-Science.git
cd Data-Science/fraud-graph-analytics
```

### 14.3 Criar ambiente virtual com `uv`

```bash
uv venv
```

No Windows PowerShell:

```powershell
.venv\Scripts\activate
```

Instalar dependências:

```bash
uv sync
```

### 14.4 Registrar kernel do Jupyter

```bash
python -m ipykernel install --user --name fraud-graph-analytics --display-name "Python 3.12 - Fraud Graph Analytics"
```

### 14.5 Executar notebooks em ordem

Execute os notebooks de `00` a `07`.

A ordem é importante porque cada notebook gera artefatos utilizados pelos próximos.

```text
00 → 01 → 02 → 03 → 04 → 05 → 06 → 07
```

---

## 15. Como Carregar no Neo4j

O Notebook 04 gera arquivos CSV em:

```text
data/03-gold/neo4j_import/
```

Para carregar no Neo4j:

1. copie os CSVs para a pasta `import` da instância Neo4j;
2. execute os scripts Cypher na seguinte ordem:

```text
cypher/01_constraints_indexes.cypher
cypher/02_load_nodes.cypher
cypher/03_load_relationships.cypher
cypher/04_fraud_investigation_queries.cypher
```

O arquivo abaixo contém consultas complementares para Neo4j Graph Data Science:

```text
cypher/06_gds_fraud_detection_queries.cypher
```

---

## 16. Stack Técnica

| Categoria            | Ferramentas                          |
| -------------------- | ------------------------------------ |
| Linguagem            | Python 3.12                          |
| Manipulação de dados | Pandas, NumPy                        |
| Dados sintéticos     | Faker                                |
| Visualização         | Plotly, Matplotlib                   |
| Grafos               | NetworkX, Neo4j, Cypher              |
| Metodologia          | CRISP-DM+, Ontologia, BLM, Taxonomia |
| Empacotamento        | Markdown, GitHub, Jupyter Notebooks  |
| Ambiente             | uv, VS Code, Jupyter Lab             |

---

## 17. Valor para Portfólio

Este projeto foi desenhado para demonstrar competências relevantes em dados, risco e prevenção a fraudes:

* entendimento de problema de negócio;
* estruturação semântica com ontologia e BLM;
* geração de dados sintéticos orientados ao domínio;
* análise exploratória com interpretação antifraude;
* criação de regras explicáveis;
* modelagem de Knowledge Graph;
* uso de algoritmos de grafos;
* criação de score final interpretável;
* documentação executiva;
* organização reprodutível de projeto.

O case é especialmente aderente a posições de:

* Cientista de Dados;
* Analista de Prevenção a Fraudes;
* Analista de Dados Sênior;
* Especialista em Analytics;
* Engenheiro Analítico;
* Profissional de Graph Analytics;
* Profissional de Risco, Crédito e Fraude.

---

## 18. Limitações

Este projeto é um MVP e possui limitações importantes:

| Limitação                  | Observação                                                                 |
| -------------------------- | -------------------------------------------------------------------------- |
| Dados sintéticos           | Não representam comportamento real de uma instituição financeira           |
| Score heurístico           | Pesos definidos por racional analítico, não por treinamento supervisionado |
| Validação operacional      | Não há validação em ambiente real de prevenção a fraudes                   |
| Neo4j opcional             | Scripts são gerados, mas a execução local depende do ambiente do usuário   |
| Temporalidade simplificada | Janelas móveis e sequências temporais podem ser aprofundadas               |

Essas limitações são intencionais para manter o projeto seguro, reprodutível e adequado a portfólio.

---

## 19. Próximas Evoluções

A evolução natural do projeto inclui:

* executar a carga completa no Neo4j;
* aplicar Neo4j Graph Data Science em ambiente local;
* criar dashboard Streamlit investigativo;
* incluir modelo supervisionado comparando regras com Machine Learning;
* criar página HTML premium no portfólio;
* publicar post técnico no LinkedIn;
* exportar notebooks para HTML com template de portfólio.

---

## 20. Considerações Éticas

Soluções antifraude exigem responsabilidade, governança e cuidado com falsos positivos.

Mesmo sendo um projeto sintético, alguns princípios foram considerados:

* não utilizar dados reais de clientes;
* manter explicabilidade dos alertas;
* evitar decisão automática de bloqueio;
* tratar o score como priorização investigativa;
* documentar regras, metodologia e limitações;
* reconhecer a necessidade de validação humana em contexto real.

---

## 21. Conclusão

O **Fraud Graph Analytics** demonstra como uma solução antifraude pode ser construída combinando **regras explicáveis**, **Knowledge Graph**, **Graph Analytics** e **score final interpretável**.

O projeto parte de uma base conceitual com CRISP-DM+, evolui para dados sintéticos, análise exploratória, motor de regras, modelagem em grafo, algoritmos estruturais e explicabilidade.

A principal contribuição do MVP está em mostrar que a prevenção a fraudes pode ganhar força quando a análise deixa de olhar apenas para eventos isolados e passa a considerar também as **relações entre entidades**.

> Fraude é um problema transacional, mas também é um problema relacional.

---

## Autor

**Roberto dos Santos Soares**
Profissional de Dados | BI | Analytics | Ciência de Dados | Engenharia Analítica

GitHub: [roberto-ssoares](https://github.com/roberto-ssoares)
LinkedIn: [roberto-dos-santos-soares](https://www.linkedin.com/in/roberto-dos-santos-soares/)
