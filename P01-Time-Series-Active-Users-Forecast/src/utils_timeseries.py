"""
utils_timeseries.py

Funções utilitárias para carregamento, preparação e
análise básica de séries temporais.

Autor: Roberto dos Santos Soares
Projeto: P01 - Processo de Análise de Séries Temporais
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Optional, Tuple, Union

import pandas as pd


def load_timeseries(
    filepath: Union[str, Path],
    date_col: Union[int, str] = 0,
    value_col: Union[int, str] = 1,
    *,
    has_header: bool = True,
    column_names: Optional[Tuple[str, str]] = None,
    date_format: Optional[str] = None,
    freq: Optional[str] = None,
    dropna: bool = True,
    sort_index: bool = True,
    index_name: str = "data",
) -> pd.Series:
    """
    Carrega um CSV simples (com ou sem cabeçalho) e retorna uma pd.Series indexada por data.

    - Aceita date_col/value_col como índice (int) ou nome (str).
    - Se has_header=False, lê com header=None e renomeia para column_names (obrigatório nesse caso).
    """

    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

    # ------------------------------
    # Leitura do CSV (com/sem header)
    # ------------------------------
    if has_header:
        df = pd.read_csv(filepath)
    else:
        if not column_names or len(column_names) != 2:
            raise ValueError(
                "Para has_header=False, informe column_names com 2 nomes, ex: ('data','usuarios_ativos')."
            )
        df = pd.read_csv(filepath, header=None)
        df = df.rename(columns={0: column_names[0], 1: column_names[1]})

    # ------------------------------
    # Resolver colunas por índice/nome
    # ------------------------------
    def _resolve_col(col: Union[int, str]) -> str:
        if isinstance(col, int):
            # converte posição -> nome real da coluna
            try:
                return df.columns[col]
            except Exception as e:
                raise KeyError(f"Coluna na posição {col} não existe. Colunas: {list(df.columns)}") from e
        # string
        if col not in df.columns:
            raise KeyError(f"Coluna '{col}' não existe. Colunas: {list(df.columns)}")
        return col

    date_col_name = _resolve_col(date_col)
    value_col_name = _resolve_col(value_col)

    # ------------------------------
    # Tipagem/conversão
    # ------------------------------
    if date_format is not None:
        df[date_col_name] = pd.to_datetime(df[date_col_name], format=date_format, errors="coerce")
    else:
        df[date_col_name] = pd.to_datetime(df[date_col_name], errors="coerce")

    df[value_col_name] = pd.to_numeric(df[value_col_name], errors="coerce")

    # ------------------------------
    # Montar série
    # ------------------------------
    ts = df.set_index(date_col_name)[value_col_name]
    ts.index.name = index_name

    if dropna:
        ts = ts.dropna()

    if sort_index:
        ts = ts.sort_index()

    if freq is not None:
        # garante frequência explícita; se houver buracos, vira NaN (bom para diagnosticar)
        ts = ts.asfreq(freq)

    return ts


# ---------------------------------------------------------------------------

def ensure_datetime_index(
    serie: pd.Series,
    freq: Optional[str] = None,
    sort_index: bool = True,
    index_name: str = "date",
) -> pd.Series:
    """
    Garante que a série tenha índice datetime.

    Parâmetros
    ----------
    serie : pd.Series
        Série temporal de entrada.
    freq : str, opcional
        Frequência desejada (ex: 'D', 'M').
    sort_index : bool, default True
        Se True, ordena o índice.
    index_name : str, default 'date'
        Nome a ser atribuído ao índice.

    Retorno
    -------
    pd.Series
        Série com índice datetime garantido.
    """
    # Se o índice já for datetime, apenas ajusta
    if not np.issubdtype(serie.index.dtype, np.datetime64):
        serie.index = pd.to_datetime(serie.index, infer_datetime_format=True)

    if sort_index:
        serie = serie.sort_index()

    serie.index.name = index_name

    if freq is not None:
        serie = serie.asfreq(freq)

    return serie

# --------------------------------------------------------------------------------------    

def fill_missing(
    serie: pd.Series,
    method: str = "ffill",
    value: Optional[float] = None,
) -> pd.Series:
    """
    Preenche valores faltantes na série temporal.

    Parâmetros
    ----------
    serie : pd.Series
        Série temporal.
    method : str, default 'ffill'
        Método de preenchimento:
        - 'ffill': forward fill (carrega último valor conhecido)
        - 'bfill': backward fill
        - 'mean': média
        - 'median': mediana
        - 'zero': zero
        - 'value': usa o parâmetro 'value'
    value : float, opcional
        Valor a ser utilizado quando method='value'.

    Retorno
    -------
    pd.Series
        Série com valores faltantes preenchidos.
    """
    if method == "ffill":
        return serie.ffill()
    elif method == "bfill":
        return serie.bfill()
    elif method == "mean":
        return serie.fillna(serie.mean())
    elif method == "median":
        return serie.fillna(serie.median())
    elif method == "zero":
        return serie.fillna(0.0)
    elif method == "value":
        if value is None:
            raise ValueError("Para method='value', é necessário informar 'value'.")
        return serie.fillna(value)
    else:
        raise ValueError(f"Método de preenchimento não suportado: {method}")

# ----------------------------------------------------------------------------------------

def difference_series(
    serie: pd.Series,
    order: int = 1,
    dropna: bool = True,
) -> pd.Series:
    """
    Aplica diferenciação na série temporal (série de diferenças).

    Parâmetros
    ----------
    serie : pd.Series
        Série temporal original.
    order : int, default 1
        Ordem da diferenciação (1, 2, ...).
    dropna : bool, default True
        Se True, remove NaNs gerados pela diferenciação.

    Retorno
    -------
    pd.Series
        Série diferenciada.
    """
    diff = serie.copy()
    for _ in range(order):
        diff = diff.diff()

    if dropna:
        diff = diff.dropna()

    return diff

# --------------------------------------------------------------------------------------    

def adfuller_test(
    serie: pd.Series,
    alpha: float = 0.05,
    autolag: str = "AIC",
    verbose: bool = False,
) -> Dict[str, Any]:
    """
    Executa o teste ADF (Dickey-Fuller Aumentado) e retorna
    um dicionário com os resultados principais.

    Parâmetros
    ----------
    serie : pd.Series
        Série temporal a ser testada.
    alpha : float, default 0.05
        Nível de significância para decisão de estacionariedade.
    autolag : str, default 'AIC'
        Critério de seleção de defasagem usado pelo statsmodels.adfuller.
    verbose : bool, default False
        Se True, imprime um resumo amigável na tela.

    Retorno
    -------
    dict
        {
            'test_statistic': float,
            'p_value': float,
            'used_lag': int,
            'n_obs': int,
            'critical_values': dict,
            'is_stationary': bool,
            'alpha': float
        }
    """
    serie_clean = serie.dropna()

    result = adfuller(serie_clean, autolag=autolag)
    test_statistic, p_value, used_lag, n_obs, critical_values, _ = result

    is_stationary = p_value < alpha

    output = {
        "test_statistic": test_statistic,
        "p_value": p_value,
        "used_lag": used_lag,
        "n_obs": n_obs,
        "critical_values": critical_values,
        "is_stationary": is_stationary,
        "alpha": alpha,
    }

    if verbose:
        print("=== Teste Dickey-Fuller Aumentado (ADF) ===")
        print(f"Estatística de teste: {test_statistic:.4f}")
        print(f"Valor-p: {p_value:.4f}")
        print(f"Lag utilizado: {used_lag}")
        print(f"Número de observações: {n_obs}")
        print("Valores críticos:")
        for k, v in critical_values.items():
            print(f"  {k}: {v:.4f}")
        print("-------------------------------------------")
        if is_stationary:
            print(f"Conclusão: Rejeitamos H0 ao nível de {alpha}.")
            print("A série pode ser considerada estacionária.")
        else:
            print(f"Conclusão: Não rejeitamos H0 ao nível de {alpha}.")
            print("A série NÃO pode ser considerada estacionária.")

    return output

# ---------------------------------------------------------------------------------------------

def boxcox_transform(
    serie: pd.Series,
    lmbda: Optional[float] = None,
) -> Tuple[pd.Series, float]:
    """
    Aplica transformação Box-Cox à série.

    Parâmetros
    ----------
    serie : pd.Series
        Série de entrada (deve ser estritamente positiva).
    lmbda : float, opcional
        Lambda da transformação. Se None, será estimado via máxima verossimilhança.

    Retorno
    -------
    (serie_transformada, lambda_utilizado)
    """
    serie_clean = serie.dropna()

    if (serie_clean <= 0).any():
        raise ValueError("A transformação Box-Cox requer todos os valores > 0.")

    if lmbda is None:
        transformed_values, fitted_lambda = stats.boxcox(serie_clean.values)
        lmbda_to_use = fitted_lambda
    else:
        transformed_values = stats.boxcox(serie_clean.values, lmbda=lmbda)
        lmbda_to_use = lmbda

    transformed = pd.Series(
        data=transformed_values,
        index=serie_clean.index,
        name=f"{serie.name}_boxcox" if serie.name else "serie_boxcox",
    )

    return transformed, lmbda_to_use
