# Ontology v0.1 — Databricks Learning Knowledge Graph

## Projeto

Databricks Certification Learning Knowledge Graph

## Certificação alvo

Databricks Certified Data Engineer Associate

## Data de geração

2026-04-27

## Visão geral

Este documento descreve a primeira versão materializada da ontologia do projeto.

## Quantidade de nós por tipo

| node_label    |   total_nodes |
|:--------------|--------------:|
| Topic         |            46 |
| Subtopic      |            20 |
| Skill         |             6 |
| ExamDomain    |             5 |
| Notebook      |             5 |
| Resource      |             4 |
| Lab           |             4 |
| Certification |             1 |
| StudySession  |             1 |
| Snapshot      |             1 |

## Quantidade de relacionamentos por tipo

| relationship       |   total_edges |
|:-------------------|--------------:|
| CAPTURES_STATUS_OF |            46 |
| COVERS             |            46 |
| HAS_SUBTOPIC       |            20 |
| PREREQUISITE_FOR   |            15 |
| SUPPORTED_BY       |            11 |
| TEACHES            |            10 |
| PRACTICES          |             8 |
| IMPLEMENTS         |             7 |
| HAS_DOMAIN         |             5 |
| STUDIED            |             4 |

## Arquivos gerados

| filename                       |   rows |   columns |
|:-------------------------------|-------:|----------:|
| certifications.csv             |      1 |        10 |
| exam_domains.csv               |      5 |         5 |
| topics.csv                     |     46 |        12 |
| subtopics.csv                  |     20 |         4 |
| resources.csv                  |      4 |         6 |
| notebooks.csv                  |      5 |         5 |
| labs.csv                       |      4 |         4 |
| skills.csv                     |      6 |         5 |
| study_sessions.csv             |      1 |         8 |
| snapshots.csv                  |      1 |         9 |
| topic_progress_snapshot.csv    |     46 |        10 |
| nodes_all.csv                  |     93 |         7 |
| edges_all.csv                  |    172 |         8 |
| relationship_types_summary.csv |     10 |         2 |
| node_labels_summary.csv        |     10 |         2 |

## Observação

Esta é a versão inicial da ontologia como dados.  
Nos próximos notebooks, essa estrutura poderá ser visualizada como grafo, carregada no Neo4j e enriquecida com novos snapshots de progresso.
