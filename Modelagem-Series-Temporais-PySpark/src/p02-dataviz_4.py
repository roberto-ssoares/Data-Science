# Projeto 2 - Visualização (Histórico + Previsão) com filtro de 12 meses e estilo executivo

import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# 1) CAMINHOS (fixos)
# ===============================
historico_csv = r"D:\_DS-Projects\Data-Science\Modelagem-Series-Temporais-PySpark\datasets\dataset.csv"
dir_previsoes = r"D:\_DS-Projects\Data-Science\Modelagem-Series-Temporais-PySpark\datasets\previsoesdeploy"

# ===============================
# 2) FUNÇÕES AUXILIARES
# ===============================
def parse_date(series: pd.Series) -> pd.Series:
    """Aceita Date como 'YYYY-MM' ou data completa; normaliza para datetime."""
    s = series.astype(str).str.strip()
    # Se vier no formato YYYY-MM, adiciona dia 01 para virar uma data válida
    s = s.where(~s.str.match(r"^\d{4}-\d{2}$"), s + "-01")
    return pd.to_datetime(s, errors="coerce")

def find_prediction_csv(folder: str) -> str:
    """Encontra o primeiro CSV no folder que contenha colunas Date e prediction."""
    p = Path(folder)
    if not p.exists():
        raise FileNotFoundError(f"Diretório de previsões não existe: {folder}")

    for f in sorted(p.glob("*.csv")):
        df = pd.read_csv(f)
        cols = set(df.columns.str.strip())
        if "Date" in cols and "prediction" in cols:
            return str(f)

    raise FileNotFoundError("Não encontrei nenhum CSV com colunas ['Date','prediction'] em previsoesdeploy.")

# ===============================
# 3) CARREGAR HISTÓRICO
# ===============================
if not Path(historico_csv).exists():
    raise FileNotFoundError(f"Arquivo histórico não encontrado: {historico_csv}")

df_hist = pd.read_csv(historico_csv)
df_hist.columns = df_hist.columns.str.strip()

# Valida colunas esperadas do histórico
if "Date" not in df_hist.columns or "Sales" not in df_hist.columns:
    raise ValueError("Histórico precisa ter colunas: 'Date' e 'Sales'.")

df_hist["Date"] = parse_date(df_hist["Date"])
df_hist = df_hist.dropna(subset=["Date"])

# Garante numérico
df_hist["Sales"] = pd.to_numeric(df_hist["Sales"], errors="coerce")

# Remove duplicadas e ordena
df_hist = (
    df_hist[["Date", "Sales"]]
    .drop_duplicates(subset=["Date"])
    .sort_values("Date")
)

# ===============================
# 4) CARREGAR PREVISÃO
# ===============================
pred_csv = find_prediction_csv(dir_previsoes)
df_pred = pd.read_csv(pred_csv)
df_pred.columns = df_pred.columns.str.strip()

df_pred["Date"] = parse_date(df_pred["Date"])
df_pred = df_pred.dropna(subset=["Date"])

df_pred["prediction"] = pd.to_numeric(df_pred["prediction"], errors="coerce")

df_pred = (
    df_pred[["Date", "prediction"]]
    .drop_duplicates(subset=["Date"])
    .sort_values("Date")
)

# ===============================
# 5) MERGE + FILTRO (12 meses antes da 1ª previsão)
# ===============================
df_plot = pd.merge(df_hist, df_pred, on="Date", how="outer").sort_values("Date")

primeira_data_pred = df_plot.loc[df_plot["prediction"].notna(), "Date"].min()
ultima_data_pred   = df_plot.loc[df_plot["prediction"].notna(), "Date"].max()

if pd.isna(primeira_data_pred):
    raise ValueError("Não consegui detectar a primeira data prevista (prediction).")

data_inicio = primeira_data_pred - pd.DateOffset(months=12)
df_plot = df_plot[df_plot["Date"] >= data_inicio].sort_values("Date")

# ===============================
# 6) PLOT com CONTINUIDADE (linha única + trecho tracejado)
# ===============================
plt.figure(figsize=(12, 6))

# Série "contínua": usa Sales quando existir; senão usa prediction
df_plot["y"] = df_plot["Sales"].combine_first(df_plot["prediction"])

# Identifica o último ponto real (Sales não-nulo) e o primeiro ponto previsto
last_real_date = df_plot.loc[df_plot["Sales"].notna(), "Date"].max()
first_pred_date = df_plot.loc[df_plot["prediction"].notna(), "Date"].min()
last_pred_date  = df_plot.loc[df_plot["prediction"].notna(), "Date"].max()

# 1) Histórico (até o último real) — linha contínua
hist_mask = df_plot["Date"] <= last_real_date
plt.plot(
    df_plot.loc[hist_mask, "Date"],
    df_plot.loc[hist_mask, "y"],
    marker="o",
    linestyle="-",
    label="Histórico (Sales)"
)

# 2) Previsão — começa no último ponto real (para dar continuidade) e segue tracejada
# Pega o último ponto real + todos os pontos previstos
pred_mask = (df_plot["Date"] >= last_real_date) & (df_plot["prediction"].notna() | (df_plot["Date"] == last_real_date))

plt.plot(
    df_plot.loc[pred_mask, "Date"],
    df_plot.loc[pred_mask, "y"],
    marker="o",
    linestyle="--",
    label="Previsão (prediction)"
)

# Linha vertical + faixa sombreada do período previsto
if pd.notna(first_pred_date):
    plt.axvline(first_pred_date, linestyle="--", alpha=0.7)
    if pd.notna(last_pred_date):
        plt.axvspan(first_pred_date, last_pred_date, alpha=0.12)

    ymax = pd.to_numeric(df_plot["y"], errors="coerce").max()
    if pd.notna(ymax):
        plt.text(first_pred_date, ymax, "Início da previsão", rotation=90,
                 va="top", ha="right", alpha=0.85)

plt.title("Vendas ao Longo do Tempo — Últimos 12 meses (Histórico) + Previsão")
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.grid(True, alpha=0.25)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Salvar + exibir
saida_png = os.path.join(dir_previsoes, "projeto2_hist12m_vs_pred_exec_continuo.png")
plt.savefig(saida_png, dpi=160)
plt.show()

print("✅ Imagem salva em:", saida_png)


# ===============================
# 7) SALVAR RESULTADO
# ===============================
saida_png = os.path.join(dir_previsoes, "projeto2_hist12m_vs_pred_exec.png")
plt.savefig(saida_png, dpi=160)
plt.show()

print("✅ Histórico:", historico_csv)
print("✅ Previsão:", pred_csv)
print("✅ Filtro aplicado a partir de:", data_inicio.date(), "(12 meses antes da 1ª previsão)")
print("✅ Imagem salva em:", saida_png)