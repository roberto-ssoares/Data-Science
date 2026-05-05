from pathlib import Path

import pandas as pd


def get_project_root() -> Path:
    """
    Retorna a raiz do projeto considerando que este arquivo está em:
    src/spotify_intelligence/data_io.py
    """
    return Path(__file__).resolve().parents[2]


def read_csv_safely(file_path: str | Path, **kwargs) -> pd.DataFrame:
    """
    Lê um arquivo CSV com configurações seguras para análise inicial.

    Parameters
    ----------
    file_path : str | Path
        Caminho do arquivo CSV.

    **kwargs
        Argumentos adicionais para pd.read_csv.

    Returns
    -------
    pd.DataFrame
        DataFrame carregado.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    return pd.read_csv(file_path, **kwargs)


def save_parquet(df: pd.DataFrame, file_path: str | Path) -> None:
    """
    Salva um DataFrame em formato Parquet.
    """
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(file_path, index=False)
