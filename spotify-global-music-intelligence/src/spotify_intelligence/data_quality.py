import pandas as pd


def summarize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria um resumo técnico das colunas do DataFrame.

    Retorna informações de:
    - tipo de dado;
    - quantidade de nulos;
    - percentual de nulos;
    - quantidade de valores únicos;
    - percentual de cardinalidade.
    """
    total_rows = len(df)

    summary = pd.DataFrame(
        {
            "column": df.columns,
            "dtype": [df[col].dtype for col in df.columns],
            "null_count": [df[col].isna().sum() for col in df.columns],
            "null_pct": [df[col].isna().mean() * 100 for col in df.columns],
            "unique_count": [df[col].nunique(dropna=True) for col in df.columns],
            "unique_pct": [
                (df[col].nunique(dropna=True) / total_rows * 100) if total_rows > 0 else 0
                for col in df.columns
            ],
        }
    )

    return summary.sort_values(by=["null_pct", "unique_count"], ascending=[False, False])


def duplicated_rows_report(df: pd.DataFrame) -> dict:
    """
    Retorna diagnóstico simples de duplicidade de linhas.
    """
    duplicated_count = df.duplicated().sum()
    total_rows = len(df)

    return {
        "total_rows": total_rows,
        "duplicated_rows": int(duplicated_count),
        "duplicated_pct": float((duplicated_count / total_rows * 100) if total_rows > 0 else 0),
    }
