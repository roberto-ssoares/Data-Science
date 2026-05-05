# Spotify Global Music Intelligence

Projeto de Análise Exploratória de Dados aplicado ao **Spotify Global Music Dataset (2009–2025)**.

## Objetivo

Construir uma EDA profissional para investigar tendências musicais, popularidade de artistas, evolução temporal de faixas e preparação analítica para futuros modelos preditivos.

## Contexto

Este projeto simula uma entrega real de consultoria em dados para uma empresa fictícia de inteligência musical, com foco em:

- entendimento de negócio;
- entendimento dos dados;
- qualidade dos dados;
- análise exploratória;
- geração de insights;
- preparação para modelagem;
- estruturação para portfólio.

## Estrutura do projeto

```text
spotify-global-music-intelligence/
├── data/
│   ├── 00_raw/
│   ├── 01_bronze/
│   ├── 02_silver/
│   └── 03_gold/
├── notebooks/
├── src/
│   └── spotify_intelligence/
├── reports/
│   ├── figures/
│   └── html/
├── docs/
├── scripts/
├── tests/
├── README.md
└── pyproject.toml
```

Notebooks planejados
Notebook    Descrição
00_business_understanding.ipynb    Contexto de negócio, problema, hipóteses e critérios de sucesso
01_data_understanding.ipynb    Leitura, estrutura e diagnóstico inicial dos datasets
02_data_quality_and_preparation.ipynb    Qualidade, padronização, tratamento e camada Silver
03_exploratory_data_analysis.ipynb    EDA univariada, bivariada, temporal e multivariada
04_executive_insights_and_next_steps.ipynb    Insights executivos, recomendações e próximos passos
Como executar
uv sync
.venv\Scripts\Activate.ps1
jupyter lab
Autor

Roberto dos Santos Soares
