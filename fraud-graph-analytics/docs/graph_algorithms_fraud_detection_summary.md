# Graph Algorithms Fraud Detection — Resumo Executivo

Este documento consolida os principais resultados do Notebook 05.

## Objetivo

Aplicar algoritmos de grafo para identificar entidades e comunidades suspeitas em uma base sintética de prevenção a fraudes transacionais.

## Síntese Geral

| item                        |   valor | interpretacao                                                       |
|:----------------------------|--------:|:--------------------------------------------------------------------|
| Nós no grafo                |   17000 | Entidades conectadas na projeção analítica.                         |
| Arestas no grafo            |  238066 | Relações agregadas entre contas, dispositivos, beneficiários e IPs. |
| Componentes conectados      |       1 | Grupos conectados por caminhos na rede.                             |
| Comunidades detectadas      |      21 | Comunidades detectadas pelo método louvain_communities.             |
| Entidades com risco crítico |     710 | Nós priorizados pela camada estrutural de grafo.                    |

## Distribuição por Tipo de Nó

| node_type    |   qtd_nos |
|:-------------|----------:|
| Conta        |      6000 |
| Dispositivo  |      4500 |
| Beneficiario |      3500 |
| IP           |      3000 |

## Relações Projetadas

| relation_type            |   qtd_edges |   peso_medio |   qtd_alertas |   score_medio |   valor_total |
|:-------------------------|------------:|-------------:|--------------:|--------------:|--------------:|
| ENVIOU_PARA_BENEFICIARIO |       79411 |      8.45974 |         79997 |       44.3757 |   8.10057e+07 |
| USOU_DISPOSITIVO         |       79329 |      8.45455 |         79997 |       44.2925 |   8.10057e+07 |
| USOU_IP                  |       79326 |      8.45635 |         79997 |       44.3093 |   8.10057e+07 |

## Top Comunidades por Risco

|   community_id |   community_size |   qtd_contas |   qtd_dispositivos |   qtd_beneficiarios |   qtd_ips |   qtd_alertas |   score_medio |   score_max |   taxa_alerta_media |   taxa_fraude_sintetica_media |   valor_total |   degree_medio |   weighted_degree_total |   pagerank_total |   betweenness_max |   node_type_diversity |   community_risk_score |
|---------------:|-----------------:|-------------:|-------------------:|--------------------:|----------:|--------------:|--------------:|------------:|--------------------:|------------------------------:|--------------:|---------------:|------------------------:|-----------------:|------------------:|----------------------:|-----------------------:|
|             16 |             1914 |          696 |                496 |                 383 |       339 |         35919 |       43.2959 |         100 |            1        |                     0.0554945 |   2.95077e+07 |        28.1594 |                  451832 |        0.112563  |        0.00146016 |                     4 |                  82.01 |
|              2 |             1571 |          568 |                405 |                 321 |       277 |         29335 |       43.2747 |         100 |            0.999928 |                     0.0618742 |   2.63925e+07 |        27.8568 |                  367454 |        0.0916687 |        0.0014044  |                     4 |                  77.01 |
|              7 |             1504 |          533 |                398 |                 317 |       256 |         27471 |       42.9968 |         100 |            0.999976 |                     0.0591184 |   2.53997e+07 |        27.2533 |                  342752 |        0.0858885 |        0.00141111 |                     4 |                  74.8  |
|             12 |             1320 |          466 |                356 |                 255 |       243 |         24012 |       42.8207 |         100 |            0.999908 |                     0.0553115 |   2.14258e+07 |        27.2545 |                  299849 |        0.0752529 |        0.00181957 |                     4 |                  74.75 |
|              4 |             1326 |          472 |                351 |                 284 |       219 |         24418 |       42.8885 |         100 |            1        |                     0.0584469 |   2.15004e+07 |        27.5173 |                  304824 |        0.0762901 |        0.00142928 |                     4 |                  73.58 |
|             14 |              915 |          327 |                231 |                 179 |       178 |         17059 |       43.6438 |         100 |            1        |                     0.0655034 |   1.65342e+07 |        27.7257 |                  213626 |        0.0532873 |        0.0015291  |                     4 |                  70.43 |
|             20 |              895 |          320 |                244 |                 175 |       156 |         16467 |       43.259  |         100 |            1        |                     0.0600992 |   1.55758e+07 |        27.5821 |                  207176 |        0.0517772 |        0.00153893 |                     4 |                  68.2  |
|             21 |              831 |          300 |                220 |                 176 |       135 |         15310 |       43.1955 |         100 |            1        |                     0.0609935 |   1.43197e+07 |        27.716  |                  193032 |        0.048235  |        0.00176227 |                     4 |                  66.51 |
|             13 |              768 |          248 |                209 |                 174 |       137 |         14712 |       43.9649 |         100 |            1        |                     0.0731627 |   1.59431e+07 |        28.5755 |                  187417 |        0.0464382 |        0.00151573 |                     4 |                  62.18 |
|             10 |              755 |          257 |                199 |                 171 |       128 |         14186 |       43.1486 |         100 |            0.999953 |                     0.0620383 |   1.29458e+07 |        28.0477 |                  177768 |        0.0443098 |        0.00142525 |                     4 |                  57.45 |
|             17 |              722 |          251 |                186 |                 145 |       140 |         13659 |       43.7061 |         100 |            0.998961 |                     0.0674792 |   1.17922e+07 |        28.0194 |                  171305 |        0.0426272 |        0.00137563 |                     4 |                  53.07 |
|              6 |              650 |          222 |                178 |                 121 |       129 |         12172 |       43.4697 |         100 |            0.999923 |                     0.0704911 |   1.30509e+07 |        28.0923 |                  154068 |        0.0383468 |        0.00165182 |                     4 |                  53.01 |
|              3 |              731 |          258 |                203 |                 151 |       119 |         13446 |       43.4429 |         100 |            1        |                     0.0597422 |   1.34019e+07 |        27.6908 |                  170717 |        0.0426233 |        0.0013235  |                     4 |                  49.91 |
|              5 |              562 |          188 |                152 |                 120 |       102 |         10799 |       43.8014 |         100 |            1        |                     0.0818782 |   9.94272e+06 |        28.5178 |                  136601 |        0.0338436 |        0.00141917 |                     4 |                  46.66 |
|              9 |              496 |          169 |                128 |                 107 |        92 |          9326 |       43.2933 |         100 |            0.999899 |                     0.0677328 |   7.65534e+06 |        28.2198 |                  117983 |        0.0293444 |        0.00146165 |                     4 |                  45.82 |

## Top Entidades por Risco de Grafo

| node                    | node_type    | entity_id   |   degree |   weighted_degree |    pagerank |   betweenness_approx |   community_id |   community_size |   community_risk_score |   qtd_transacoes |   qtd_alertas |   score_medio |   score_max |   taxa_alerta |   taxa_fraude_sintetica |   valor_total |   entity_graph_risk_score | entity_graph_risk_band   |
|:------------------------|:-------------|:------------|---------:|------------------:|------------:|---------------------:|---------------:|-----------------:|-----------------------:|-----------------:|--------------:|--------------:|------------:|--------------:|------------------------:|--------------:|--------------------------:|:-------------------------|
| Conta:CTA_002509        | Conta        | CTA_002509  |      254 |           3120.8  | 0.000674528 |          0.000821097 |             16 |             1914 |                  82.01 |               86 |            86 |       82.2791 |         100 |             1 |                0.895349 |      525957   |                     98.64 | critico                  |
| Dispositivo:DEV_000856  | Dispositivo  | DEV_000856  |      147 |           1398.3  | 0.000299819 |          0.000956129 |             16 |             1914 |                  82.01 |              150 |           150 |       54.4733 |          96 |             1 |                0.893333 |       74310.8 |                     97.87 | critico                  |
| Conta:CTA_000664        | Conta        | CTA_000664  |      252 |           2755.3  | 0.000596949 |          0.000745943 |              2 |             1571 |                  77.01 |               85 |            85 |       69.0353 |         100 |             1 |                0.929412 |      590316   |                     97.56 | critico                  |
| Conta:CTA_003626        | Conta        | CTA_003626  |      135 |           1434    | 0.000317031 |          0.000539762 |              2 |             1571 |                  77.01 |               45 |            45 |       66.2222 |         100 |             1 |                0.733333 |       60066.6 |                     97.23 | critico                  |
| Dispositivo:DEV_002736  | Dispositivo  | DEV_002736  |       76 |            731.8  | 0.000159129 |          0.000358947 |              2 |             1571 |                  77.01 |               76 |            76 |       56.2895 |         100 |             1 |                0.881579 |      114463   |                     96.39 | critico                  |
| Dispositivo:DEV_002048  | Dispositivo  | DEV_002048  |       91 |            873.1  | 0.000189151 |          0.000315985 |             16 |             1914 |                  82.01 |               95 |            95 |       54.4737 |          93 |             1 |                0.747368 |       55695.3 |                     96.38 | critico                  |
| Beneficiario:BEN_002999 | Beneficiario | BEN_002999  |      106 |           1082.6  | 0.000233527 |          0.000301931 |              2 |             1571 |                  77.01 |              108 |           108 |       61.4537 |         100 |             1 |                0.787037 |      180489   |                     96.37 | critico                  |
| Beneficiario:BEN_000283 | Beneficiario | BEN_000283  |       82 |            821.3  | 0.0001786   |          0.000209443 |             16 |             1914 |                  82.01 |               82 |            82 |       60.1585 |         100 |             1 |                0.768293 |       98789.2 |                     96.28 | critico                  |
| Conta:CTA_001134        | Conta        | CTA_001134  |      236 |           2847.75 | 0.000615133 |          0.000439573 |              7 |             1504 |                  74.8  |               79 |            79 |       80.4557 |         100 |             1 |                0.835443 |      433077   |                     96.21 | critico                  |
| Conta:CTA_001014        | Conta        | CTA_001014  |       84 |            763.8  | 0.000174644 |          0.00138895  |              2 |             1571 |                  77.01 |               28 |            28 |       50.9286 |         100 |             1 |                0.178571 |      183403   |                     95.89 | critico                  |
| Dispositivo:DEV_000671  | Dispositivo  | DEV_000671  |       79 |            766.1  | 0.000167347 |          0.000256305 |              2 |             1571 |                  77.01 |               79 |            79 |       56.9747 |         100 |             1 |                0.898734 |       56482.2 |                     95.74 | critico                  |
| Dispositivo:DEV_001848  | Dispositivo  | DEV_001848  |       63 |            614.2  | 0.000137282 |          0.000169464 |             16 |             1914 |                  82.01 |               65 |            65 |       56.3692 |         100 |             1 |                0.784615 |       31253.8 |                     95.2  | critico                  |
| Conta:CTA_003281        | Conta        | CTA_003281  |      164 |           1875.5  | 0.00041117  |          0.000399659 |             12 |             1320 |                  74.75 |               55 |            55 |       74.2909 |         100 |             1 |                0.690909 |       92931.9 |                     95.2  | critico                  |
| Conta:CTA_000875        | Conta        | CTA_000875  |      222 |           2406.3  | 0.000528279 |          0.00108179  |              4 |             1326 |                  73.58 |               75 |            75 |       67.96   |         100 |             1 |                0.84     |      385964   |                     95.13 | critico                  |
| Beneficiario:BEN_002517 | Beneficiario | BEN_002517  |       74 |            740.6  | 0.000163378 |          0.000207433 |              2 |             1571 |                  77.01 |               75 |            75 |       59.6267 |         100 |             1 |                0.746667 |      111428   |                     95.12 | critico                  |
| Dispositivo:DEV_004007  | Dispositivo  | DEV_004007  |      143 |           1344.3  | 0.00028781  |          0.000724795 |              4 |             1326 |                  73.58 |              145 |           145 |       53.6897 |         100 |             1 |                0.924138 |       60139.9 |                     94.98 | critico                  |
| Dispositivo:DEV_000105  | Dispositivo  | DEV_000105  |       68 |            646.2  | 0.000143228 |          0.000271535 |              7 |             1504 |                  74.8  |               69 |            69 |       54.6087 |         100 |             1 |                0.826087 |       32608.2 |                     94.75 | critico                  |
| Beneficiario:BEN_000903 | Beneficiario | BEN_000903  |       92 |            939.7  | 0.000204924 |          0.000410413 |              4 |             1326 |                  73.58 |               92 |            92 |       62.1413 |         100 |             1 |                0.771739 |      127894   |                     94.32 | critico                  |
| Dispositivo:DEV_002307  | Dispositivo  | DEV_002307  |       83 |            782.4  | 0.000171675 |          0.000193944 |             16 |             1914 |                  82.01 |               83 |            83 |       54.2651 |          88 |             1 |                0.807229 |       32110   |                     94.06 | critico                  |
| Conta:CTA_005335        | Conta        | CTA_005335  |      240 |           2502.6  | 0.000543485 |          0.00117911  |             20 |              895 |                  68.2  |               81 |            81 |       63.8765 |         100 |             1 |                0.802469 |      457827   |                     93.97 | critico                  |
| Dispositivo:DEV_000102  | Dispositivo  | DEV_000102  |       88 |            839.5  | 0.000184287 |          0.000187519 |              2 |             1571 |                  77.01 |               89 |            89 |       55.0674 |          89 |             1 |                0.797753 |       40333.1 |                     93.5  | critico                  |
| Beneficiario:BEN_002787 | Beneficiario | BEN_002787  |       93 |            942.55 | 0.000204632 |          0.000230942 |              2 |             1571 |                  77.01 |               94 |            94 |       61.1277 |          87 |             1 |                0.755319 |      152518   |                     93.48 | critico                  |
| Conta:CTA_005360        | Conta        | CTA_005360  |      233 |           2586.9  | 0.000566827 |          0.000734779 |             21 |              831 |                  66.51 |               79 |            79 |       70.6203 |         100 |             1 |                0.835443 |      409792   |                     93.32 | critico                  |
| Conta:CTA_000903        | Conta        | CTA_000903  |       72 |            710.1  | 0.000159826 |          0.000791615 |              7 |             1504 |                  74.8  |               24 |            24 |       58.625  |         100 |             1 |                0.333333 |      183111   |                     93.08 | critico                  |
| Conta:CTA_002395        | Conta        | CTA_002395  |      231 |           2421.05 | 0.000528028 |          0.0010094   |             13 |              768 |                  62.18 |               78 |            78 |       64.4615 |         100 |             1 |                0.846154 |      471439   |                     92.96 | critico                  |

## Achados dos Algoritmos

| algoritmo                | achado                                                                                            | interpretacao_antifraude                                                                                   | uso_no_proximo_notebook                                        |
|:-------------------------|:--------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|
| Degree / Weighted Degree | Entidades com muitas conexões ou conexões de alto peso foram destacadas.                          | Pode indicar beneficiários concentradores, dispositivos compartilhados ou IPs usados por múltiplas contas. | Compor variáveis estruturais no score de risco explicável.     |
| PageRank                 | Entidades estruturalmente relevantes foram identificadas considerando a importância dos vizinhos. | Ajuda a priorizar nós que ocupam regiões importantes da rede, mesmo quando não têm o maior grau bruto.     | Adicionar camada de relevância relacional ao score final.      |
| Connected Components     | O grafo foi segmentado em grupos conectados.                                                      | Componentes maiores podem representar regiões de maior complexidade investigativa.                         | Usar tamanho e composição do componente como sinal contextual. |
| Community Detection      | Comunidades foram detectadas a partir da estrutura de conexões.                                   | Comunidades com muitas contas, dispositivos, beneficiários e alertas podem indicar atuação coordenada.     | Usar community_risk_score como componente do score final.      |
| Betweenness aproximado   | Nós com potencial papel de ponte foram identificados.                                             | Contas ou entidades ponte podem conectar grupos distintos e merecer investigação prioritária.              | Adicionar sinal de intermediação estrutural ao score final.    |

## Valor Analítico

- Identificação de entidades estruturalmente relevantes.
- Priorização de comunidades suspeitas.
- Complemento ao motor de regras antifraude.
- Criação de features relacionais para score explicável.
- Preparação para uso posterior no Neo4j Graph Data Science.

## Observação

Os resultados são derivados de dados sintéticos criados exclusivamente para fins educacionais, analíticos e de portfólio.
