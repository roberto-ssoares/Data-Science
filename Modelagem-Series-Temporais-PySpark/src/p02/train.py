from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml import Pipeline

from .config import DATA_PATH, MODEL_PATH, PRED_PATH, SPARK_MASTER, APP_NAME_TRAIN
from .io import read_sales_csv, write_predictions_csv
from .features import add_time_features, temporal_split

def get_spark(app_name: str) -> SparkSession:
    builder = SparkSession.builder.appName(app_name)
    if SPARK_MASTER:
        builder = builder.master(SPARK_MASTER)
    return builder.getOrCreate()

def main():
    spark = get_spark(APP_NAME_TRAIN)

    df = read_sales_csv(spark, DATA_PATH)
    df = add_time_features(df, "Date")

    train_df, test_df = temporal_split(df, "Date", train_ratio=0.8)

    assembler = VectorAssembler(inputCols=["Year", "Month"], outputCol="Features")
    lr = LinearRegression(featuresCol="Features", labelCol="Sales")
    pipeline = Pipeline(stages=[assembler, lr])

    model = pipeline.fit(train_df)
    pred = model.transform(test_df)

    rmse = RegressionEvaluator(labelCol="Sales", predictionCol="prediction", metricName="rmse").evaluate(pred)
    r2   = RegressionEvaluator(labelCol="Sales", predictionCol="prediction", metricName="r2").evaluate(pred)

    print(f"RMSE = {rmse}")
    print(f"R2   = {r2}")

    model.write().overwrite().save(MODEL_PATH)
    write_predictions_csv(pred.select("Date", "Sales", "prediction"), PRED_PATH)

    spark.stop()

if __name__ == "__main__":
    main()
