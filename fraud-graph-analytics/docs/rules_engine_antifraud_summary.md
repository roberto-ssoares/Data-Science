# Rules Engine Antifraud — Resumo Executivo

Este documento consolida os principais resultados do Notebook 03.

## Objetivo

Construir um motor de regras antifraude explicável para priorização de transações suspeitas em uma base sintética.

## Síntese Executiva

| indicador                              |         valor | interpretacao                                             |
|:---------------------------------------|--------------:|:----------------------------------------------------------|
| Total de transações analisadas         | 80000         | Base transacional sintética usada pelo motor de regras.   |
| Total de alertas gerados               | 79997         | Transações com score mínimo para investigação.            |
| Taxa de alertas                        |     0.999962  | Proporção de transações priorizadas pelo motor de regras. |
| Score médio dos alertas                |    44.6333    | Pontuação média entre transações alertadas.               |
| Alertas críticos                       |  4627         | Transações com score igual ou superior a 70.              |
| Taxa sintética de fraude entre alertas |     0.0875033 | Validação exploratória contra o label sintético.          |
| Contas com alertas                     |  6000         | Quantidade de contas distintas sinalizadas.               |
| Dispositivos com alertas               |  4500         | Quantidade de dispositivos envolvidos em alertas.         |
| Beneficiários com alertas              |  3500         | Quantidade de beneficiários envolvidos em alertas.        |

## Avaliação por Regra

| regra                                  |   qtd_transacoes_acionadas |   qtd_fraudes_sinteticas_acionadas |   taxa_fraude_entre_acionadas |   cobertura_fraude_sintetica |   valor_medio_acionadas |
|:---------------------------------------|---------------------------:|-----------------------------------:|------------------------------:|-----------------------------:|------------------------:|
| R008_muitos_beneficiarios_no_dia       |                       1200 |                               1200 |                     1         |                     0.171429 |                 1875.91 |
| R007_rajada_transacional_horaria       |                       1183 |                               1183 |                     1         |                     0.169    |                 1871.81 |
| R003_conta_nova_alto_valor             |                       1944 |                               1506 |                     0.774691  |                     0.215143 |                15944.2  |
| R001_alto_valor_transacional           |                       4000 |                               3012 |                     0.753     |                     0.430286 |                11708.3  |
| R002_valor_acima_limite_diario         |                       4848 |                               2679 |                     0.552599  |                     0.382714 |                 8822.94 |
| R010_canal_digital_alto_valor          |                       7120 |                               3651 |                     0.512781  |                     0.521571 |                 6825.98 |
| R006_rede_ou_device_alto_risco         |                       9517 |                               2990 |                     0.314175  |                     0.427143 |                 1685.05 |
| R005_beneficiario_concentrador         |                      31469 |                               4083 |                     0.129747  |                     0.583286 |                 1179.11 |
| R004_dispositivo_compartilhado         |                      79996 |                               7000 |                     0.0875044 |                     1        |                 1012.58 |
| R009_ip_compartilhado_multiplas_contas |                      80000 |                               7000 |                     0.0875    |                     1        |                 1012.57 |

## Avaliação por Faixa de Risco

| risk_band   |   qtd_transacoes |   qtd_alertas |   taxa_fraude_sintetica |   valor_medio |   qtd_cenarios |   media_regras_acionadas |
|:------------|-----------------:|--------------:|------------------------:|--------------:|---------------:|-------------------------:|
| baixo       |                3 |             0 |              0          |       496.477 |              1 |                  1       |
| medio       |            40494 |         40494 |              0.00118536 |       397.986 |              3 |                  2.03835 |
| alto        |            34876 |         34876 |              0.0941335  |       581.667 |              7 |                  3.185   |
| critico     |             4627 |          4627 |              0.792954   |      9639.5   |              7 |                  5.97644 |

## Cenários Sintéticos e Score Médio

| fraud_scenario           |   qtd_transacoes |   taxa_alerta |   score_medio |   score_p95 |   media_regras_acionadas |   taxa_fraude_sintetica |
|:-------------------------|-----------------:|--------------:|--------------:|------------:|-------------------------:|------------------------:|
| coordinated_network      |             1000 |      1        |       94.79   |         100 |                  6.654   |                       1 |
| new_account_high_value   |             1000 |      1        |       91.779  |         100 |                  6.228   |                       1 |
| burst_transactions       |             1200 |      1        |       83.0525 |         100 |                  5.42417 |                       1 |
| bridge_account           |              800 |      1        |       72.9125 |         100 |                  5.05875 |                       1 |
| beneficiary_concentrator |             1400 |      1        |       61.3064 |          87 |                  3.81071 |                       1 |
| shared_device_ring       |             1600 |      1        |       54.4744 |          66 |                  3.45688 |                       1 |
| normal                   |            73000 |      0.999959 |       41.8222 |          64 |                  2.56127 |                       0 |

## Top Contas Alertadas

| conta_origem_id   |   qtd_alertas |   score_medio |   score_max |   valor_total_alertado |   qtd_beneficiarios |   qtd_devices |   qtd_ips |   taxa_fraude_sintetica |
|:------------------|--------------:|--------------:|------------:|-----------------------:|--------------------:|--------------:|----------:|------------------------:|
| CTA_002509        |            86 |       82.2791 |         100 |               525957   |                  85 |            85 |        84 |                0.895349 |
| CTA_000664        |            85 |       69.0353 |         100 |               590316   |                  84 |            84 |        84 |                0.929412 |
| CTA_005335        |            81 |       63.8765 |         100 |               457827   |                  81 |            80 |        79 |                0.802469 |
| CTA_001134        |            79 |       80.4557 |         100 |               433077   |                  78 |            79 |        79 |                0.835443 |
| CTA_005360        |            79 |       70.6203 |         100 |               409792   |                  78 |            77 |        78 |                0.835443 |
| CTA_002395        |            78 |       64.4615 |         100 |               471439   |                  77 |            77 |        77 |                0.846154 |
| CTA_001976        |            76 |       70.3421 |         100 |               411664   |                  75 |            76 |        76 |                0.868421 |
| CTA_000875        |            75 |       67.96   |         100 |               385964   |                  75 |            74 |        73 |                0.84     |
| CTA_004448        |            66 |       67.8333 |         100 |               379934   |                  66 |            66 |        66 |                0.878788 |
| CTA_003281        |            55 |       74.2909 |         100 |                92931.9 |                  54 |            55 |        55 |                0.690909 |

## Top Dispositivos Alertados

| device_id   |   qtd_alertas |   contas_distintas |   score_medio |   score_max |   valor_total_alertado |   taxa_fraude_sintetica |
|:------------|--------------:|-------------------:|--------------:|------------:|-----------------------:|------------------------:|
| DEV_000856  |           150 |                147 |       54.4733 |          96 |                74310.8 |                0.893333 |
| DEV_004007  |           145 |                143 |       53.6897 |         100 |                60139.9 |                0.924138 |
| DEV_003932  |           100 |                 99 |       57.04   |         100 |                46842.9 |                0.81     |
| DEV_002418  |            97 |                 96 |       54.7835 |          78 |                31917.1 |                0.835052 |
| DEV_002048  |            95 |                 91 |       54.4737 |          93 |                55695.3 |                0.747368 |
| DEV_000102  |            89 |                 88 |       55.0674 |          89 |                40333.1 |                0.797753 |
| DEV_002459  |            88 |                 88 |       55.1705 |          89 |                41954.5 |                0.772727 |
| DEV_001272  |            87 |                 86 |       53.7011 |         100 |                82371.5 |                0.827586 |
| DEV_003863  |            86 |                 86 |       54.8721 |          86 |                34586.1 |                0.837209 |
| DEV_000361  |            83 |                 83 |       56.0723 |         100 |                55483   |                0.710843 |

## Top Beneficiários Alertados

| beneficiario_id   |   qtd_alertas |   contas_origem_distintas |   score_medio |   score_max |   valor_total_alertado |   taxa_fraude_sintetica |
|:------------------|--------------:|--------------------------:|--------------:|------------:|-----------------------:|------------------------:|
| BEN_002999        |           108 |                       106 |       61.4537 |         100 |               180489   |                0.787037 |
| BEN_003123        |           108 |                       105 |       59.6296 |         100 |               140199   |                0.731481 |
| BEN_003031        |           103 |                       102 |       61.6699 |         100 |               185370   |                0.805825 |
| BEN_000268        |           103 |                       102 |       60.5825 |          97 |               136142   |                0.84466  |
| BEN_001264        |            97 |                        97 |       59.1856 |          97 |               127915   |                0.721649 |
| BEN_001791        |            95 |                        95 |       59.6    |         100 |               126122   |                0.747368 |
| BEN_000352        |            94 |                        94 |       60.9149 |          97 |               140127   |                0.851064 |
| BEN_000998        |            93 |                        93 |       57.3763 |          96 |                95672.9 |                0.784946 |
| BEN_002787        |            94 |                        93 |       61.1277 |          87 |               152518   |                0.755319 |
| BEN_002457        |            93 |                        93 |       57.7312 |          87 |               105149   |                0.72043  |

## Observação

Os resultados são derivados de dados sintéticos criados exclusivamente para fins educacionais, analíticos e de portfólio.
O motor de regras não representa um sistema antifraude produtivo, mas demonstra uma abordagem explicável para investigação transacional.
