from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

def read_sales_csv(spark: SparkSession, path: str) -> DataFrame:
    return spark.read.csv(path, header=True, inferSchema=True)

def write_predictions_csv(df: DataFrame, path: str) -> None:
    (
        df.write
        .mode("overwrite")
        .option("header", True)
        .csv(path)
    )
