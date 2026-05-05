import sys
from pathlib import Path

# Garantir acesso à raiz do projeto
ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import duckdb
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pydeck as pdk
import streamlit as st

from src.pipeline.ingestion import run_ingestion, needs_rebuild
from src.database.tasks_repo import create_task


# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parents[2]
PARQUET_PATH = BASE_DIR / "data" / "01-processed" / "acidentes.parquet"


# =========================================================
# CARGA DE DADOS
# =========================================================

@st.cache_data
def load_data() -> pd.DataFrame:
    if not PARQUET_PATH.exists() or needs_rebuild():
        run_ingestion()

    con = duckdb.connect()

    try:
        df = con.execute(
            f"SELECT * FROM read_parquet('{PARQUET_PATH}')"
        ).df()
        return df
    finally:
        con.close()


# =========================================================
# HELPERS
# =========================================================

def prepare_map_data(df: pd.DataFrame) -> pd.DataFrame:
    map_data = df.dropna(subset=["latitude", "longitude"]).copy()

    map_data["latitude"] = pd.to_numeric(map_data["latitude"], errors="coerce")
    map_data["longitude"] = pd.to_numeric(map_data["longitude"], errors="coerce")

    map_data = map_data.dropna(subset=["latitude", "longitude"])

    map_data = map_data[
        map_data["latitude"].between(-35, 10)
        & map_data["longitude"].between(-75, -30)
    ].copy()

    for col in ["br", "km", "municipio", "uf", "causa_acidente"]:
        if col not in map_data.columns:
            map_data[col] = None

    return map_data.head(500)


def render_map(map_data: pd.DataFrame):
    if map_data.empty:
        st.info("Sem dados geográficos válidos para exibir no mapa.")
        return None

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=map_data,
        get_position="[longitude, latitude]",
        get_radius=800,
        get_fill_color="[255, 80, 80, 180]",
        pickable=True,
    )

    view = pdk.ViewState(
        latitude=map_data["latitude"].mean(),
        longitude=map_data["longitude"].mean(),
        zoom=4,
    )

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view,
        tooltip={
            "html": """
                <b>Rodovia:</b> {br}<br/>
                <b>KM:</b> {km}<br/>
                <b>Município:</b> {municipio}<br/>
                <b>UF:</b> {uf}<br/>
                <b>Causa:</b> {causa_acidente}
            """
        },
    )

    event = st.pydeck_chart(
        deck,
        use_container_width=True,
        on_select="rerun",
        selection_mode="single-object",
    )

    return event


# =========================================================
# MAIN
# =========================================================

def main():
    st.title("📊 Análise de Acidentes PRF")

    try:
        df = load_data()
    except FileNotFoundError as e:
        st.error(f"❌ {e}")
        return
    except Exception as e:
        st.error(f"❌ Erro ao carregar os dados: {e}")
        return

    if df.empty:
        st.warning("Dataset vazio.")
        return

    # -----------------------------------------------------
    # PADRONIZAÇÕES
    # -----------------------------------------------------
    if "data_inversa" in df.columns:
        df["data_inversa"] = pd.to_datetime(df["data_inversa"], errors="coerce")

    if "horario" in df.columns:
        df["hora"] = pd.to_datetime(
            df["horario"], format="%H:%M:%S", errors="coerce"
        ).dt.hour

    # -----------------------------------------------------
    # SIDEBAR
    # -----------------------------------------------------
    st.sidebar.header("Filtros")

    ufs = []
    if "uf" in df.columns:
        ufs = st.sidebar.multiselect(
            "Estado (UF)",
            sorted(df["uf"].dropna().unique()),
        )

    anos = []
    if "ano" in df.columns:
        anos_disponiveis = sorted(df["ano"].dropna().unique().tolist())
        anos = st.sidebar.multiselect(
            "Ano",
            anos_disponiveis,
            default=anos_disponiveis if len(anos_disponiveis) == 1 else [],
        )

    filtered_df = df.copy()

    if ufs:
        filtered_df = filtered_df[filtered_df["uf"].isin(ufs)]

    if anos:
        filtered_df = filtered_df[filtered_df["ano"].isin(anos)]

    if filtered_df.empty:
        st.warning("Nenhum registro encontrado com os filtros selecionados.")
        return

    # -----------------------------------------------------
    # KPIs
    # -----------------------------------------------------
    total_acidentes = len(filtered_df)
    estados_atendidos = filtered_df["uf"].nunique() if "uf" in filtered_df.columns else 0
    causa_top_1 = (
        filtered_df["causa_acidente"].mode()[0]
        if "causa_acidente" in filtered_df.columns and not filtered_df.empty
        else "N/A"
    )
    taxa_letalidade = (
        filtered_df["mortos"].sum() / total_acidentes * 100
        if "mortos" in filtered_df.columns and total_acidentes > 0
        else 0
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total de Acidentes", total_acidentes)
    c2.metric("Estados Atendidos", estados_atendidos)
    c3.metric("Causa Top 1", causa_top_1)
    c4.metric("Taxa de Letalidade", f"{taxa_letalidade:.2f}%")

    st.divider()

    # -----------------------------------------------------
    # TOP CAUSAS
    # -----------------------------------------------------
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Top 10 Causas de Acidentes")

        causas = (
            filtered_df["causa_acidente"]
            .value_counts()
            .head(10)
            .reset_index()
        )
        causas.columns = ["causa_acidente", "count"]

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

    # -----------------------------------------------------
    # DIA DA SEMANA
    # -----------------------------------------------------
    with col_right:
        st.subheader("Acidentes por Dia da Semana")

        dias = filtered_df["dia_semana"].value_counts().reset_index()
        dias.columns = ["dia_semana", "count"]

        fig_dias = px.pie(
            dias,
            values="count",
            names="dia_semana",
            hole=0.4,
            template="plotly_dark",
        )
        st.plotly_chart(fig_dias, use_container_width=True)

    st.divider()

    # -----------------------------------------------------
    # EVOLUÇÃO MENSAL
    # -----------------------------------------------------
    st.subheader("📈 Ocorrências ao Longo do Tempo por Estado")
    st.caption(
        "Evolução mensal do total de acidentes registrados, segmentada por Unidade Federativa."
    )

    timeline_df = filtered_df.dropna(subset=["data_inversa"]).copy()
    timeline_df["mes"] = timeline_df["data_inversa"].dt.to_period("M").dt.to_timestamp()

    time_series = (
        timeline_df.groupby(["mes", "uf"])
        .size()
        .reset_index(name="ocorrencias")
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

    st.divider()

    # -----------------------------------------------------
    # MAPA
    # -----------------------------------------------------
    st.subheader("🗺️ Visualização Geográfica (Top 500 ocorrências)")
    st.caption(
        "Passe o mouse sobre o ponto para ver Rodovia e KM. Clique no ponto para criar uma tarefa."
    )

    map_data = prepare_map_data(filtered_df)
    event = render_map(map_data)

    if event and "selection" in event:
        selected_objects = event["selection"].get("objects")

        if selected_objects:
            selected = selected_objects[0]

            br = selected.get("br")
            km = selected.get("km")
            municipio = selected.get("municipio")
            uf = selected.get("uf")
            latitude = selected.get("latitude")
            longitude = selected.get("longitude")

            st.success(f"Trecho selecionado: BR {br} | KM {km}")

            titulo_sugerido = f"Intervenção BR {br} KM {km}"
            descricao_sugerida = "Trecho identificado como crítico no dashboard de acidentes."

            if st.button("Criar tarefa para este ponto"):
                create_task(
                    titulo=titulo_sugerido,
                    descricao=descricao_sugerida,
                    prioridade="Alta",
                    status="Pendente",
                    br=br,
                    km=km,
                    municipio=municipio,
                    uf=uf,
                    latitude=latitude,
                    longitude=longitude,
                )
                st.success("Tarefa criada com sucesso!")

    st.divider()

    # -----------------------------------------------------
    # SEVERIDADE POR TIPO
    # -----------------------------------------------------
    st.subheader("⚠️ Severidade por Tipo de Acidente")
    st.caption(
        "Proporção de vítimas por tipo de acidente. Tipos com maior concentração de mortos merecem atenção prioritária."
    )

    sev_cols = ["tipo_acidente", "ilesos", "feridos", "mortos"]
    if all(col in filtered_df.columns for col in sev_cols):
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
            xaxis_tickangle=-35,
            legend_title="Classificação",
            hovermode="x unified",
            xaxis_title="Tipo de Acidente",
            yaxis_title="Número de Envolvidos",
        )
        st.plotly_chart(fig_sev, use_container_width=True)

    st.divider()

    # -----------------------------------------------------
    # HEATMAP TEMPORAL
    # -----------------------------------------------------
    st.subheader("🕐 Janelas Críticas: Dia da Semana × Hora do Dia")
    st.caption(
        "Áreas mais intensas indicam concentração de acidentes e ajudam a orientar fiscalização."
    )

    if "dia_semana" in filtered_df.columns and "hora" in filtered_df.columns:
        heat_df = filtered_df.dropna(subset=["hora"]).copy()

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

    st.divider()

    # -----------------------------------------------------
    # LETALIDADE POR CLIMA
    # -----------------------------------------------------
    st.subheader("🌧️ Condição Climática vs. Letalidade")
    st.caption(
        "A taxa de letalidade ajuda a entender quais condições climáticas são mais perigosas, e não apenas mais frequentes."
    )

    if all(col in filtered_df.columns for col in ["condicao_metereologica", "id", "mortos"]):
        clima_df = (
            filtered_df.groupby("condicao_metereologica")
            .agg(acidentes=("id", "count"), mortos=("mortos", "sum"))
            .reset_index()
        )

        clima_df["letalidade_pct"] = (
            clima_df["mortos"] / clima_df["acidentes"] * 100
        ).round(2)

        clima_df = clima_df[
            clima_df["condicao_metereologica"] != "Ignorado"
        ].sort_values("letalidade_pct", ascending=False)

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
    