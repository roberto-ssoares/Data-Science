# Learning Evidence Ingestion W01 — Databricks Learning KG

## Projeto

Databricks Certification Learning Knowledge Graph

## Fonte da evidência

Projeto: `databricks-credit-risk-lakehouse`  
Notebook: `01_lakehouse_fundamentals.ipynb`  
Data: 2026-04-29

## Evidências incorporadas

| evidence_id    | topic                  | topic_id   | evidence_type               |   confidence_delta_suggested |   mastery_delta_suggested |
|:---------------|:-----------------------|:-----------|:----------------------------|-----------------------------:|--------------------------:|
| EVID_CR_LH_001 | Lakehouse Architecture | T001       | conceptual_study            |                         0.2  |                      0.05 |
| EVID_CR_LH_002 | Medallion Architecture | T020       | architecture_mapping        |                         0.2  |                      0.1  |
| EVID_CR_LH_003 | Delta Lake             | T016       | conceptual_study            |                         0.1  |                      0    |
| EVID_CR_LH_004 | Managed Table          | T018       | conceptual_study            |                         0.1  |                      0    |
| EVID_CR_LH_005 | External Table         | T019       | conceptual_study            |                         0.1  |                      0    |
| EVID_CR_LH_006 | Naming Conventions     | T046       | project_standard            |                         0.1  |                      0.05 |
| EVID_CR_LH_007 | Data Ingestion         | T007       | raw_layer_preparation       |                         0.15 |                      0.05 |
| EVID_CR_LH_008 | File Formats           | T011       | csv_generation              |                         0.1  |                      0.05 |
| EVID_CR_LH_009 | Schema Definition      | T013       | schema_documentation        |                         0.15 |                      0.05 |
| EVID_CR_LH_010 | Data Quality           | T045       | raw_quality_profile         |                         0.1  |                      0.05 |
| EVID_CR_LH_011 | Naming Conventions     | T046       | raw_file_naming             |                         0.05 |                      0.05 |
| EVID_CR_LH_012 | Data Ingestion         | T007       | raw_to_bronze_ingestion     |                         0.15 |                      0.1  |
| EVID_CR_LH_013 | File Formats           | T011       | csv_to_parquet_conversion   |                         0.15 |                      0.1  |
| EVID_CR_LH_014 | Schema Definition      | T013       | bronze_schema_tracking      |                         0.1  |                      0.05 |
| EVID_CR_LH_015 | Pipeline Idempotency   | T037       | idempotent_overwrite        |                         0.1  |                      0.1  |
| EVID_CR_LH_016 | Medallion Architecture | T020       | bronze_layer_implementation |                         0.1  |                      0.1  |
| EVID_CR_LH_017 | Data Quality           | T045       | bronze_quality_profile      |                         0.1  |                      0.05 |

## Validação Neo4j

| check                   |   total |
|:------------------------|--------:|
| learning_evidence_nodes |      19 |
| evidence_relationships  |      45 |
| project_evidence_paths  |     123 |

## Snapshot W01 real

| snapshot_id   | snapshot_date   |   week_number |   overall_progress |   coverage_pct |   avg_confidence |   avg_mastery | main_gap                                                                                                | main_achievement                                                                       |
|:--------------|:----------------|--------------:|-------------------:|---------------:|-----------------:|--------------:|:--------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| SNAP_W01_REAL | 2026-04-29      |             1 |             0.1087 |         0.4783 |           0.2576 |        0.1087 | Ainda faltam práticas reais em ingestão Databricks, Delta Lake, Workflows, Jobs, Tasks e Unity Catalog. | Primeira evidência real do projeto databricks-credit-risk-lakehouse incorporada ao KG. |

## Leitura executiva

O Knowledge Graph passou a incorporar evidências reais vindas do projeto prático `databricks-credit-risk-lakehouse`.

A partir deste ponto, a evolução dos tópicos da certificação Databricks será baseada em artefatos concretos: notebooks, estudos aplicados, práticas, cargas, consultas e entregáveis de portfólio.

Esta etapa estabelece a ponte entre estudo prático e monitoramento semântico da jornada de aprendizagem.
