from pyspark.sql import DataFrame
from pyspark.sql.functions import col, year, month

def add_time_features(df: DataFrame, date_col: str = "Date") -> DataFrame:
    # Cast para date + Year/Month
    df = df.withColumn(date_col, col(date_col).cast("date"))
    df = df.withColumn("Year", year(col(date_col))).withColumn("Month", month(col(date_col)))
    return df

def temporal_split(df: DataFrame, date_col: str = "Date", train_ratio: float = 0.8):
    """
    Split temporal: ordena por data e pega as primeiras N linhas para treino,
    e o restante para teste. Evita leakage do randomSplit em séries temporais.
    """
    df = df.orderBy(date_col)
    n = df.count()
    cutoff = int(n * train_ratio)

    # zipWithIndex para split determinístico
    df_idx = df.rdd.zipWithIndex().toDF(["row", "idx"]).select("row.*", "idx")
    train = df_idx.filter(col("idx") < cutoff).drop("idx")
    test  = df_idx.filter(col("idx") >= cutoff).drop("idx")
    return train, test
