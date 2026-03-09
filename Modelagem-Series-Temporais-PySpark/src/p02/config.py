import os

def env(name: str, default: str) -> str:
    return os.getenv(name, default)

# Paths (dentro do container)
DATA_PATH  = env("DATA_PATH",  "/opt/spark/dados/dataset.csv")
MODEL_PATH = env("MODEL_PATH", "/opt/spark/jobs/artifacts/model/modelo_p02")
PRED_PATH  = env("PRED_PATH",  "/opt/spark/jobs/artifacts/predictions/pred_p02")

# Spark
SPARK_MASTER = os.getenv("SPARK_MASTER")  # ex: spark://spark-master-rss:7077
APP_NAME_TRAIN = env("APP_NAME_TRAIN", "P02-Treino")
APP_NAME_PRED  = env("APP_NAME_PRED",  "P02-Predict")
