import pandas as pd


def get_numeric_columns(df: pd.DataFrame) -> list[str]:
    """
    Retorna lista de colunas numéricas.
    """
    return df.select_dtypes(include=["number"]).columns.tolist()


def get_categorical_columns(df: pd.DataFrame) -> list[str]:
    """
    Retorna lista de colunas categóricas/textuais.
    """
    return df.select_dtypes(include=["object", "category", "string"]).columns.tolist()


def basic_shape_report(df: pd.DataFrame, dataset_name: str) -> pd.DataFrame:
    """
    Retorna uma visão executiva simples sobre tamanho do dataset.
    """
    return pd.DataFrame(
        {
            "dataset": [dataset_name],
            "rows": [df.shape[0]],
            "columns": [df.shape[1]],
            "total_cells": [df.shape[0] * df.shape[1]],
        }
    )
