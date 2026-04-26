# Metodologia do Fraud Risk Score

Este documento descreve a metodologia usada no Notebook 06 para composição do score final de risco antifraude.

## Componentes do Score

| componente                                |   peso | peso_percentual   |
|:------------------------------------------|-------:|:------------------|
| rule_score                                |  0.45  | 45.0%             |
| account_graph_entity_graph_risk_score     |  0.2   | 20.0%             |
| device_graph_entity_graph_risk_score      |  0.125 | 12.5%             |
| beneficiary_graph_entity_graph_risk_score |  0.125 | 12.5%             |
| ip_graph_entity_graph_risk_score          |  0.05  | 5.0%              |
| max_community_risk_score                  |  0.05  | 5.0%              |

## Fórmula Conceitual

```text
fraud_risk_score =
    0.45  * rule_score
  + 0.20  * account_graph_risk_score
  + 0.125 * device_graph_risk_score
  + 0.125 * beneficiary_graph_risk_score
  + 0.05  * ip_graph_risk_score
  + 0.05  * max_community_risk_score
```

## Faixas de Risco

| Faixa | Critério |
|---|---|
| crítico | score >= 80 |
| alto | 60 <= score < 80 |
| médio | 35 <= score < 60 |
| baixo | score < 35 |

## Observação

O score foi criado para fins educacionais, analíticos e de portfólio. Ele não representa um modelo produtivo de decisão antifraude.
