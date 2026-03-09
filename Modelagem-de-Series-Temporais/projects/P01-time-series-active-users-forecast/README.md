# Previsão de Usuários Ativos em Website com Séries Temporais

## 📌 Contexto

A previsão de usuários ativos é um problema recorrente em produtos digitais,
plataformas SaaS e e-commerces, impactando diretamente decisões de
infraestrutura, marketing, retenção e planejamento estratégico.

Este projeto apresenta uma solução completa de **modelagem de séries temporais**,
partindo da análise exploratória até a comparação entre diferentes modelos
preditivos.

---

## 🎯 Objetivo

Prever a quantidade de usuários ativos ao longo do tempo a partir de dados
históricos, identificando padrões de tendência, sazonalidade e ruído.

---

## 🧠 Abordagem

O projeto foi desenvolvido seguindo uma abordagem estruturada:

- Entendimento do problema e da série temporal
- Preparação e regularização dos dados
- Análise exploratória e estatística
- Avaliação da estacionariedade (ADF, ACF, PACF)
- Modelagem preditiva:
  - ARIMA (baseline)
  - ARIMA otimizado (grid search + AIC)
  - SARIMA (incorporação de sazonalidade)
  - ETS (Holt-Winters)
- Comparação quantitativa e visual entre modelos
- Extração de insights de negócio

---

## 📊 Modelos e Resultados

| Modelo               | MAE       | RMSE      |
| -------------------- | --------- | --------- |
| ARIMA Otimizado      | 38.70     | 46.05     |
| **SARIMA Otimizado** | **15.98** | **20.82** |
| ETS                  | 16.85     | 22.09     |

👉 O **SARIMA Otimizado** apresentou o melhor equilíbrio entre desempenho,
estabilidade e interpretação.

---

## 💡 Insights de Negócio

- A série apresenta sazonalidade recorrente
- Previsões permitem antecipar picos e quedas de engajamento
- Apoiam decisões de infraestrutura e campanhas
- Podem ser usadas para monitoramento e detecção de anomalias

---

## ⚠️ Limitações

- Uso exclusivo da própria série (sem variáveis externas)
- Modelos clássicos podem ter limitações em cenários muito voláteis

---

## 🚀 Próximos Passos

- Inclusão de variáveis exógenas (ARIMAX / SARIMAX)
- Modelos de Machine Learning
- Automatização e deploy do pipeline

---

## 🛠️ Tecnologias

Python, Pandas, NumPy, Statsmodels, Scikit-learn, Matplotlib

📎 Notebook completo disponível em HTML neste repositório.


