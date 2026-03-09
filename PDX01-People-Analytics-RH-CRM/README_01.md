# 📊 People Analytics — RH & CRM (DX Project)



## 🎯 Visão Geral

Este projeto aplica **People Analytics** para apoiar decisões estratégicas em **Recursos Humanos (RH)** e **Gestão de Relacionamento com Clientes (CRM)**, utilizando técnicas de **Análise de Dados** e **Ciência de Dados**.

O foco está em:

- **Redução da rotatividade de funcionários (turnover)**

- **Identificação de fatores associados à saída de colaboradores**

- **Estimativa da probabilidade de desligamento**

- **Criação de personas para clientes e funcionários**

O projeto foi estruturado seguindo boas práticas de **DX (Developer / Data Experience)**, com foco em **clareza, reprodutibilidade e impacto no negócio**.

---

## 🧠 Contexto de Negócio

A empresa fictícia **RetailX** possui aproximadamente 4.000 funcionários e uma ampla base de clientes. Atualmente enfrenta dois desafios estratégicos:

### 🔹 Recursos Humanos (RH)

- Taxa anual de rotatividade em torno de **15%**

- Custos elevados com recrutamento, treinamento e perda de produtividade

- Necessidade de entender **quais fatores influenciam a saída de funcionários**

### 🔹 CRM

- Grande volume de dados de clientes (compras, campanhas, perfil socioeconômico)

- Dificuldade em personalizar ações de marketing

- Necessidade de identificar **personas** para melhorar relacionamento e faturamento

---

## 🎯 Objetivos do Projeto

### Foco em RH

- Identificar padrões de comportamento associados à rotatividade

- Estimar a **probabilidade de desligamento** de funcionários

- Apoiar decisões estratégicas de retenção

### Foco em CRM

- Identificar **segmentos (personas)** de clientes

- Analisar características comportamentais de cada grupo

- Apoiar estratégias de marketing e relacionamento

---

## 🧭 Abordagem Analítica (CRISP-DM)

O projeto segue o framework **CRISP-DM**, com as seguintes etapas:

1. **Business Understanding**

2. **Data Understanding**

3. **Data Preparation**

4. **Modeling**
   
   - Clusterização (Personas)
   
   - Classificação (Probabilidade de Rotatividade)

5. **Evaluation**

6. **Business Impact**

Cada etapa foi documentada em notebooks independentes, garantindo clareza e organização.

---

## 🗂️ Estrutura do Repositório

```
people-analytics-dx/
│
├── data/
│   ├── raw/            # Dados brutos (não versionados)
│   ├── interim/        # Dados integrados (joins)
│   └── processed/      # Dados prontos para modelagem
│
├── notebooks/
│   ├── 01_business_understanding.ipynb
│   ├── 02_data_understanding.ipynb
│   ├── 03_data_preparation.ipynb
│   ├── 04_modeling_personas_cluster.ipynb
│   └── 05_modeling_attrition_probabilidade.ipynb
│
├── src/
│   ├── ingest_data.py
│   ├── preprocessing.py
│   ├── models.py
│   └── metrics.py
│
├── artifacts/
│   ├── preprocessor.pkl
│   ├── pca.pkl
│   ├── kmeans.pkl
│   └── model_attrition.pkl
│
├── figures/
│
├── requirements.txt
└── README.md
```

---

## 📂 Dados

Os dados utilizados neste projeto estão disponíveis publicamente no **Kaggle**.

Por boas práticas de **engenharia de dados e DX**, os dados brutos **não são versionados** no repositório.

### 🔽 Como obter os dados

1. Criar uma conta no Kaggle

2. Instalar o Kaggle CLI

3. Executar o comando abaixo:

```bash
kaggle datasets download -d 2e87aca9cfb969c5d6e89dbba2aba6d7b5a3cb769e43608a247859512197917d
```

4. Descompactar os arquivos em:

```
data/raw/
```

---

## ⚙️ Como Executar o Projeto

```bash
# criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# instalar dependências
pip install -r requirements.txt
```

Depois, execute os notebooks **na ordem numérica**.

---

## 🛠️ Tecnologias Utilizadas

- Python

- Pandas / NumPy

- Scikit-learn

- Matplotlib / Seaborn

- Jupyter Notebook

- Git / GitHub

---

## 📊 Principais Entregáveis

- Análises exploratórias orientadas ao negócio

- Segmentação de funcionários e clientes por personas

- Modelo preditivo para **probabilidade de rotatividade**

- Identificação dos principais fatores de risco

- Artefatos prontos para reuso (pipelines e modelos)

---

## 💼 Impacto para o Negócio

Os resultados do projeto permitem:

- Antecipar riscos de desligamento

- Direcionar ações de retenção

- Otimizar campanhas de marketing

- Apoiar decisões estratégicas com base em dados

---

## 🚀 Próximos Passos

- Criação de dashboards executivos

- Integração com pipelines de dados

- Monitoramento contínuo dos modelos

- Expansão para novos dados e fontes

---

## 👤 Autor

**Roberto Soares**  
Data Scientist | Data Engineer  
📍 Brasil



---

---








