# Projeto 2 - Análise e Visualização de Dados de Vendas ao Longo do Tempo com PySpark
# Script de Visualização (Histórico + Previsão)

import os
import pandas as pd
import matplotlib.pyplot as plt

# Diretório dos CSVs
diretorio = r"D:/_DS-Projects/Data-Science/Modelagem-Series-Temporais-PySpark/datasets/previsoesdeploy"

# Lista CSVs
csvs = [f for f in os.listdir(diretorio) if f.lower().endswith(".csv")]
if not csvs:
    raise FileNotFoundError("Nenhum arquivo CSV encontrado no diretório especificado.")

# Carrega todos os CSVs e identifica qual é histórico e qual é previsão
df_hist = None
df_pred = None

for f in csvs:
    path = os.path.join(diretorio, f)
    df = pd.read_csv(path)

    cols = set(df.columns.str.strip())  # normaliza espaços
    if "Date" in cols and "Sales" in cols and df_hist is None:
        df_hist = df.copy()
        df_hist["__source__"] = f

    if "Date" in cols and "prediction" in cols and df_pred is None:
        df_pred = df.copy()
        df_pred["__source__"] = f

if df_hist is None:
    raise ValueError("Não encontrei um CSV com colunas ['Date', 'Sales'] (histórico) no diretório.")
if df_pred is None:
    raise ValueError("Não encontrei um CSV com colunas ['Date', 'prediction'] (previsão) no diretório.")

# --- Conversão de datas (funciona bem com 'YYYY-MM' do seu print) ---
def parse_date(s: pd.Series) -> pd.Series:
    s = s.astype(str).str.strip()
    # Se vier no formato YYYY-MM, adiciona dia 01 para ficar uma data completa
    s = s.where(~s.str.match(r"^\d{4}-\d{2}$"), s + "-01")
    return pd.to_datetime(s, errors="coerce")

df_hist["Date"] = parse_date(df_hist["Date"])
df_pred["Date"] = parse_date(df_pred["Date"])

# Remove linhas com Date inválida (se existir)
df_hist = df_hist.dropna(subset=["Date"])
df_pred = df_pred.dropna(subset=["Date"])

# Seleciona só o necessário e remove duplicadas por Date (se houver)
df_hist = df_hist[["Date", "Sales"]].drop_duplicates(subset=["Date"]).sort_values("Date")
df_pred = df_pred[["Date", "prediction"]].drop_duplicates(subset=["Date"]).sort_values("Date")

# Merge por Date (outer para aparecer tudo: histórico e/ou previsão)
df_plot = pd.merge(df_hist, df_pred, on="Date", how="outer").sort_values("Date")

# --- Plot ---
plt.figure(figsize=(12, 6))

# Histórico
plt.plot(df_plot["Date"], df_plot["Sales"], marker="o", linestyle="-", label="Histórico (Sales)")

# Previsão
plt.plot(df_plot["Date"], df_plot["prediction"], marker="o", linestyle="--", label="Previsão (prediction)")

plt.title("Vendas ao Longo do Tempo — Histórico vs Previsão")
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.grid(True, alpha=0.3)
plt.legend()

# Se tiver muitos pontos, melhora a leitura do eixo X
plt.xticks(rotation=45)

# Salva o gráfico
saida = os.path.join(diretorio, "projeto2_hist_vs_pred.png")
plt.tight_layout()
plt.savefig(saida, dpi=150)

plt.show()

print("Histórico veio de:", "dataset com Sales (detectado automaticamente)")
print("Previsão veio de:", "dataset com prediction (detectado automaticamente)")
print("Imagem salva em:", saida)