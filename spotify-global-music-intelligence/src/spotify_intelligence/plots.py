import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_missing_values(summary_df: pd.DataFrame, top_n: int = 20) -> None:
    """
    Plota as colunas com maior percentual de valores ausentes.
    Espera um DataFrame produzido pela função summarize_dataframe().
    """
    plot_df = (
        summary_df[summary_df["null_pct"] > 0]
        .sort_values("null_pct", ascending=False)
        .head(top_n)
    )

    if plot_df.empty:
        print("Não há valores ausentes para visualizar.")
        return

    plt.figure(figsize=(10, 6))
    sns.barplot(data=plot_df, x="null_pct", y="column")
    plt.title("Top colunas com maior percentual de valores ausentes")
    plt.xlabel("Percentual de nulos (%)")
    plt.ylabel("Coluna")
    plt.tight_layout()
    plt.show()
