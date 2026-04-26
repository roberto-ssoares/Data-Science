# Fraud Risk Score Explainability — Resumo Executivo

Este documento consolida os principais resultados do Notebook 06.

## Objetivo

Combinar regras antifraude explicáveis com features estruturais de grafo para criar um score final de risco transacional.

## Síntese Executiva

| indicador                                     |         valor | interpretacao                                                      |
|:----------------------------------------------|--------------:|:-------------------------------------------------------------------|
| Total de transações avaliadas                 | 80000         | Quantidade total de eventos avaliados pelo score final.            |
| Total de alertas finais                       | 79254         | Transações priorizadas pela combinação de regras e grafo.          |
| Taxa de alertas finais                        |     0.990675  | Proporção da base direcionada para investigação.                   |
| Score final médio                             |    51.0871    | Risco médio após combinação de sinais transacionais e relacionais. |
| Alertas críticos finais                       |  1582         | Transações com score final igual ou superior a 80.                 |
| Taxa sintética de fraude entre alertas finais |     0.0883236 | Validação exploratória contra o label sintético.                   |
| Contas com alertas finais                     |  5999         | Quantidade de contas distintas priorizadas.                        |
| Dispositivos com alertas finais               |  4500         | Quantidade de dispositivos distintos envolvidos.                   |
| Beneficiários com alertas finais              |  3500         | Quantidade de beneficiários distintos envolvidos.                  |
| IPs com alertas finais                        |  3000         | Quantidade de IPs distintos envolvidos.                            |

## Distribuição por Faixa de Risco Final

| final_risk_band   |   qtd_transacoes |   taxa_alerta |   taxa_fraude_sintetica |   score_medio |   score_min |   score_max |   valor_medio |
|:------------------|-----------------:|--------------:|------------------------:|--------------:|------------:|------------:|--------------:|
| baixo             |              746 |             0 |               0         |       33.2689 |       26.71 |       34.99 |       345.552 |
| medio             |            67934 |             1 |               0.0203433 |       48.3247 |       35    |       59.99 |       436.74  |
| alto              |             9738 |             1 |               0.417848  |       66.1264 |       60    |       79.99 |      3464.98  |
| critico           |             1582 |             1 |               0.97914   |       85.5382 |       80    |       91.84 |     10958.6   |

## Comparação entre Score de Regras e Score Final

| indicador                                 |        valor |
|:------------------------------------------|-------------:|
| Score médio de regras                     |   44.6321    |
| Score final médio                         |   51.0871    |
| Taxa de alerta por regras                 |    0.999962  |
| Taxa de alerta final                      |    0.990675  |
| Fraude sintética entre alertas por regras |    0.0875033 |
| Fraude sintética entre alertas finais     |    0.0883236 |
| Transações críticas por regras            | 4627         |
| Transações críticas pelo score final      | 1582         |

## Score por Cenário Sintético

| fraud_scenario           |   qtd_transacoes |   taxa_fraude_sintetica |   rule_score_medio |   fraud_risk_score_medio |   fraud_risk_score_p95 |   taxa_alerta_final |   qtd_criticos |
|:-------------------------|-----------------:|------------------------:|-------------------:|-------------------------:|-----------------------:|--------------------:|---------------:|
| coordinated_network      |             1000 |                       1 |            94.79   |                  86.4247 |                89.76   |            1        |            912 |
| new_account_high_value   |             1000 |                       1 |            91.779  |                  75.4559 |                84.417  |            1        |            243 |
| burst_transactions       |             1200 |                       1 |            83.0525 |                  72.885  |                83.803  |            1        |            242 |
| bridge_account           |              800 |                       1 |            72.9125 |                  69.4219 |                85.063  |            1        |            106 |
| beneficiary_concentrator |             1400 |                       1 |            61.3064 |                  63.2848 |                76.2415 |            1        |             33 |
| shared_device_ring       |             1600 |                       1 |            54.4744 |                  62.307  |                73.3545 |            1        |             13 |
| normal                   |            73000 |                       0 |            41.8222 |                  49.2301 |                61.56   |            0.989781 |             33 |

## Top Contas por Alertas Finais

| conta_origem_id   |   qtd_alertas |   score_final_medio |   score_final_max |   valor_total_alertado |   qtd_beneficiarios |   qtd_devices |   qtd_ips |   taxa_fraude_sintetica |   max_entity_graph_risk_score |   max_community_risk_score |
|:------------------|--------------:|--------------------:|------------------:|-----------------------:|--------------------:|--------------:|----------:|------------------------:|------------------------------:|---------------------------:|
| CTA_000875        |            75 |             66.908  |             91.84 |               385964   |                  75 |            74 |        73 |                0.84     |                         95.13 |                      82.01 |
| CTA_003281        |            55 |             70.7345 |             91.72 |                92931.9 |                  54 |            55 |        55 |                0.690909 |                         96.28 |                      82.01 |
| CTA_003015        |            19 |             60.8421 |             91.53 |               124621   |                  19 |            19 |        19 |                0.263158 |                         95.74 |                      82.01 |
| CTA_005360        |            79 |             67.6987 |             91.47 |               409792   |                  78 |            77 |        78 |                0.835443 |                         94.75 |                      82.01 |
| CTA_003572        |            39 |             66.6992 |             90.58 |                60862.8 |                  39 |            39 |        39 |                0.666667 |                         90.54 |                      82.01 |
| CTA_002863        |            33 |             67.1615 |             90.34 |               115095   |                  29 |            27 |        26 |                0.424242 |                         89.28 |                      82.01 |
| CTA_002741        |            32 |             70.3044 |             90.31 |               193349   |                  25 |            22 |        24 |                0.53125  |                         89.43 |                      82.01 |
| CTA_004244        |            32 |             72.8588 |             90.18 |               179777   |                  23 |            22 |        24 |                0.5625   |                         88.55 |                      82.01 |
| CTA_000323        |            34 |             73.0962 |             90.12 |               157852   |                  28 |            25 |        25 |                0.588235 |                         87.37 |                      82.01 |
| CTA_003481        |            32 |             69.3109 |             90.12 |               149352   |                  27 |            24 |        25 |                0.46875  |                         96.28 |                      82.01 |

## Top Dispositivos por Alertas Finais

| device_id   |   qtd_alertas |   contas_distintas |   score_final_medio |   score_final_max |   valor_total_alertado |   taxa_fraude_sintetica |
|:------------|--------------:|-------------------:|--------------------:|------------------:|-----------------------:|------------------------:|
| DEV_000856  |           150 |                147 |             63.3721 |             84.41 |                74310.8 |                0.893333 |
| DEV_004007  |           145 |                143 |             62.1557 |             89.04 |                60139.9 |                0.924138 |
| DEV_003932  |           100 |                 99 |             62.8082 |             86.35 |                46842.9 |                0.81     |
| DEV_002418  |            97 |                 96 |             62.5267 |             75.76 |                31917.1 |                0.835052 |
| DEV_002048  |            95 |                 91 |             63.3573 |             89.1  |                55695.3 |                0.747368 |
| DEV_000102  |            89 |                 88 |             62.6945 |             79.31 |                40333.1 |                0.797753 |
| DEV_002459  |            88 |                 88 |             62.3983 |             78.86 |                41954.5 |                0.772727 |
| DEV_001272  |            87 |                 86 |             61.7605 |             88.46 |                82371.5 |                0.827586 |
| DEV_003863  |            86 |                 86 |             62.631  |             79.99 |                34586.1 |                0.837209 |
| DEV_000361  |            83 |                 83 |             62.954  |             91.84 |                55483   |                0.710843 |

## Top Beneficiários por Alertas Finais

| beneficiario_id   |   qtd_alertas |   contas_origem_distintas |   score_final_medio |   score_final_max |   valor_total_alertado |   taxa_fraude_sintetica |
|:------------------|--------------:|--------------------------:|--------------------:|------------------:|-----------------------:|------------------------:|
| BEN_002999        |           108 |                       106 |             64.6209 |             87.87 |               180489   |                0.787037 |
| BEN_003123        |           108 |                       105 |             62.5851 |             81.85 |               140199   |                0.731481 |
| BEN_003031        |           103 |                       102 |             63.5499 |             85.27 |               185370   |                0.805825 |
| BEN_000268        |           103 |                       102 |             62.2286 |             81.75 |               136142   |                0.84466  |
| BEN_001264        |            97 |                        97 |             61.5532 |             78.94 |               127915   |                0.721649 |
| BEN_001791        |            95 |                        95 |             62.4224 |             84.45 |               126122   |                0.747368 |
| BEN_000352        |            94 |                        94 |             62.4589 |             80.53 |               140127   |                0.851064 |
| BEN_002787        |            94 |                        93 |             63.6515 |             83.14 |               152518   |                0.755319 |
| BEN_000998        |            93 |                        93 |             61.0788 |             80.45 |                95672.9 |                0.784946 |
| BEN_002457        |            93 |                        93 |             60.9528 |             79.93 |               105149   |                0.72043  |

## Top IPs por Alertas Finais

| ip_id     |   qtd_alertas |   contas_distintas |   score_final_medio |   score_final_max |   valor_total_alertado |   taxa_fraude_sintetica |
|:----------|--------------:|-------------------:|--------------------:|------------------:|-----------------------:|------------------------:|
| IP_002369 |           134 |                 92 |             77.503  |             90.02 |       934405           |                0.701493 |
| IP_001997 |           145 |                 91 |             79.1777 |             90.31 |            1.03316e+06 |                0.765517 |
| IP_001101 |           140 |                 79 |             80.6794 |             90.12 |            1.04821e+06 |                0.814286 |
| IP_001109 |           144 |                 78 |             81.4255 |             90.18 |            1.10872e+06 |                0.847222 |
| IP_000564 |           128 |                 75 |             80.3556 |             90.07 |       946469           |                0.796875 |
| IP_002713 |           124 |                 74 |             79.3744 |             90.34 |       920034           |                0.766129 |
| IP_000568 |           120 |                 71 |             81.5755 |             90.25 |       963521           |                0.841667 |
| IP_002423 |           117 |                 70 |             80.703  |             89.92 |       798075           |                0.846154 |
| IP_001280 |           115 |                 69 |             82.5914 |             89.89 |            1.00305e+06 |                0.852174 |
| IP_000480 |           101 |                 61 |             81.0048 |             90.09 |       839087           |                0.841584 |

## Principais Achados

| achado                                                                | evidencia                                                                                          | interpretacao                                                                                                |
|:----------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|
| O score final combina risco transacional e risco relacional           | O score utiliza rule_score, risco de conta, dispositivo, beneficiário, IP e comunidade.            | A priorização deixa de depender apenas da transação isolada e passa a considerar o contexto da rede.         |
| Entidades estruturalmente suspeitas elevam a prioridade investigativa | Transações conectadas a entidades com alto entity_graph_risk_score recebem reforço no score final. | Dispositivos compartilhados, beneficiários concentradores e IPs recorrentes tornam-se sinais complementares. |
| Comunidades de grafo agregam contexto coletivo                        | O max_community_risk_score incorpora o risco das comunidades associadas às entidades da transação. | A análise passa a observar grupos conectados, não apenas eventos pontuais.                                   |
| A explicabilidade melhora a utilidade operacional                     | Cada transação recebe uma justificativa textual com regras acionadas e sinais de grafo.            | A saída pode apoiar triagem, revisão manual, comunicação executiva e documentação do raciocínio.             |
| A abordagem é adequada para portfólio sênior                          | O projeto integra CRISP-DM+, regras, grafos, score e explicabilidade em uma trilha reprodutível.   | Demonstra capacidade de transformar problema de negócio em solução analítica estruturada.                    |

## Valor Analítico

- Integra regras transacionais e contexto relacional de grafo.
- Prioriza transações com maior risco final.
- Explica os motivos do alerta em linguagem interpretável.
- Permite investigação por transação, conta, dispositivo, beneficiário, IP e comunidade.
- Prepara o projeto para conclusão executiva e empacotamento de portfólio.

## Observação

Os resultados são derivados de dados sintéticos criados exclusivamente para fins educacionais, analíticos e de portfólio.
