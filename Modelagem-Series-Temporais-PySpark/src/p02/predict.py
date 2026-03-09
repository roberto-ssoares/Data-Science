from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

from .config import DATA_PATH, MODEL_PATH, PRED_PATH, SPARK_MASTER, APP_NAME_PRED
from .io import read_sales_csv, write_predictions_csv
from .features import add_time_features

def get_spark(app_name: str) -> SparkSession:
    builder = SparkSession.builder.appName(app_name)
    if SPARK_MASTER:
        builder = builder.master(SPARK_MASTER)
    return builder.getOrCreate()

def main():
    spark = get_spark(APP_NAME_PRED)

    df = read_sales_csv(spark, DATA_PATH)
    df = add_time_features(df, "Date")

    model = PipelineModel.load(MODEL_PATH)
    pred = model.transform(df)

    write_predictions_csv(pred.select("Date", "Sales", "prediction"), PRED_PATH + "_full")

    spark.stop()

if __name__ == "__main__":
    main()
