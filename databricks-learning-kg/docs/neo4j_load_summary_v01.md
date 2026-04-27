# Neo4j Load Summary v0.1 — Databricks Learning Knowledge Graph

## Projeto

Databricks Certification Learning Knowledge Graph

## Carga no Neo4j

| Entidade | Total |
|---|---:|
| Nós carregados | 93 |
| Relacionamentos carregados | 172 |

## Nós por tipo

| node_label    |   total |
|:--------------|--------:|
| Topic         |      46 |
| Subtopic      |      20 |
| Skill         |       6 |
| ExamDomain    |       5 |
| Notebook      |       5 |
| Resource      |       4 |
| Lab           |       4 |
| StudySession  |       1 |
| Snapshot      |       1 |
| Certification |       1 |

## Relacionamentos por tipo

| relationship       |   total |
|:-------------------|--------:|
| COVERS             |      46 |
| CAPTURES_STATUS_OF |      46 |
| HAS_SUBTOPIC       |      20 |
| PREREQUISITE_FOR   |      15 |
| SUPPORTED_BY       |      11 |
| TEACHES            |      10 |
| PRACTICES          |       8 |
| IMPLEMENTS         |       7 |
| HAS_DOMAIN         |       5 |
| STUDIED            |       4 |

## Tópicos por domínio

| domain                            |   total_topics |
|:----------------------------------|---------------:|
| Data Processing & Transformations |             13 |
| Development and Ingestion         |              9 |
| Productionizing Data Pipelines    |              9 |
| Data Governance & Quality         |              9 |
| Databricks Intelligence Platform  |              6 |

## Pré-requisitos mais estruturantes

| topic_id   | topic                  |   unlocks_topics |
|:-----------|:-----------------------|-----------------:|
| T007       | Data Ingestion         |                3 |
| T039       | Catalog                |                1 |
| T029       | Databricks Workflows   |                1 |
| T016       | Delta Lake             |                1 |
| T017       | Delta Table            |                1 |
| T030       | Jobs                   |                1 |
| T023       | Joins                  |                1 |
| T001       | Lakehouse Architecture |                1 |
| T040       | Schema                 |                1 |
| T012       | Schema Inference       |                1 |
| T014       | Spark SQL              |                1 |
| T031       | Tasks                  |                1 |
| T038       | Unity Catalog          |                1 |

## Leitura executiva

A carga inicial no Neo4j materializou o Knowledge Graph da jornada de certificação Databricks em uma base de grafos consultável.

A estrutura permite navegar da certificação para domínios, tópicos, subtópicos, notebooks, recursos, skills e snapshots de progresso.

As primeiras consultas já permitem identificar lacunas de evidência prática, tópicos prioritários e conceitos que funcionam como pré-requisitos para outros assuntos.
