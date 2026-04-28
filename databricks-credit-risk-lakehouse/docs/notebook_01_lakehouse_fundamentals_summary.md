# Notebook 01 — Lakehouse Fundamentals

## Projeto

Databricks Credit Risk Lakehouse

## Data

2026-04-27

## Objetivo

Entender os fundamentos de Lakehouse, Databricks, Delta Lake e Arquitetura Medalhão aplicados a um projeto de risco de crédito.

## Conceitos estudados

- Data Lake
- Data Warehouse
- Lakehouse
- Databricks Workspace
- Notebooks
- Compute
- Catalog
- Schema
- Table
- Delta Lake
- Managed Table
- External Table
- Arquitetura Medalhão
- Raw, Bronze, Silver e Gold
- Convenções de nomenclatura

## Aplicação ao domínio de risco de crédito

O projeto propõe organizar entidades como clientes, contratos, pagamentos e eventos de crédito em uma arquitetura medalhão.

## Tabelas propostas

| layer   | table_name                     | source_entity                    | description                                                                        |
|:--------|:-------------------------------|:---------------------------------|:-----------------------------------------------------------------------------------|
| Bronze  | bronze_customers               | customers                        | Clientes ingeridos com estrutura próxima da origem.                                |
| Bronze  | bronze_contracts               | contracts                        | Contratos de crédito ingeridos a partir da origem.                                 |
| Bronze  | bronze_payments                | payments                         | Pagamentos ingeridos a partir da origem.                                           |
| Bronze  | bronze_credit_events           | credit_events                    | Eventos de crédito ingeridos a partir da origem.                                   |
| Silver  | silver_customers_clean         | customers                        | Clientes com tipos padronizados, nulos tratados e duplicidades avaliadas.          |
| Silver  | silver_contracts_clean         | contracts                        | Contratos tratados, tipados e validados.                                           |
| Silver  | silver_payments_clean          | payments                         | Pagamentos tratados com cálculo de atraso.                                         |
| Silver  | silver_customer_credit_profile | customers + contracts + payments | Perfil integrado do cliente com informações cadastrais e comportamento financeiro. |
| Gold    | gold_credit_risk_features      | silver_customer_credit_profile   | Features analíticas para análise ou modelagem de risco de crédito.                 |
| Gold    | gold_default_risk_indicators   | silver_customer_credit_profile   | Indicadores agregados de inadimplência e atraso.                                   |
| Gold    | gold_customer_risk_segments    | gold_credit_risk_features        | Segmentação analítica dos clientes por perfil de risco.                            |

## Evidências de aprendizagem geradas

| evidence_id    | topic                  | evidence_type        |   confidence_delta_suggested |   mastery_delta_suggested |
|:---------------|:-----------------------|:---------------------|-----------------------------:|--------------------------:|
| EVID_CR_LH_001 | Lakehouse Architecture | conceptual_study     |                          0.2 |                      0.05 |
| EVID_CR_LH_002 | Medallion Architecture | architecture_mapping |                          0.2 |                      0.1  |
| EVID_CR_LH_003 | Delta Lake             | conceptual_study     |                          0.1 |                      0    |
| EVID_CR_LH_004 | Managed Table          | conceptual_study     |                          0.1 |                      0    |
| EVID_CR_LH_005 | External Table         | conceptual_study     |                          0.1 |                      0    |
| EVID_CR_LH_006 | Naming Conventions     | project_standard     |                          0.1 |                      0.05 |

## Próximo passo

O próximo notebook deverá iniciar a preparação dos dados sintéticos ou públicos para ingestão na camada Raw/Bronze.
