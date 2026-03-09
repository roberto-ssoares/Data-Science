from pyspark.sql import DataFrame
from pyspark.sql.functions import col
from pyspark.ml.stat import Summarizer, Correlation
from pyspark.ml.feature import VectorAssembler

def sales_basic_stats(df: DataFrame, sales_col: str = "Sales") -> DataFrame:
    # mean, variance, min, max
    return df.select(
        Summarizer.metrics("mean", "variance", "min", "max").summary(col(sales_col)).alias("summary")
    )

def correlation_year_month_sales(df: DataFrame) -> DataFrame:
    """
    Retorna uma matriz de correlação para [Year, Month, Sales].
    """
    vec = VectorAssembler(inputCols=["Year", "Month", "Sales"], outputCol="features_corr")
    df_corr = vec.transform(df).select("features_corr")
    return Correlation.corr(df_corr, "features_corr")
