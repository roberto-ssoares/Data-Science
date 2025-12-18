"""
plot_functions.py

Funções de visualização para análise de séries temporais.

Autor: Roberto dos Santos Soares
Projeto: P01 - Processo de Análise de Séries Temporais
"""

from __future__ import annotations

from typing import Optional, Tuple

import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def plot_series(
    serie: pd.Series,
    title: str = "Série Temporal",
    xlabel: str = "Tempo",
    ylabel: str = "Valor",
    figsize: Tuple[int, int] = (12, 4),
    grid: bool = True,
) -> None:
    """
    Plota uma série temporal simples.

    Parâmetros
    ----------
    serie : pd.Series
        Série temporal a ser plotada.
    title : str, default 'Série Temporal'
        Título do gráfico.
    xlabel : str, default 'Tempo'
    ylabel : str, default 'Valor'
    figsize : tuple, default (12, 4)
        Tamanho da figura em polegadas.
    grid : bool, default True
        Se True, exibe grid no gráfico.
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(serie.index, serie.values)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if grid:
        ax.grid(True)
    fig.tight_layout()
    plt.show()


def plot_decomposition(
    serie: pd.Series,
    model: str = "additive",
    freq: Optional[int] = None,
    figsize: Tuple[int, int] = (12, 8),
) -> None:
    """
    Realiza e plota a decomposição de uma série temporal.

    Parâmetros
    ----------
    serie : pd.Series
        Série temporal.
    model : str, default 'additive'
        Modelo de decomposição ('additive' ou 'multiplicative').
    freq : int, opcional
        Período sazonal (por ex: 12 para mensal com sazonalidade anual).
        Se None, o statsmodels tenta inferir em algumas situações.
    figsize : tuple, default (12, 8)
        Tamanho da figura.
    """
    decomposition = seasonal_decompose(serie.dropna(), model=model, period=freq)

    fig = decomposition.plot()
    fig.set_size_inches(figsize[0], figsize[1])
    fig.tight_layout()
    plt.show()


def plot_rolling_statistics(
    serie: pd.Series,
    window: int = 12,
    title: str = "Rolling Mean & Rolling Std",
    figsize: Tuple[int, int] = (12, 4),
) -> None:
    """
    Plota série original, média móvel e desvio padrão móvel.

    Parâmetros
    ----------
    serie : pd.Series
        Série temporal.
    window : int, default 12
        Tamanho da janela de cálculo das estatísticas móveis.
    title : str, default 'Rolling Mean & Rolling Std'
        Título do gráfico.
    figsize : tuple, default (12, 4)
        Tamanho da figura.
    """
    rolmean = serie.rolling(window=window).mean()
    rolstd = serie.rolling(window=window).std()

    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(serie, label="Série original")
    ax.plot(rolmean, label=f"Média móvel ({window})", linestyle="--")
    ax.plot(rolstd, label=f"Desvio padrão móvel ({window})", linestyle=":")
    ax.set_title(title)
    ax.set_xlabel("Tempo")
    ax.set_ylabel("Valor")
    ax.legend()
    ax.grid(True)
    fig.tight_layout()
    plt.show()


def plot_acf_pacf_side_by_side(
    serie: pd.Series,
    lags: int = 40,
    figsize: Tuple[int, int] = (12, 4),
) -> None:
    """
    Plota ACF e PACF lado a lado para uma série temporal.

    Parâmetros
    ----------
    serie : pd.Series
        Série temporal.
    lags : int, default 40
        Número de defasagens a serem exibidas.
    figsize : tuple, default (12, 4)
        Tamanho da figura.
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)

    plot_acf(serie.dropna(), lags=lags, ax=axes[0])
    axes[0].set_title("Função de Autocorrelação (ACF)")

    plot_pacf(serie.dropna(), lags=lags, ax=axes[1], method="ywm")
    axes[1].set_title("Função de Autocorrelação Parcial (PACF)")

    fig.tight_layout()
    plt.show()
