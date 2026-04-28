# Learning Progress Snapshot W01 — Databricks Learning KG

## Projeto

Databricks Certification Learning Knowledge Graph

## Snapshot

| Métrica                            | Valor      |
| ---------------------------------- | ----------:|
| Semana                             | 1          |
| Data do snapshot                   | 2026-04-27 |
| Progresso geral médio              | 0.1043     |
| Cobertura de tópicos com evidência | 0.5        |
| Confiança média                    | 0.2315     |
| Domínio médio                      | 0.1043     |

## Principal conquista

Primeira versão operacional do Knowledge Graph criada, visualizada e carregada no Neo4j.

## Principal lacuna

Prática real em Databricks Workflows, Delta Lake, Auto Loader e Unity Catalog ainda precisa ser aprofundada.

## Tópicos com maior progresso

| topic_id | name                   | confidence_gain | mastery_gain | status_w01    |
|:-------- |:---------------------- | ---------------:| ------------:|:------------- |
| T001     | Lakehouse Architecture | 0.3             | 0.25         | practicing    |
| T020     | Medallion Architecture | 0.25            | 0.25         | consolidating |
| T037     | Pipeline Idempotency   | 0.1             | 0.1          | mapped        |
| T045     | Data Quality           | 0.1             | 0.1          | practicing    |
| T038     | Unity Catalog          | 0.05            | 0.05         | mapped        |
| T029     | Databricks Workflows   | 0.05            | 0            | not_started   |

## Tópicos prioritários ainda frágeis

| topic_id | name                 | category       | priority | confidence_score | mastery_score | status      |
|:-------- |:-------------------- |:-------------- |:-------- | ----------------:| -------------:|:----------- |
| T008     | read_files           | Ingestion      | high     | 0                | 0             | not_started |
| T030     | Jobs                 | Production     | high     | 0                | 0             | not_started |
| T031     | Tasks                | Production     | high     | 0                | 0             | not_started |
| T032     | Task Dependencies    | Production     | high     | 0                | 0             | not_started |
| T029     | Databricks Workflows | Production     | high     | 0.05             | 0             | not_started |
| T021     | MERGE INTO           | Transformation | high     | 0.1              | 0             | not_started |
| T043     | Permissions          | Governance     | high     | 0.1              | 0             | not_started |
| T038     | Unity Catalog        | Governance     | high     | 0.15             | 0.05          | mapped      |
| T007     | Data Ingestion       | Ingestion      | high     | 0.25             | 0.1           | mapped      |
| T012     | Schema Inference     | Ingestion      | high     | 0.25             | 0.1           | mapped      |
| T013     | Schema Definition    | Ingestion      | high     | 0.25             | 0.1           | mapped      |
| T016     | Delta Lake           | Transformation | high     | 0.25             | 0.1           | mapped      |
| T017     | Delta Table          | Transformation | high     | 0.25             | 0.1           | mapped      |
| T037     | Pipeline Idempotency | Production     | high     | 0.35             | 0.2           | mapped      |
| T022     | Window Functions     | Transformation | high     | 0.4              | 0.2           | mapped      |

## Progresso por domínio

| domain_id | name_domain                       | weight_pct | total_topics | avg_confidence | avg_mastery | topics_with_evidence | coverage_pct |
|:--------- |:--------------------------------- | ----------:| ------------:| --------------:| -----------:| --------------------:| ------------:|
| D03       | Data Processing & Transformations | 31         | 13           | 0.3346         | 0.1538      | 8                    | 0.6154       |
| D02       | Development and Ingestion         | 30         | 9            | 0.25           | 0.1167      | 6                    | 0.6667       |
| D04       | Productionizing Data Pipelines    | 18         | 9            | 0.0444         | 0.0222      | 1                    | 0.1111       |
| D05       | Data Governance & Quality         | 11         | 9            | 0.2278         | 0.0944      | 5                    | 0.5556       |
| D01       | Databricks Intelligence Platform  | 10         | 6            | 0.2667         | 0.1167      | 3                    | 0.5          |

## Leitura executiva

A primeira evolução temporal do Knowledge Graph mostra que a jornada já possui evidências fortes em modelagem conceitual, ontologia, visualização de grafo e carga no Neo4j.

Os próximos focos técnicos devem ser direcionados para prática real em Delta Lake, ingestão, Workflows, Jobs, Tasks, Unity Catalog e qualidade de dados na plataforma Databricks.
