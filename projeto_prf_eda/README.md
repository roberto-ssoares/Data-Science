# 🚔 PRF Data Analytics & Action Plan

> Dashboard analítico e gestor de tarefas baseado nos dados de acidentes da Polícia Rodoviária Federal (PRF) de 2023.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.55-red?logo=streamlit)
![Polars](https://img.shields.io/badge/Polars-1.38-orange)
![DuckDB](https://img.shields.io/badge/DuckDB-1.5-yellow?logo=duckdb)
![Plotly](https://img.shields.io/badge/Plotly-6.6-purple?logo=plotly)

---

## 📌 Sobre o Projeto

Este projeto aplica a metodologia **CRISP-DM** para analisar os dados de acidentes rodoviários da PRF de 2023, com dois objetivos principais:

1. **Analytics Dashboard** — Exploração dos dados com visualizações interativas para identificar padrões, causas e janelas críticas de acidentes.
2. **Gestor de Tarefas** — Transformar insights em ações concretas, com CRUD de tarefas priorizadas por status e prioridade.

### Objetivos de Aprendizado

- Aprofundamento em **Polars** e **DuckDB** para processamento de dados de alta performance
- Construção de aplicações analíticas com **Streamlit**
- Boas práticas de **storytelling com dados**
- Pipeline de dados estruturado (ingestão → processamento → visualização)

---

## 🗂️ Estrutura do Projeto

```
projeto_prf_eda/
├── app/
│   ├── main.py                  # Página principal (roteamento)
│   └── pages/
│       ├── 01_analysis.py       # Analytics Dashboard
│       └── 02_tasks.py          # Gestor de Tarefas
├── src/
│   ├── pipeline/
│   │   └── ingestion.py         # Pipeline de ingestão e limpeza
│   └── database/
│       └── ...                  # Camada de banco de dados (SQLite)
├── data/
│   ├── 00-raw/                  # Dados brutos (não versionados)
│   ├── 01-processed/            # Dados processados .parquet (não versionados)
│   └── 02-database/             # SQLite (não versionado)
├── notebooks/                   # Exploração e prototipagem
├── requirements.txt
└── README.md
```

---

## 📊 Features do Dashboard

| Seção                                     | Descrição                                                                  |
| ----------------------------------------- | -------------------------------------------------------------------------- |
| **KPIs**                                  | Total de acidentes, estados atendidos, causa principal, taxa de letalidade |
| **Top 10 Causas**                         | Ranking das principais causas de acidentes                                 |
| **Acidentes por Dia da Semana**           | Distribuição por dia em gráfico de rosca                                   |
| **Ocorrências ao Longo do Tempo**         | Evolução mensal por estado (UF)                                            |
| **Mapa Geográfico**                       | Top 500 ocorrências plotadas no mapa                                       |
| **⚠️ Severidade por Tipo de Acidente**    | Barras empilhadas: ilesos vs. feridos vs. mortos                           |
| **🕐 Heatmap Temporal**                   | Dia da semana × Hora do dia — janelas críticas                             |
| **🌧️ Condição Climática vs. Letalidade** | Taxa de mortalidade por condição meteorológica                             |

---

## 🚀 Como Rodar Localmente

### Pré-requisitos

- Python 3.10+
- Os dados brutos da PRF 2023 (ver abaixo)

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/projeto_prf_eda.git
cd projeto_prf_eda
```

### 2. Crie um ambiente virtual e instale as dependências

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3. Obtenha os dados da PRF

Baixe o arquivo de acidentes de 2023 diretamente do portal oficial da PRF:

- 🔗 [Dados Abertos PRF](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf)
- Salve em `data/00-raw/Dados_PRF_2023_utf8.csv`

### 4. Execute o pipeline de ingestão

```bash
python src/pipeline/ingestion.py
```

### 5. Inicie o aplicativo

```bash
streamlit run app/main.py
```

---

## 🛠️ Stack Técnica

| Tecnologia    | Uso                                                                    |
| ------------- | ---------------------------------------------------------------------- |
| **Polars**    | Processamento de dados no pipeline (lazy evaluation, alta performance) |
| **DuckDB**    | Query engine para leitura do Parquet no dashboard                      |
| **Streamlit** | Framework da aplicação web interativa                                  |
| **Plotly**    | Visualizações interativas (bar, line, pie, heatmap, imshow)            |
| **Pandas**    | Compatibilidade e transformações intermediárias                        |
| **SQLite**    | Persistência das tarefas do Gestor                                     |

---

## ☁️ Deploy

Este projeto é hospedável gratuitamente no **Streamlit Community Cloud**:

1. Faça fork/push deste repositório para o seu GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. 
4. Conecte seu repositório e aponte para `app/main.py`
5. Configure os dados (via upload ou fonte externa)

> **Nota:** Os dados da PRF não são incluídos neste repositório. Siga as instruções de ingestão acima.

---

## 📄 Licença

Este projeto é de uso educacional e para portfólio. Os dados são públicos e disponibilizados pela PRF.

---

<p align="center">Feito com ❤️ usando Python + Streamlit</p>
