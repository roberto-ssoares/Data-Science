# 

## Etapa-00 Estrutura Refinada do Repositório

Sugiro evoluir para:

```
Data-Science/
│
└── Modelagem-de-Series-Temporais/
    │
    ├── P01-Processo-de-Analise/
    │    ├── notebooks/
    │    │     ├── P01-analise-inicial.ipynb
    │    │     ├── P01-transformacoes.ipynb
    │    │     ├── P01-estatisticas.ipynb
    │    │     └── P01-visualizacoes.ipynb
    │    │
    │    ├── data/
    │    │     ├── raw/
    │    │     └── processed/
    │    │
    │    ├── src/
    │    │     ├── utils_timeseries.py
    │    │     └── plot_functions.py
    │    │
    │    ├── figures/
    │    │     ├── decomposicao.png
    │    │     ├── acf.png
    │    │     └── pacf.png
    │    │
    │    ├── README.md
    │    └── requirements.txt
    │
    └── P02-(futuro-projeto)/
```

Benefícios: organização de dados, código, artefatos e documentação — exatamente como empresas esperam.

---

## ETAPA 01 — Criar o notebook base do Projeto P01

O notebook seguirá exatamente a estrutura:

Notebook 01 – Processo de Análise

Títulos sugeridos:

1.01. Visão Geral

1.02. Inicialização do Ambiente

1.03. O Processo de Análise

1.04. Instalação e Carregamento de Pacotes

1.05. Carregamento e Exploração da Série Temporal

1.06. Processamento e Ajuste de Tipo de Dado

1.07. Visualização da Série Temporal

1.08. Decomposição

1.09. Extração dos Componentes

1.10. Estatísticas

1.11. Rolling Statistics

1.12. ACF e PACF

1.13. Teste Dickey-Fuller

1.14. Transformações (log, sqrt, box-cox)

1.15. Automatização

1.16. Conclusão

---

## ETAPA 02 — Adicionar dados

Se desejar usar dados fictícios de usuários ativos (como no capítulo), posso gerar um dataset:

`data/raw/usuarios_ativos.csv`

Ou podemos usar datasets reais (por exemplo, tráfego de site do Kaggle).  
Você escolhe.

---

## ETAPA 03 — Criar scripts utilitários (opcional, mas profissional)

Na pasta `src/`:

- `utils_timeseries.py`

- `plot_functions.py`

Esses scripts fornecem:

- funções para processar datas

- funções de teste de estacionariedade

- funções de plot, decomposição, ACF/PACF

Isso mostra maturidade técnica no portfólio.

---

## ETAPA 04 — Publicação no GitHub (comandos)

No VS Code ou terminal:

```powershell
git clone https://github.com/<seu-usuario>/Data-Science.git 

cd Data-Science mkdir Modelagem-de-Series-Temporais 

cd Modelagem-de-Series-Temporais mkdir P01-Processo-de-Analise
```

Depois copie os arquivos e rode:

```
git add . git commit -m "P01 - Processo de Análise de Séries Temporais" 

git push origin main
```

---

# 
