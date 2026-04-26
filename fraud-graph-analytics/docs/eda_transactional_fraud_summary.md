# EDA Transactional Fraud — Resumo Executivo

Este documento consolida os principais resultados do Notebook 02.

## KPIs Gerais

| indicador                   |           valor |
|:----------------------------|----------------:|
| total_transacoes            | 80000           |
| taxa_fraude_sintetica       |     0.0875      |
| valor_total_transacionado   |     8.10057e+07 |
| valor_medio                 |  1012.57        |
| valor_mediano               |   299.645       |
| qtd_clientes_distintos      |  3487           |
| qtd_contas_distintas        |  6000           |
| qtd_beneficiarios_distintos |  3500           |
| qtd_dispositivos_distintos  |  4500           |
| qtd_ips_distintos           |  3000           |
| qtd_transacoes_em_analise   |  3550           |
| qtd_transacoes_negadas      |  3664           |

## Distribuição dos Cenários

| fraud_scenario           |   qtd_transacoes |   taxa_fraude |      valor_total |   valor_medio |   contas_distintas |   beneficiarios_distintos |   dispositivos_distintos |   percentual_transacoes |
|:-------------------------|-----------------:|--------------:|-----------------:|--------------:|-------------------:|--------------------------:|-------------------------:|------------------------:|
| normal                   |            73000 |             0 |      3.44712e+07 |       472.208 |               6000 |                      3500 |                     4500 |                  0.9125 |
| shared_device_ring       |             1600 |             1 | 706118           |       441.324 |               1381 |                      1266 |                       23 |                  0.02   |
| beneficiary_concentrator |             1400 |             1 |      2.22096e+06 |      1586.4   |               1244 |                        20 |                     1209 |                  0.0175 |
| burst_transactions       |             1200 |             1 |      2.25109e+06 |      1875.91  |                 40 |                      1020 |                     1049 |                  0.015  |
| new_account_high_value   |             1000 |             1 |      2.67525e+07 |     26752.5   |                261 |                       854 |                      909 |                  0.0125 |
| coordinated_network      |             1000 |             1 |      9.35903e+06 |      9359.03  |                 60 |                        15 |                       10 |                  0.0125 |
| bridge_account           |              800 |             1 |      5.24484e+06 |      6556.05  |                 12 |                       717 |                      736 |                  0.01   |

## Valor por Cenário

| fraud_scenario           |   qtd_transacoes |   valor_medio |   valor_mediano |   valor_p95 |   valor_max |
|:-------------------------|-----------------:|--------------:|----------------:|------------:|------------:|
| new_account_high_value   |             1000 |     26752.5   |       26593     |    42909.2  |    44999.7  |
| coordinated_network      |             1000 |      9359.03  |        9387.64  |    16966.9  |    17980.4  |
| bridge_account           |              800 |      6556.05  |        6651.77  |    11643.6  |    11984.3  |
| burst_transactions       |             1200 |      1875.91  |        1815.92  |     3296.96 |     3499.92 |
| beneficiary_concentrator |             1400 |      1586.4   |        1230.71  |     4066.21 |     8670.9  |
| normal                   |            73000 |       472.208 |         272.78  |     1529.56 |    25000    |
| shared_device_ring       |             1600 |       441.324 |         264.495 |     1363.16 |     9947.93 |

## Top Beneficiários Concentradores

| beneficiario_id   |   qtd_transacoes |   contas_origem_distintas |   clientes_distintos |   valor_total |   valor_medio |   taxa_fraude |   qtd_cenarios | tipo_beneficiario   | banco_destino     | uf_destino   |
|:------------------|-----------------:|--------------------------:|---------------------:|--------------:|--------------:|--------------:|---------------:|:--------------------|:------------------|:-------------|
| BEN_002999        |              108 |                       106 |                  103 |      180489   |       1671.2  |      0.787037 |              6 | pessoa_fisica       | banco_d           | RJ           |
| BEN_003123        |              108 |                       105 |                  105 |      140199   |       1298.14 |      0.731481 |              2 | conta_interna       | banco_b           | PE           |
| BEN_003031        |              103 |                       102 |                  102 |      185370   |       1799.7  |      0.805825 |              3 | pessoa_fisica       | banco_a           | GO           |
| BEN_000268        |              103 |                       102 |                  101 |      136142   |       1321.76 |      0.84466  |              3 | pessoa_fisica       | mesma_instituicao | ES           |
| BEN_001264        |               97 |                        97 |                   94 |      127915   |       1318.71 |      0.721649 |              3 | pessoa_fisica       | banco_d           | ES           |
| BEN_001791        |               95 |                        95 |                   95 |      126122   |       1327.6  |      0.747368 |              2 | pessoa_juridica     | banco_b           | DF           |
| BEN_000352        |               94 |                        94 |                   94 |      140127   |       1490.72 |      0.851064 |              2 | pessoa_juridica     | banco_b           | ES           |
| BEN_002787        |               94 |                        93 |                   92 |      152518   |       1622.53 |      0.755319 |              3 | pessoa_juridica     | banco_d           | RS           |
| BEN_002457        |               93 |                        93 |                   92 |      105149   |       1130.64 |      0.72043  |              3 | pessoa_fisica       | banco_b           | SC           |
| BEN_000998        |               93 |                        93 |                   93 |       95672.9 |       1028.74 |      0.784946 |              3 | pessoa_fisica       | banco_b           | DF           |

## Top Dispositivos Compartilhados

| device_id   |   qtd_transacoes |   contas_distintas |   clientes_distintos |   beneficiarios_distintos |   valor_total |   valor_medio |   taxa_fraude | tipo_device   | sistema_operacional   | fingerprint_risco   |
|:------------|-----------------:|-------------------:|---------------------:|--------------------------:|--------------:|--------------:|--------------:|:--------------|:----------------------|:--------------------|
| DEV_000856  |              150 |                147 |                  146 |                       143 |       74310.8 |       495.406 |      0.893333 | desktop       | Android               | alto                |
| DEV_004007  |              145 |                143 |                  140 |                       145 |       60139.9 |       414.758 |      0.924138 | mobile        | iOS                   | alto                |
| DEV_003932  |              100 |                 99 |                   99 |                        98 |       46842.9 |       468.429 |      0.81     | mobile        | Android               | alto                |
| DEV_002418  |               97 |                 96 |                   94 |                        96 |       31917.1 |       329.042 |      0.835052 | mobile        | Windows               | alto                |
| DEV_002048  |               95 |                 91 |                   90 |                        94 |       55695.3 |       586.266 |      0.747368 | mobile        | Windows               | alto                |
| DEV_000102  |               89 |                 88 |                   88 |                        88 |       40333.1 |       453.181 |      0.797753 | mobile        | Windows               | alto                |
| DEV_002459  |               88 |                 88 |                   87 |                        88 |       41954.5 |       476.756 |      0.772727 | mobile        | Android               | alto                |
| DEV_003863  |               86 |                 86 |                   84 |                        86 |       34586.1 |       402.164 |      0.837209 | mobile        | iOS                   | alto                |
| DEV_001272  |               87 |                 86 |                   85 |                        86 |       82371.5 |       946.799 |      0.827586 | tablet        | Android               | alto                |
| DEV_002307  |               83 |                 83 |                   83 |                        83 |       32110   |       386.868 |      0.807229 | desktop       | Linux                 | alto                |

## Regras Candidatas

| regra_candidata                |   qtd_transacoes_acionadas |   taxa_fraude_entre_acionadas |   valor_medio_acionadas |   qtd_cenarios_cobertos |
|:-------------------------------|---------------------------:|------------------------------:|------------------------:|------------------------:|
| r006_transacoes_em_rajada      |                       1183 |                     1         |                 1871.81 |                       1 |
| r004_conta_nova_alto_valor     |                       1944 |                     0.774691  |                15944.2  |                       7 |
| r001_alto_valor                |                       4000 |                     0.753     |                11708.3  |                       7 |
| r005_rede_ou_device_risco      |                       9517 |                     0.314175  |                 1685.05 |                       7 |
| r003_beneficiario_concentrador |                      31469 |                     0.129747  |                 1179.11 |                       7 |
| r002_dispositivo_compartilhado |                      79996 |                     0.0875044 |                 1012.58 |                       7 |

## Achados Principais

| achado                                                            | evidencia                                                                                                                     | implicacao                                                                           |
|:------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
| Cenários sintéticos de fraude foram preservados                   | A base contém cenários como dispositivo compartilhado, beneficiário concentrador, conta nova de alto valor e rede coordenada. | A base está adequada para desenvolver regras antifraude e análises de grafo.         |
| Valores transacionais variam fortemente por cenário               | Cenários como conta nova de alto valor e beneficiário concentrador apresentam maior valor médio.                              | Regras baseadas em percentis de valor podem capturar parte dos riscos.               |
| Beneficiários concentradores possuem alto potencial investigativo | Alguns beneficiários recebem transações de muitas contas distintas.                                                           | Beneficiários devem ser nós centrais no Knowledge Graph.                             |
| Dispositivos compartilhados são sinal estrutural forte            | Dispositivos com muitas contas distintas aparecem como candidatos relevantes.                                                 | Device centrality e shared-device rules devem compor o motor antifraude.             |
| Combinação de regras aumenta a priorização                        | Transações com múltiplas regras acionadas apresentam maior valor investigativo.                                               | O próximo notebook deve criar um score baseado em severidade e quantidade de sinais. |

## Observação

Os resultados são derivados de dados sintéticos criados exclusivamente para fins educacionais, analíticos e de portfólio.
