# Notebook 03 — Raw to Bronze Ingestion

## Projeto

Databricks Credit Risk Lakehouse

## Data

2026-04-29

## Objetivo

Realizar a ingestão dos arquivos CSV da camada Raw para a camada Bronze, adicionando metadados técnicos e persistindo os dados em formato Parquet.

## Manifesto da camada Bronze

| entity        | source_file       | target_file                  |   raw_rows |   bronze_rows |   raw_columns |   bronze_columns | target_format   |
|:--------------|:------------------|:-----------------------------|-----------:|--------------:|--------------:|-----------------:|:----------------|
| customers     | customers.csv     | bronze_customers.parquet     |        501 |           501 |            11 |               22 | parquet         |
| contracts     | contracts.csv     | bronze_contracts.parquet     |        622 |           622 |            10 |               21 | parquet         |
| payments      | payments.csv      | bronze_payments.parquet      |      12919 |         12919 |            11 |               22 | parquet         |
| credit_events | credit_events.csv | bronze_credit_events.parquet |        580 |           580 |             8 |               19 | parquet         |

## Reconciliação Raw → Bronze

| entity        |   raw_rows |   bronze_rows | row_count_match   |   raw_columns |   bronze_columns |   metadata_columns_added |
|:--------------|-----------:|--------------:|:------------------|--------------:|-----------------:|-------------------------:|
| customers     |        501 |           501 | True              |            11 |               22 |                       11 |
| contracts     |        622 |           622 | True              |            10 |               21 |                       11 |
| payments      |      12919 |         12919 | True              |            11 |               22 |                       11 |
| credit_events |        580 |           580 | True              |             8 |               19 |                       11 |

## Qualidade inicial da Bronze

| entity        |   rows |   columns |   duplicated_rows |   duplicated_hashes |   total_null_cells |   metadata_columns |
|:--------------|-------:|----------:|------------------:|--------------------:|-------------------:|-------------------:|
| customers     |    501 |        22 |                 0 |                   1 |                 15 |                 11 |
| contracts     |    622 |        21 |                 0 |                   1 |                  6 |                 11 |
| payments      |  12919 |        22 |                 0 |                   1 |                378 |                 11 |
| credit_events |    580 |        19 |                 0 |                   0 |                  6 |                 11 |

## Validação de arquivos Bronze

| entity        | exists   |   file_size_bytes |
|:--------------|:---------|------------------:|
| customers     | True     |             42314 |
| contracts     | True     |             49384 |
| payments      | True     |            521789 |
| credit_events | True     |             41398 |

## Evidências de aprendizagem geradas

| evidence_id    | topic                  | evidence_type               |   confidence_delta_suggested |   mastery_delta_suggested |
|:---------------|:-----------------------|:----------------------------|-----------------------------:|--------------------------:|
| EVID_CR_LH_012 | Data Ingestion         | raw_to_bronze_ingestion     |                         0.15 |                      0.1  |
| EVID_CR_LH_013 | File Formats           | csv_to_parquet_conversion   |                         0.15 |                      0.1  |
| EVID_CR_LH_014 | Schema Definition      | bronze_schema_tracking      |                         0.1  |                      0.05 |
| EVID_CR_LH_015 | Pipeline Idempotency   | idempotent_overwrite        |                         0.1  |                      0.1  |
| EVID_CR_LH_016 | Medallion Architecture | bronze_layer_implementation |                         0.1  |                      0.1  |
| EVID_CR_LH_017 | Data Quality           | bronze_quality_profile      |                         0.1  |                      0.05 |

## Leitura executiva

Este notebook implementou a primeira etapa prática de ingestão do projeto `Databricks Credit Risk Lakehouse`.

Os dados brutos foram preservados e enriquecidos com metadados técnicos, permitindo rastreabilidade entre Raw e Bronze. A persistência em Parquet prepara o projeto para etapas posteriores de limpeza, padronização, integração e construção de features de risco de crédito.

## Próximo passo

O próximo notebook será:

`Notebook 04 — Bronze to Silver Data Cleaning`

Nele, as tabelas Bronze serão tratadas para remoção ou marcação de duplicidades, padronização de tipos, tratamento de nulos, validação de chaves e preparação da camada Silver.
