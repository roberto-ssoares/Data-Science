# 🧠 Credit Risk with Geometric Machine Learning

## 📌 Visão Geral

Este projeto explora uma abordagem inovadora para modelagem de risco de crédito utilizando **Geometric Machine Learning**.  

A proposta central é incorporar **estrutura relacional entre clientes** através de um grafo de similaridade e extrair **features geométricas baseadas em curvatura de Ricci**, avaliando seu impacto na capacidade preditiva de modelos tradicionais.  

---  

## 🎯 Objetivo

Investigar se **features geométricas derivadas de grafos** agregam valor ao problema de previsão de inadimplência em comparação com modelos baseados apenas em dados tabulares.  

---  

## 🚀 Destaques do Projeto

- ✔ Engenharia de recursos baseada em grafos aplicada ao risco de crédito

- ✔ Curvatura de Ollivier-Ricci para análise estrutural

- ✔ Grafo de similaridade KNN entre clientes

- ✔ Avaliação comparativa: recursos tabulares versus geométricos

- ✔ Pipeline completo (dados brutos → modelagem)



---

## 🧱 Arquitetura do Projeto



data/  
├── 00-raw/  
├── 01-bronze/  
├── 02-interim/  
├── 03-feature-store/  
├── 04-model-output/  
├── 90-profiling/  
└── 99-audit/

notebooks/  
├── 00_raw_to_bronze_duckdb.ipynb  
├── 01_application_train_knn_ricci.ipynb  
└── 02_baseline_vs_geometric_features.ipynb

---  

## ⚙️ Pipeline

### 🔹 Etapa 00 — Ingestão

- Conversão de CSV → Parquet com DuckDB  
- Auditoria de ingestão  
- Schema registry  
- Profiling de dados  

### 🔹 Etapa 01 — Graph Construction + Ricci Curvature

- Construção de grafo KNN entre clientes  
- Cálculo de Ollivier-Ricci Curvature  
- Feature engineering geométrico  

### 🔹 Etapa 02 — Modelagem

- Baseline tabular  
- Tabular + features geométricas  
- Comparação de desempenho  

---  

## 🧠 Metodologia

### 1. Construção do Grafo

- KNN sobre variáveis financeiras e cadastrais  
- Distância Euclidiana normalizada  
- Grafo não-direcionado  

### 2. Curvatura de Ricci

- Algoritmo: Ollivier-Ricci  
- Interpretação:  
  - curvatura negativa → regiões de transição  
  - curvatura positiva → regiões coesas  

### 3. Features Geométricas

- `geom_curvature_mean`  
- `geom_curvature_std`  
- `geom_curvature_min`  
- `geom_curvature_max`  
- `geom_curvature_neg_ratio`  
- `geom_degree`  

---  

## 📊 Resultados

### 🔹 Logistic Regression

✔ Melhora consistente em todas as métricas:  

- ROC-AUC ↑  
- KS ↑  
- Average Precision ↑  

### 🔹 Random Forest / LightGBM

- Resultados mistos  
- Indicam possível redundância com estruturas não-lineares já capturadas  

---  

## 🔍 Insights Principais

- Features geométricas aparecem entre as mais importantes do modelo  
- A variabilidade da curvatura (`geom_curvature_std`) é um forte indicador  
- A estrutura relacional entre clientes contém informação relevante  

---  

## 🧠 Conclusão

Os resultados indicam que:  

> A geometria do grafo captura padrões estruturais que não estão explicitamente representados no espaço tabular tradicional.  

Mesmo com ganhos modestos, a abordagem demonstra:  

- viabilidade técnica  
- valor analítico  
- potencial para evolução  

---  

## 🚀 Próximos Passos

- Ajuste de KNN (k, métrica)  
- Integração com outras tabelas (bureau, previous_application)  
- Construção de Knowledge Graph  
- Modelos híbridos tabular + grafo  

---  

## 🛠️ Tecnologias

- Python  
- Polars  
- DuckDB  
- NetworkX  
- GraphRicciCurvature  
- Scikit-learn  
- LightGBM  

---  

## 👤 Autor

Roberto Soares    
Data Scientist | Data Engineer    
[LinkedIn](https://www.linkedin.com/in/roberto-dos-santos-soares)  

---  

## ⭐ Destaque

Este projeto explora a interseção entre:  

- Machine Learning  
- Teoria dos Grafos  
- Geometria Discreta  

Aplicada a um problema real de negócio: **risco de crédito**.
