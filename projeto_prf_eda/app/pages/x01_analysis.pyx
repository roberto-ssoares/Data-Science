import streamlit as st
import duckdb
import pandas as pd
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

# Configuração da Página
st.set_page_config(page_title="Analytics Dashboard", page_icon="📊", layout="wide")

# Caminhos
BASE_DIR = Path(__file__).resolve().parents[2]
PARQUET_PATH = BASE_DIR / "data" / "01-processed" / "acidentes.parquet"


@st.cache_data
def load_data():
    # Usando DuckDB para ler o parquet de forma ultra rápida
    con = duckdb.connect()
    df = con.execute(f"SELECT * FROM read_parquet('{PARQUET_PATH}')").df()
    return df


def main():
    st.title("📊 Análise de Acidentes PRF - 2023")

    if not PARQUET_PATH.exists():
        st.error(
            "❌ Arquivo de dados não encontrado. Por favor, execute o pipeline de ingestão primeiro."
        )
        return

    df = load_data()

    # Sidebar Filtros
    st.sidebar.header("Filtros")
    ufs = st.sidebar.multiselect(
        "Selecione o Estado (UF)", options=sorted(df["uf"].unique()), default=[]
    )

    filtered_df = df if not ufs else df[df["uf"].isin(ufs)]

    # KPIs Rápidos
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total de Acidentes", len(filtered_df))
    m2.metric("Estados Atendidos", filtered_df["uf"].nunique())
    m3.metric(
        "Causa Top 1",
        filtered_df["causa_acidente"].mode()[0] if not filtered_df.empty else "N/A",
    )
    total_acidentes = len(filtered_df)
    taxa_letalidade = (
        filtered_df["mortos"].sum() / total_acidentes * 100
        if total_acidentes > 0
        else 0
    )
    m4.metric("Taxa de Letalidade", f"{taxa_letalidade:.2f}%")

    st.markdown("---")

    # Gráficos
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Top 10 Causas de Acidentes")
        causas = filtered_df["causa_acidente"].value_counts().head(10).reset_index()
        fig_causas = px.bar(
            causas,
            x="count",
            y="causa_acidente",
            orientation="h",
            color="count",
            color_continuous_scale="Viridis",
            template="plotly_dark",
        )
        st.plotly_chart(fig_causas, use_container_width=True)

    with col_right:
        st.subheader("Acidentes por Dia da Semana")
        dias = filtered_df["dia_semana"].value_counts().reset_index()
        fig_dias = px.pie(
            dias, values="count", names="dia_semana", hole=0.4, template="plotly_dark"
        )
        st.plotly_chart(fig_dias, use_container_width=True)

    st.markdown("---")

    # Gráfico de Linha: Ocorrências ao Longo do Tempo por Estado
    st.subheader("📈 Ocorrências ao Longo do Tempo por Estado")
    st.caption(
        "Evolução mensal do total de acidentes registrados, segmentada por Unidade Federativa."
    )

    timeline_df = filtered_df.copy()
    timeline_df["data_inversa"] = pd.to_datetime(
        timeline_df["data_inversa"], errors="coerce"
    )
    timeline_df = timeline_df.dropna(subset=["data_inversa"])
    # Agrupar por mês e UF
    timeline_df["mes"] = timeline_df["data_inversa"].dt.to_period("M").dt.to_timestamp()
    time_series = (
        timeline_df.groupby(["mes", "uf"]).size().reset_index(name="ocorrencias")
    )
    fig_timeline = px.line(
        time_series,
        x="mes",
        y="ocorrencias",
        color="uf",
        markers=True,
        labels={
            "mes": "Mês",
            "ocorrencias": "Total de Ocorrências",
            "uf": "Estado (UF)",
        },
        template="plotly_dark",
    )
    fig_timeline.update_layout(
        xaxis_title="Período",
        yaxis_title="Total de Ocorrências",
        legend_title="Estado (UF)",
        hovermode="x unified",
    )
    st.plotly_chart(fig_timeline, use_container_width=True)

    st.markdown("---")
    st.subheader("Visualização Geográfica (Top 500 ocorrencias)")
    # Nota: Arquivo da PRF tem latitude/longitude. Vamos filtrar para exibir.
    map_data = filtered_df.dropna(subset=["latitude", "longitude"]).head(500)
    
    # Converter lat/long para float (PRF às vezes usa ponto/vírgula inconsistente)
    #map_data["latitude"] = map_data["latitude"].str.replace(",", ".").astype(float)
    map_data["latitude"] = pd.to_numeric(
    map_data["latitude"].astype(str).str.replace(",", ".", regex=False),
    errors="coerce"
    )
    #map_data["longitude"] = map_data["longitude"].str.replace(",", ".").astype(float)
    map_data["longitude"] = pd.to_numeric(
        map_data["longitude"].astype(str).str.replace(",", ".", regex=False),
        errors="coerce"
    )

    map_data = map_data.dropna(subset=["latitude", "longitude"])
    map_data = map_data[
        map_data["latitude"].between(-35, 10) &
        map_data["longitude"].between(-75, -30)
    ]

    st.map(map_data[["latitude", "longitude"]])

    st.markdown("---")

    # === INSIGHT 1: Severidade por Tipo de Acidente ===
    st.subheader("⚠️ Severidade por Tipo de Acidente")
    st.caption(
        "Proporção de vítimas (ilesas, feridas, fatais) para cada tipo de acidente. "
        "Tipos com maior proporção de faixas vermelhas exigem atenção prioritária."
    )
    sev_cols = ["tipo_acidente", "ilesos", "feridos", "mortos"]
    sev_df = filtered_df[sev_cols].copy()
    sev_agg = (
        sev_df.groupby("tipo_acidente")[["ilesos", "feridos", "mortos"]]
        .sum()
        .reset_index()
    )
    sev_agg = sev_agg.sort_values("mortos", ascending=False).head(12)
    fig_sev = go.Figure()
    fig_sev.add_bar(
        name="Ilesos",
        x=sev_agg["tipo_acidente"],
        y=sev_agg["ilesos"],
        marker_color="#4CAF50",
    )
    fig_sev.add_bar(
        name="Feridos",
        x=sev_agg["tipo_acidente"],
        y=sev_agg["feridos"],
        marker_color="#FFC107",
    )
    fig_sev.add_bar(
        name="Mortos",
        x=sev_agg["tipo_acidente"],
        y=sev_agg["mortos"],
        marker_color="#F44336",
    )
    fig_sev.update_layout(
        barmode="stack",
        template="plotly_dark",
        xaxis_tickangle=-30,
        legend_title="Classificação",
        hovermode="x unified",
        xaxis_title="Tipo de Acidente",
        yaxis_title="Número de Envolvidos",
    )
    st.plotly_chart(fig_sev, use_container_width=True)

    st.markdown("---")

    # === INSIGHT 2: Heatmap Temporal (Dia da Semana x Hora) ===
    st.subheader("🕐 Janelas Críticas: Dia da Semana × Hora do Dia")
    st.caption(
        "Concentrações de acidentes por período. Áreas mais claras indicam maior número de ocorrências "
        "e devem guiar o planejamento de fiscalização."
    )
    heat_df = filtered_df.copy()
    heat_df["hora"] = pd.to_datetime(
        heat_df["horario"], format="%H:%M:%S", errors="coerce"
    ).dt.hour
    heat_df = heat_df.dropna(subset=["hora"])
    dias_ordem = [
        "segunda-feira",
        "terça-feira",
        "quarta-feira",
        "quinta-feira",
        "sexta-feira",
        "sábado",
        "domingo",
    ]
    heat_pivot = (
        heat_df.groupby(["dia_semana", "hora"])
        .size()
        .reset_index(name="ocorrencias")
        .pivot(index="dia_semana", columns="hora", values="ocorrencias")
        .reindex(dias_ordem)
        .fillna(0)
    )
    fig_heat = px.imshow(
        heat_pivot,
        color_continuous_scale="YlOrRd",
        template="plotly_dark",
        labels={"x": "Hora do Dia", "y": "Dia da Semana", "color": "Ocorrências"},
        aspect="auto",
    )
    fig_heat.update_layout(
        xaxis_title="Hora do Dia (0–23h)",
        yaxis_title="Dia da Semana",
        coloraxis_colorbar_title="Ocorrências",
    )
    st.plotly_chart(fig_heat, use_container_width=True)

    st.markdown("---")

    # === INSIGHT 3: Impacto das Condições Climáticas na Letalidade ===
    st.subheader("🌧️ Condição Climática vs. Letalidade")
    st.caption(
        "Comparação entre total de acidentes e mortos por condição meteorológica. "
        "A taxa de letalidade (%) revela quais condições são mais perigosas — não apenas mais frequentes."
    )
    clima_df = (
        filtered_df.groupby("condicao_metereologica")
        .agg(acidentes=("id", "count"), mortos=("mortos", "sum"))
        .reset_index()
    )
    clima_df["letalidade_pct"] = (
        clima_df["mortos"] / clima_df["acidentes"] * 100
    ).round(2)
    clima_df = clima_df[clima_df["condicao_metereologica"] != "Ignorado"].sort_values(
        "letalidade_pct", ascending=False
    )
    fig_clima = px.bar(
        clima_df,
        x="condicao_metereologica",
        y="letalidade_pct",
        color="letalidade_pct",
        color_continuous_scale="Reds",
        labels={
            "condicao_metereologica": "Condição Climática",
            "letalidade_pct": "Letalidade (%)",
        },
        hover_data={"acidentes": True, "mortos": True},
        template="plotly_dark",
    )
    fig_clima.update_layout(
        xaxis_title="Condição Climática",
        yaxis_title="Taxa de Letalidade (%)",
        coloraxis_showscale=False,
    )
    st.plotly_chart(fig_clima, use_container_width=True)


if __name__ == "__main__":
    main()
