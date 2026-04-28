# Notebook 02 — Data Source and Raw Layer Preparation

## Projeto

Databricks Credit Risk Lakehouse

## Data

2026-04-28

## Objetivo

Criar a base inicial de dados sintéticos para o projeto de risco de crédito e preparar os arquivos da camada Raw.

## Entidades geradas

| entity        |   rows |   columns |
|:--------------|-------:|----------:|
| customers     |    501 |        11 |
| contracts     |    622 |        10 |
| payments      |  12919 |        11 |
| credit_events |    580 |         8 |

## Manifesto da camada Raw

| entity        | file_name         | layer   | file_format   |   rows |   columns | source_systems    |
|:--------------|:------------------|:--------|:--------------|-------:|----------:|:------------------|
| customers     | customers.csv     | raw     | csv           |    501 |        11 | crm_core          |
| contracts     | contracts.csv     | raw     | csv           |    622 |        10 | loan_management   |
| payments      | payments.csv      | raw     | csv           |  12919 |        11 | payment_gateway   |
| credit_events | credit_events.csv | raw     | csv           |    580 |         8 | credit_operations |

## Qualidade inicial por entidade

| entity        |   rows |   columns |   duplicated_rows |   total_null_cells |   total_blank_cells |
|:--------------|-------:|----------:|------------------:|-------------------:|--------------------:|
| customers     |    501 |        11 |                 1 |                 15 |                   0 |
| contracts     |    622 |        10 |                 1 |                  0 |                   6 |
| payments      |  12919 |        11 |                 1 |                 65 |                 313 |
| credit_events |    580 |         8 |                 0 |                  6 |                   0 |

## Evidências de aprendizagem geradas

| evidence_id    | topic              | evidence_type         |   confidence_delta_suggested |   mastery_delta_suggested |
|:---------------|:-------------------|:----------------------|-----------------------------:|--------------------------:|
| EVID_CR_LH_007 | Data Ingestion     | raw_layer_preparation |                         0.15 |                      0.05 |
| EVID_CR_LH_008 | File Formats       | csv_generation        |                         0.1  |                      0.05 |
| EVID_CR_LH_009 | Schema Definition  | schema_documentation  |                         0.15 |                      0.05 |
| EVID_CR_LH_010 | Data Quality       | raw_quality_profile   |                         0.1  |                      0.05 |
| EVID_CR_LH_011 | Naming Conventions | raw_file_naming       |                         0.05 |                      0.05 |

## Leitura executiva

Este notebook criou a primeira fonte de dados do projeto `Databricks Credit Risk Lakehouse`.

Foram gerados arquivos brutos para clientes, contratos, pagamentos e eventos de crédito. Os dados incluem pequenas imperfeições controladas, como valores ausentes, blanks e duplicidades, para permitir a prática realista de ingestão, validação e tratamento nas próximas camadas.

## Próximo passo

O próximo notebook será:

`Notebook 03 — Raw to Bronze Ingestion`

Nele, os arquivos CSV da camada Raw serão lidos, enriquecidos com metadados técnicos e persistidos na camada Bronze em formato analítico.
