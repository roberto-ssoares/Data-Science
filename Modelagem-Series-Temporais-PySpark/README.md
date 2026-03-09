# Projeto 2 — Análise e Visualização de Vendas ao Longo do Tempo com PySpark (Cluster Docker)

### Objetivo

Construir baseline de previsão de vendas ao longo do tempo, explorando estatística descritiva, correlação e modelagem com PySpark, executando em cluster Spark containerizado (master + 2 workers + history + jupyter driver).

### Arquitetura

- `spark-master-rss`: coordenação do cluster

- `spark-worker-rss-*`: executores (2 workers)

- `spark-history-rss`: histórico de jobs via event logs

- `jupyter-rss`: notebook como driver conectado ao master

### Como rodar (Cluster)

`docker compose up -d --scale spark-worker-rss=2`

Acessos:

- Jupyter: [http://localhost:8888](http://localhost:8888)

- Spark UI: http://localhost:9090

- History: http://localhost:18080

### Como rodar o treino via script

Dentro do container `jupyter-rss` (ou criar um serviço runner):

`docker exec -it jupyter-rss bash -lc "SPARK_MASTER=spark://spark-master-rss:7077 python /opt/spark/jobs/src/p02/train.py"`

### Notebooks

- `P02_01_Data_Understanding_Estatistico_PySpark.ipynb`

- `P02_02_Modelagem_Baseline_Cluster_PySpark.ipynb`

### Métricas

- RMSE

- R²

### Próximos passos

- Features temporais (lags, médias móveis)

- Modelos não-lineares (RF/GBT)

- Validação temporal (rolling/expanding)

- Streaming (real-time)
