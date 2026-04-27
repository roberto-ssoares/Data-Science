# Graph Summary v0.1 — Databricks Learning Knowledge Graph

## Projeto

Databricks Certification Learning Knowledge Graph

## Visão geral estrutural

| Métrica                                   | Valor    |
| ----------------------------------------- | --------:|
| Total de nós                              | 93       |
| Total de relacionamentos MultiDiGraph     | 172      |
| Total de relacionamentos projeção simples | 172      |
| Densidade da projeção simples             | 0.020103 |
| Componentes fracamente conectados         | 2        |
| Grafo fracamente conectado                | False    |

## Nós mais conectados

| node_id  | name                              | node_label | total_degree | degree_centrality |
|:-------- |:--------------------------------- |:---------- | ------------:| -----------------:|
| SNAP_W00 | 2026-04-27                        | Snapshot   | 46           | 0.5               |
| D03      | Data Processing & Transformations | ExamDomain | 14           | 0.152174          |
| T001     | Lakehouse Architecture            | Topic      | 14           | 0.152174          |
| T020     | Medallion Architecture            | Topic      | 11           | 0.119565          |
| T038     | Unity Catalog                     | Topic      | 11           | 0.119565          |
| D02      | Development and Ingestion         | ExamDomain | 10           | 0.108696          |
| D04      | Productionizing Data Pipelines    | ExamDomain | 10           | 0.108696          |
| D05      | Data Governance & Quality         | ExamDomain | 10           | 0.108696          |
| T016     | Delta Lake                        | Topic      | 10           | 0.108696          |
| T021     | MERGE INTO                        | Topic      | 8            | 0.086957          |

## Tópicos mais conectados

| node_id | name                   | total_degree | degree_centrality |
|:------- |:---------------------- | ------------:| -----------------:|
| T001    | Lakehouse Architecture | 14           | 0.152174          |
| T020    | Medallion Architecture | 11           | 0.119565          |
| T038    | Unity Catalog          | 11           | 0.119565          |
| T016    | Delta Lake             | 10           | 0.108696          |
| T021    | MERGE INTO             | 8            | 0.086957          |
| T007    | Data Ingestion         | 7            | 0.076087          |
| T029    | Databricks Workflows   | 7            | 0.076087          |
| T030    | Jobs                   | 7            | 0.076087          |
| T045    | Data Quality           | 7            | 0.076087          |
| T031    | Tasks                  | 6            | 0.065217          |

## Resumo por tipo de nó

| node_label    | total_nodes | avg_total_degree | max_total_degree | avg_centrality |
|:------------- | -----------:| ----------------:| ----------------:| --------------:|
| Snapshot      | 1           | 46               | 46               | 0.5            |
| ExamDomain    | 5           | 10.2             | 14               | 0.11087        |
| Certification | 1           | 5                | 5                | 0.054348       |
| StudySession  | 1           | 4                | 4                | 0.043478       |
| Topic         | 46          | 3.95652          | 14               | 0.0430057      |
| Resource      | 4           | 2.5              | 4                | 0.027174       |
| Skill         | 6           | 1.83333          | 2                | 0.0199275      |
| Lab           | 4           | 1.75             | 3                | 0.019022       |
| Notebook      | 5           | 1.6              | 3                | 0.0173916      |
| Subtopic      | 20          | 1                | 1                | 0.01087        |

## Interpretação inicial

A primeira versão do Knowledge Graph já permite identificar conceitos estruturantes da jornada de certificação Databricks.

Os nós mais conectados tendem a representar tópicos, domínios ou artefatos com maior papel de integração dentro do plano de estudos.

Nas próximas etapas, o grafo será enriquecido com novas sessões de estudo, novos snapshots temporais, dúvidas, erros, insights e evidências práticas.
