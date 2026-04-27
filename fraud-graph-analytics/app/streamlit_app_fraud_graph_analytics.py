from __future__ import annotations

"""
Fraud Graph Analytics — Streamlit Investigative App

Modos de uso:

1. App Streamlit:
   streamlit run app/streamlit_app.py

2. Diagnóstico/testes sem Streamlit:
   python app/streamlit_app.py --self-test
   python app/streamlit_app.py --diagnose

3. Ambientes interativos/sandbox/notebook:
   O arquivo não depende obrigatoriamente de __file__ e não encerra com erro
   quando Streamlit não está instalado. Ele imprime instruções e finaliza com
   código 0, para não quebrar execuções diagnósticas.
"""

from pathlib import Path
import argparse
import sys
from typing import Any

import pandas as pd

try:
    import plotly.express as px
except ModuleNotFoundError:  # pragma: no cover - fallback de ambiente
    px = None

try:
    import streamlit as st
except ModuleNotFoundError:  # pragma: no cover - fallback de ambiente
    st = None


# ============================================================
# Fraud Graph Analytics — Streamlit Investigative App
# ============================================================


def find_project_root(start_path: Path | None = None) -> Path:
    """Find project root from a starting path.

    Works when executed as a regular Python file, by Streamlit, or in
    interactive/sandbox contexts where __file__ may be unavailable.
    """
    start = (start_path or Path.cwd()).resolve()

    if start.is_file():
        start = start.parent

    candidates = [start, *start.parents]

    for candidate in candidates:
        has_project_markers = (
            (candidate / "pyproject.toml").exists()
            or (candidate / "notebooks").exists()
            or (candidate / "app").exists()
        )
        has_expected_dirs = (
            (candidate / "data").exists()
            or (candidate / "docs").exists()
            or (candidate / "artifacts").exists()
        )

        if has_project_markers and has_expected_dirs:
            return candidate

    return start


def get_project_root() -> Path:
    """Return project root regardless of execution context."""
    file_value = globals().get("__file__")

    if file_value:
        current = Path(file_value).resolve()
        if current.parent.name == "app":
            return current.parents[1]
        return find_project_root(current)

    return find_project_root(Path.cwd())


PROJECT_ROOT = get_project_root()
DATA_DIR = PROJECT_ROOT / "data"
GOLD_DIR = DATA_DIR / "03-gold"
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
REPORTS_DIR = ARTIFACTS_DIR / "reports"
DOCS_DIR = PROJECT_ROOT / "docs"


# -----------------------------
# Formatting helpers
# -----------------------------


def format_number(value: float | int | None) -> str:
    if value is None or pd.isna(value):
        return "0"
    if abs(float(value)) >= 1_000_000:
        return f"{value / 1_000_000:,.1f}M".replace(",", ".")
    if abs(float(value)) >= 1_000:
        return f"{value / 1_000:,.1f}k".replace(",", ".")
    return f"{value:,.0f}".replace(",", ".")


def format_currency(value: float | int | None) -> str:
    if value is None or pd.isna(value):
        return "R$ 0,00"
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def format_percent(value: float | int | None) -> str:
    if value is None or pd.isna(value):
        return "0,00%"
    return f"{value:.2%}".replace(".", ",")


def risk_color(risk_band: str) -> str:
    colors = {
        "baixo": "#22c55e",
        "medio": "#38bdf8",
        "médio": "#38bdf8",
        "alto": "#f97316",
        "critico": "#ef4444",
        "crítico": "#ef4444",
    }
    return colors.get(str(risk_band).lower(), "#94a3b8")


# -----------------------------
# Data loading helpers
# -----------------------------


def load_parquet_or_empty(path: Path) -> pd.DataFrame:
    if path.exists():
        return pd.read_parquet(path)
    return pd.DataFrame()


def load_csv_or_empty(path: Path) -> pd.DataFrame:
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()


def load_data_uncached() -> dict[str, pd.DataFrame]:
    """Load generated outputs from notebooks.

    Parquet files under data/03-gold are preferred. If they are not available,
    the app falls back to versionable CSV samples under artifacts/reports.
    """
    final_score = load_parquet_or_empty(GOLD_DIR / "final_fraud_risk_score.parquet")
    final_alerts = load_parquet_or_empty(GOLD_DIR / "final_fraud_alerts.parquet")
    entity_ranking = load_parquet_or_empty(GOLD_DIR / "graph_entity_ranking.parquet")
    community_risk = load_parquet_or_empty(GOLD_DIR / "community_risk_summary.parquet")

    if final_alerts.empty:
        final_alerts = load_csv_or_empty(REPORTS_DIR / "final_fraud_alerts_sample.csv")

    if entity_ranking.empty:
        entity_ranking = load_csv_or_empty(REPORTS_DIR / "graph_entity_ranking_top.csv")

    if community_risk.empty:
        community_risk = load_csv_or_empty(REPORTS_DIR / "community_risk_summary_top.csv")

    for df in [final_score, final_alerts]:
        if not df.empty and "data_hora" in df.columns:
            df["data_hora"] = pd.to_datetime(df["data_hora"], errors="coerce")

    return {
        "final_score": final_score,
        "final_alerts": final_alerts,
        "entity_ranking": entity_ranking,
        "community_risk": community_risk,
    }


if st is not None:
    load_data = st.cache_data(show_spinner=True)(load_data_uncached)
else:
    load_data = load_data_uncached


# -----------------------------
# Business helpers
# -----------------------------


def build_risk_summary(score_df: pd.DataFrame) -> pd.DataFrame:
    """Build risk-band summary safely for app and tests."""
    if score_df.empty or "final_risk_band" not in score_df.columns:
        return pd.DataFrame()

    required_columns = {"transacao_id", "fraud_risk_score"}
    if not required_columns.issubset(score_df.columns):
        return pd.DataFrame()

    aggregations: dict[str, tuple[str, str] | tuple[str, Any]] = {
        "qtd_transacoes": ("transacao_id", "count"),
        "score_medio": ("fraud_risk_score", "mean"),
    }

    if "is_fraud" in score_df.columns:
        aggregations["taxa_fraude_sintetica"] = ("is_fraud", "mean")

    return score_df.groupby("final_risk_band").agg(**aggregations).reset_index()


def build_scenario_score_summary(score_df: pd.DataFrame) -> pd.DataFrame:
    """Build scenario-level score summary safely for app and tests."""
    if score_df.empty or "fraud_scenario" not in score_df.columns:
        return pd.DataFrame()

    required_columns = {"transacao_id", "fraud_risk_score"}
    if not required_columns.issubset(score_df.columns):
        return pd.DataFrame()

    aggregations: dict[str, tuple[str, str] | tuple[str, Any]] = {
        "qtd_transacoes": ("transacao_id", "count"),
        "score_medio": ("fraud_risk_score", "mean"),
        "score_p95": ("fraud_risk_score", lambda x: x.quantile(0.95)),
    }

    if "valor" in score_df.columns:
        aggregations["valor_medio"] = ("valor", "mean")

    if "is_fraud" in score_df.columns:
        aggregations["taxa_fraude_sintetica"] = ("is_fraud", "mean")

    return (
        score_df.groupby("fraud_scenario")
        .agg(**aggregations)
        .reset_index()
        .sort_values("score_medio", ascending=False)
    )


def select_existing_columns(df: pd.DataFrame, columns: list[str]) -> list[str]:
    return [col for col in columns if col in df.columns]


def dependency_status() -> dict[str, str]:
    return {
        "streamlit": "available" if st is not None else "missing",
        "plotly": "available" if px is not None else "missing",
        "pandas": "available",
    }


def installation_message() -> str:
    return """
Streamlit não está instalado ou este arquivo foi executado fora do comando streamlit.

Para executar o app localmente no projeto:

    uv add streamlit plotly
    streamlit run app/streamlit_app.py

Alternativa com pip:

    pip install streamlit plotly
    streamlit run app/streamlit_app.py

Para validar apenas as funções auxiliares sem Streamlit:

    python app/streamlit_app.py --self-test

Para ver diagnóstico do ambiente:

    python app/streamlit_app.py --diagnose
""".strip()


def run_diagnostics() -> None:
    print("Fraud Graph Analytics — Environment Diagnostics")
    print(f"PROJECT_ROOT: {PROJECT_ROOT}")
    print(f"GOLD_DIR: {GOLD_DIR}")
    print(f"REPORTS_DIR: {REPORTS_DIR}")
    print("Dependencies:")
    for package, status in dependency_status().items():
        print(f"- {package}: {status}")

    data = load_data_uncached()
    print("Artifacts:")
    for name, df in data.items():
        print(f"- {name}: shape={df.shape}")

    if st is None:
        print("\n" + installation_message())


def run_self_tests() -> None:
    """Minimal tests for helper functions.

    These tests intentionally avoid Streamlit so they can run in simple Python environments.
    """
    assert format_number(1_500) == "1.5k"
    assert format_number(2_500_000) == "2.5M"
    assert format_currency(1234.5) == "R$ 1.234,50"
    assert format_percent(0.1234) == "12,34%"
    assert risk_color("critico") == "#ef4444"
    assert risk_color("desconhecido") == "#94a3b8"

    sample = pd.DataFrame(
        {
            "transacao_id": ["TX1", "TX2", "TX3"],
            "final_risk_band": ["alto", "baixo", "alto"],
            "fraud_risk_score": [80.0, 10.0, 70.0],
            "is_fraud": [1, 0, 1],
            "fraud_scenario": ["shared_device_ring", "normal", "shared_device_ring"],
            "valor": [1000.0, 50.0, 800.0],
        }
    )

    risk_summary = build_risk_summary(sample)
    assert set(risk_summary["final_risk_band"]) == {"alto", "baixo"}
    assert risk_summary.loc[risk_summary["final_risk_band"] == "alto", "qtd_transacoes"].iloc[0] == 2

    scenario_summary = build_scenario_score_summary(sample)
    assert scenario_summary.iloc[0]["fraud_scenario"] == "shared_device_ring"
    assert select_existing_columns(sample, ["transacao_id", "missing_col"]) == ["transacao_id"]

    cwd_root = find_project_root(Path.cwd())
    assert isinstance(cwd_root, Path)
    assert cwd_root.is_absolute()

    project_root = get_project_root()
    assert isinstance(project_root, Path)
    assert project_root.is_absolute()

    minimal_df = pd.DataFrame({"final_risk_band": ["alto"]})
    assert build_risk_summary(minimal_df).empty

    minimal_scenario_df = pd.DataFrame({"fraud_scenario": ["normal"]})
    assert build_scenario_score_summary(minimal_scenario_df).empty

    status = dependency_status()
    assert status["pandas"] == "available"
    assert status["streamlit"] in {"available", "missing"}
    assert status["plotly"] in {"available", "missing"}

    msg = installation_message()
    assert "streamlit run app/streamlit_app.py" in msg
    assert "--self-test" in msg

    print("Self-tests OK: helper functions are working.")


# -----------------------------
# Streamlit UI helpers
# -----------------------------


def streamlit_available() -> bool:
    return st is not None


def plotly_available() -> bool:
    return px is not None


def show_missing_streamlit_message() -> None:
    """Print a friendly message without raising SystemExit.

    Important: this function intentionally does not raise. Some automated
    environments execute the file directly and treat SystemExit as an error.
    """
    print(installation_message())


def show_missing_plotly_message() -> None:
    print("Plotly não está instalado. Instale com: uv add plotly")


def filter_alerts(df: pd.DataFrame) -> pd.DataFrame:
    if st is None:
        return df

    if df.empty:
        return df

    filtered = df.copy()

    with st.sidebar:
        st.header("Filtros")

        if "final_risk_band" in filtered.columns:
            risk_options = sorted(filtered["final_risk_band"].dropna().unique().tolist())
            selected_risk = st.multiselect(
                "Faixa de risco final",
                options=risk_options,
                default=risk_options,
            )
            if selected_risk:
                filtered = filtered[filtered["final_risk_band"].isin(selected_risk)]

        if "fraud_scenario" in filtered.columns:
            scenario_options = sorted(filtered["fraud_scenario"].dropna().unique().tolist())
            selected_scenarios = st.multiselect(
                "Cenário sintético",
                options=scenario_options,
                default=scenario_options,
            )
            if selected_scenarios:
                filtered = filtered[filtered["fraud_scenario"].isin(selected_scenarios)]

        if "tipo_transacao" in filtered.columns:
            type_options = sorted(filtered["tipo_transacao"].dropna().unique().tolist())
            selected_types = st.multiselect(
                "Tipo de transação",
                options=type_options,
                default=type_options,
            )
            if selected_types:
                filtered = filtered[filtered["tipo_transacao"].isin(selected_types)]

        if "canal" in filtered.columns:
            channel_options = sorted(filtered["canal"].dropna().unique().tolist())
            selected_channels = st.multiselect(
                "Canal",
                options=channel_options,
                default=channel_options,
            )
            if selected_channels:
                filtered = filtered[filtered["canal"].isin(selected_channels)]

        if "fraud_risk_score" in filtered.columns and not filtered["fraud_risk_score"].dropna().empty:
            min_score = float(filtered["fraud_risk_score"].min())
            max_score = float(filtered["fraud_risk_score"].max())

            if min_score == max_score:
                st.caption(f"Fraud Risk Score único nos filtros: {min_score:.2f}")
            else:
                selected_score = st.slider(
                    "Intervalo do Fraud Risk Score",
                    min_value=float(round(min_score, 2)),
                    max_value=float(round(max_score, 2)),
                    value=(float(round(min_score, 2)), float(round(max_score, 2))),
                )
                filtered = filtered[
                    filtered["fraud_risk_score"].between(selected_score[0], selected_score[1])
                ]

        top_n = st.slider("Quantidade de linhas nas tabelas", 10, 200, 50, step=10)

    return filtered.head(top_n)


# -----------------------------
# Streamlit App
# -----------------------------


def run_app() -> None:
    if not streamlit_available():
        show_missing_streamlit_message()
        return

    if not plotly_available():
        if st is not None:
            st.error("Plotly não está instalado. Instale com: uv add plotly")
            st.stop()
        show_missing_plotly_message()
        return

    st.set_page_config(
        page_title="Fraud Graph Analytics",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    data = load_data()
    final_score = data["final_score"]
    final_alerts = data["final_alerts"]
    entity_ranking = data["entity_ranking"]
    community_risk = data["community_risk"]

    with st.sidebar:
        st.title("🛡️ Fraud Graph Analytics")
        st.caption("App investigativo para alertas antifraude, grafos e explicabilidade.")

        st.divider()

        st.markdown("### Artefatos carregados")
        st.write(f"Final score: `{final_score.shape}`")
        st.write(f"Final alerts: `{final_alerts.shape}`")
        st.write(f"Entity ranking: `{entity_ranking.shape}`")
        st.write(f"Community risk: `{community_risk.shape}`")
        st.write(f"Project root: `{PROJECT_ROOT}`")

        st.divider()

    st.title("Fraud Graph Analytics")
    st.markdown(
        """
        **Prevenção a Fraudes Transacionais com Knowledge Graph, Regras Explicáveis e Graph Analytics**

        Este app consolida a camada investigativa do projeto, permitindo explorar alertas finais,
        entidades com maior risco estrutural e comunidades suspeitas. Os dados são sintéticos e foram
        criados exclusivamente para fins educacionais, analíticos e de portfólio.
        """
    )

    if final_alerts.empty and final_score.empty:
        st.error(
            "Nenhum artefato analítico foi encontrado. Execute os notebooks 01 a 06 antes de abrir o app."
        )
        st.stop()

    st.subheader("Visão executiva")

    base_for_kpis = final_score if not final_score.empty else final_alerts
    alerts_for_kpis = final_alerts

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Transações avaliadas", format_number(len(base_for_kpis)))

    with col2:
        st.metric("Alertas finais", format_number(len(alerts_for_kpis)))

    with col3:
        if not base_for_kpis.empty and "final_alert" in base_for_kpis.columns:
            st.metric("Taxa de alertas", format_percent(base_for_kpis["final_alert"].mean()))
        else:
            st.metric("Taxa de alertas", "N/D")

    with col4:
        if not alerts_for_kpis.empty and "is_fraud" in alerts_for_kpis.columns:
            st.metric("Fraude sintética nos alertas", format_percent(alerts_for_kpis["is_fraud"].mean()))
        else:
            st.metric("Fraude sintética nos alertas", "N/D")

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        if not alerts_for_kpis.empty and "valor" in alerts_for_kpis.columns:
            st.metric("Valor total alertado", format_currency(alerts_for_kpis["valor"].sum()))
        else:
            st.metric("Valor total alertado", "N/D")

    with col6:
        if not alerts_for_kpis.empty and "fraud_risk_score" in alerts_for_kpis.columns:
            st.metric("Score médio dos alertas", f"{alerts_for_kpis['fraud_risk_score'].mean():.1f}")
        else:
            st.metric("Score médio dos alertas", "N/D")

    with col7:
        if not alerts_for_kpis.empty and "conta_origem_id" in alerts_for_kpis.columns:
            st.metric("Contas alertadas", format_number(alerts_for_kpis["conta_origem_id"].nunique()))
        else:
            st.metric("Contas alertadas", "N/D")

    with col8:
        if not alerts_for_kpis.empty and "beneficiario_id" in alerts_for_kpis.columns:
            st.metric("Beneficiários alertados", format_number(alerts_for_kpis["beneficiario_id"].nunique()))
        else:
            st.metric("Beneficiários alertados", "N/D")

    st.divider()

    tab_alerts, tab_score, tab_entities, tab_communities, tab_methodology = st.tabs(
        [
            "🚨 Alertas finais",
            "📊 Score e cenários",
            "🕸️ Entidades de grafo",
            "👥 Comunidades",
            "📘 Metodologia",
        ]
    )

    with tab_alerts:
        st.subheader("Alertas finais priorizados")
        st.caption(
            "Filtros laterais são aplicados sobre a base de alertas finais. "
            "A priorização combina regras antifraude e risco estrutural de grafo."
        )

        filtered_alerts = filter_alerts(final_alerts)

        if filtered_alerts.empty:
            st.warning("Nenhum alerta encontrado para os filtros selecionados.")
        else:
            c1, c2 = st.columns([1.2, 1])

            with c1:
                if "final_risk_band" in filtered_alerts.columns:
                    risk_dist = (
                        filtered_alerts["final_risk_band"]
                        .value_counts()
                        .rename_axis("final_risk_band")
                        .reset_index(name="qtd_alertas")
                    )
                    fig = px.bar(
                        risk_dist,
                        x="final_risk_band",
                        y="qtd_alertas",
                        title="Alertas por faixa de risco",
                        labels={"final_risk_band": "Faixa", "qtd_alertas": "Alertas"},
                    )
                    st.plotly_chart(fig, use_container_width=True)

            with c2:
                if "fraud_scenario" in filtered_alerts.columns:
                    scenario_dist = (
                        filtered_alerts["fraud_scenario"]
                        .value_counts()
                        .rename_axis("fraud_scenario")
                        .reset_index(name="qtd_alertas")
                        .head(10)
                    )
                    fig = px.bar(
                        scenario_dist,
                        x="qtd_alertas",
                        y="fraud_scenario",
                        orientation="h",
                        title="Top cenários entre alertas",
                        labels={"qtd_alertas": "Alertas", "fraud_scenario": "Cenário"},
                    )
                    st.plotly_chart(fig, use_container_width=True)

            display_cols = select_existing_columns(
                filtered_alerts,
                [
                    "transacao_id",
                    "conta_origem_id",
                    "beneficiario_id",
                    "device_id",
                    "ip_id",
                    "valor",
                    "data_hora",
                    "tipo_transacao",
                    "canal",
                    "fraud_scenario",
                    "rule_score",
                    "fraud_risk_score",
                    "final_risk_band",
                    "max_entity_graph_risk_score",
                    "max_community_risk_score",
                    "final_explanation",
                ],
            )

            st.dataframe(
                filtered_alerts[display_cols],
                use_container_width=True,
                hide_index=True,
            )

            st.download_button(
                "Baixar alertas filtrados em CSV",
                data=filtered_alerts[display_cols].to_csv(index=False).encode("utf-8"),
                file_name="filtered_fraud_alerts.csv",
                mime="text/csv",
            )

            if "transacao_id" in filtered_alerts.columns:
                st.markdown("### Detalhe de uma transação")
                selected_tx = st.selectbox(
                    "Selecione uma transação para ver a explicação",
                    options=filtered_alerts["transacao_id"].dropna().astype(str).tolist(),
                )

                selected_row = filtered_alerts.loc[
                    filtered_alerts["transacao_id"].astype(str) == selected_tx
                ].head(1)

                if not selected_row.empty:
                    row = selected_row.iloc[0]
                    st.info(row.get("final_explanation", "Sem explicação disponível."))

                    detail_cols = select_existing_columns(
                        selected_row,
                        [
                            "transacao_id",
                            "valor",
                            "fraud_scenario",
                            "is_fraud",
                            "rule_score",
                            "fraud_risk_score",
                            "final_risk_band",
                            "qtd_regras_acionadas",
                            "account_graph_entity_graph_risk_score",
                            "device_graph_entity_graph_risk_score",
                            "beneficiary_graph_entity_graph_risk_score",
                            "ip_graph_entity_graph_risk_score",
                            "max_community_risk_score",
                        ],
                    )
                    st.dataframe(selected_row[detail_cols], use_container_width=True, hide_index=True)

    with tab_score:
        st.subheader("Distribuição do score final")

        if final_score.empty:
            st.warning("Base final de score não encontrada. Exibindo apenas alertas disponíveis.")
            score_df = final_alerts.copy()
        else:
            score_df = final_score.copy()

        if score_df.empty or "fraud_risk_score" not in score_df.columns:
            st.warning("Não há coluna fraud_risk_score disponível.")
        else:
            c1, c2 = st.columns(2)

            with c1:
                fig = px.histogram(
                    score_df,
                    x="fraud_risk_score",
                    nbins=40,
                    title="Distribuição do Fraud Risk Score",
                    labels={"fraud_risk_score": "Fraud Risk Score"},
                )
                st.plotly_chart(fig, use_container_width=True)

            with c2:
                risk_summary = build_risk_summary(score_df)
                if not risk_summary.empty:
                    fig = px.bar(
                        risk_summary,
                        x="final_risk_band",
                        y="score_medio",
                        title="Score médio por faixa de risco",
                        labels={"final_risk_band": "Faixa", "score_medio": "Score médio"},
                    )
                    st.plotly_chart(fig, use_container_width=True)

            scenario_score = build_scenario_score_summary(score_df)
            if not scenario_score.empty:
                st.markdown("### Score por cenário sintético")
                st.dataframe(scenario_score, use_container_width=True, hide_index=True)

                fig = px.bar(
                    scenario_score,
                    x="score_medio",
                    y="fraud_scenario",
                    orientation="h",
                    title="Score médio por cenário",
                    labels={"score_medio": "Score médio", "fraud_scenario": "Cenário"},
                )
                st.plotly_chart(fig, use_container_width=True)

    with tab_entities:
        st.subheader("Ranking de entidades por risco de grafo")

        if entity_ranking.empty:
            st.warning("Ranking de entidades não encontrado. Execute o Notebook 05.")
        else:
            entity_df = entity_ranking.copy()

            if "node_type" in entity_df.columns:
                entity_types = sorted(entity_df["node_type"].dropna().unique().tolist())
                selected_entity_types = st.multiselect(
                    "Filtrar tipo de entidade",
                    options=entity_types,
                    default=entity_types,
                )
                if selected_entity_types:
                    entity_df = entity_df[entity_df["node_type"].isin(selected_entity_types)]

            sort_col = "entity_graph_risk_score" if "entity_graph_risk_score" in entity_df.columns else entity_df.columns[0]
            entity_df = entity_df.sort_values(sort_col, ascending=False).head(100)

            c1, c2 = st.columns([1, 1])

            with c1:
                if "node_type" in entity_df.columns:
                    type_dist = (
                        entity_df["node_type"]
                        .value_counts()
                        .rename_axis("node_type")
                        .reset_index(name="qtd")
                    )
                    fig = px.pie(
                        type_dist,
                        names="node_type",
                        values="qtd",
                        title="Distribuição das entidades exibidas",
                    )
                    st.plotly_chart(fig, use_container_width=True)

            with c2:
                if {"entity_id", "entity_graph_risk_score"}.issubset(entity_df.columns):
                    top_entities_plot = entity_df.head(15).copy()
                    fig = px.bar(
                        top_entities_plot.sort_values("entity_graph_risk_score", ascending=True),
                        x="entity_graph_risk_score",
                        y="entity_id",
                        color="node_type" if "node_type" in top_entities_plot.columns else None,
                        orientation="h",
                        title="Top entidades por risco estrutural",
                        labels={
                            "entity_graph_risk_score": "Entity Graph Risk Score",
                            "entity_id": "Entidade",
                        },
                    )
                    st.plotly_chart(fig, use_container_width=True)

            display_cols = select_existing_columns(
                entity_df,
                [
                    "node_type",
                    "entity_id",
                    "degree",
                    "weighted_degree",
                    "pagerank",
                    "betweenness_approx",
                    "community_id",
                    "community_risk_score",
                    "qtd_alertas",
                    "score_max",
                    "taxa_alerta",
                    "taxa_fraude_sintetica",
                    "valor_total",
                    "entity_graph_risk_score",
                    "entity_graph_risk_band",
                ],
            )

            st.dataframe(entity_df[display_cols], use_container_width=True, hide_index=True)

    with tab_communities:
        st.subheader("Comunidades suspeitas")

        if community_risk.empty:
            st.warning("Resumo de comunidades não encontrado. Execute o Notebook 05.")
        else:
            community_df = community_risk.copy()

            numeric_cols = community_df.select_dtypes("number").columns.tolist()
            if "community_risk_score" in community_df.columns:
                score_col = "community_risk_score"
            elif numeric_cols:
                score_col = numeric_cols[0]
            else:
                score_col = community_df.columns[0]

            community_df = community_df.sort_values(score_col, ascending=False)

            c1, c2 = st.columns([1, 1])

            with c1:
                if {"community_id", score_col}.issubset(community_df.columns):
                    top_communities = community_df.head(15).copy()
                    fig = px.bar(
                        top_communities.sort_values(score_col, ascending=True),
                        x=score_col,
                        y="community_id",
                        orientation="h",
                        title="Top comunidades por risco",
                        labels={score_col: "Community Risk Score", "community_id": "Comunidade"},
                    )
                    st.plotly_chart(fig, use_container_width=True)

            with c2:
                if "community_size" in community_df.columns and score_col in community_df.columns:
                    fig = px.scatter(
                        community_df.head(100),
                        x="community_size",
                        y=score_col,
                        size="qtd_alertas" if "qtd_alertas" in community_df.columns else None,
                        title="Tamanho da comunidade vs risco",
                        labels={
                            "community_size": "Tamanho",
                            score_col: "Community Risk Score",
                        },
                    )
                    st.plotly_chart(fig, use_container_width=True)

            st.dataframe(community_df.head(100), use_container_width=True, hide_index=True)

    with tab_methodology:
        st.subheader("Metodologia do MVP")

        st.markdown(
            """
            Este app é a camada demonstrável do projeto **Fraud Graph Analytics**.

            A jornada completa é composta por:

            1. **Domain Understanding com CRISP-DM+**  
               Ontologia, Business Language Model, taxonomia de fraudes e hipóteses investigativas.

            2. **Geração de dados sintéticos**  
               Clientes, contas, transações, dispositivos, IPs, beneficiários e cenários de fraude.

            3. **EDA transacional**  
               Exploração de valores, canais, horários, beneficiários, dispositivos e contas.

            4. **Motor de regras antifraude**  
               Regras explicáveis com severidade, pontuação e justificativa.

            5. **Knowledge Graph**  
               Modelagem de contas, transações, dispositivos, IPs, beneficiários e regras.

            6. **Algoritmos de grafo**  
               Degree, PageRank, Connected Components, comunidades e Betweenness aproximado.

            7. **Fraud Risk Score final**  
               Combinação de score de regras, risco estrutural das entidades e risco de comunidade.
            """
        )

        st.markdown("### Fórmula conceitual do score")
        st.code(
            """
fraud_risk_score =
    0.45  * rule_score
  + 0.20  * account_graph_risk_score
  + 0.125 * device_graph_risk_score
  + 0.125 * beneficiary_graph_risk_score
  + 0.05  * ip_graph_risk_score
  + 0.05  * max_community_risk_score
            """.strip(),
            language="text",
        )

        st.markdown("### Observação ética")
        st.info(
            "Os dados são sintéticos e o score é heurístico. O app demonstra uma abordagem analítica "
            "para priorização investigativa, não uma solução produtiva de bloqueio automático."
        )

        st.markdown("### Links úteis")
        st.link_button(
            "Repositório no GitHub",
            "https://github.com/roberto-ssoares/Data-Science/tree/main/fraud-graph-analytics",
        )

    st.divider()
    st.caption(
        "Fraud Graph Analytics — MVP de portfólio com dados sintéticos, regras explicáveis, Graph Analytics e Streamlit."
    )


# -----------------------------
# CLI entrypoint
# -----------------------------


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Fraud Graph Analytics Streamlit app")
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run helper tests without requiring Streamlit.",
    )
    parser.add_argument(
        "--diagnose",
        action="store_true",
        help="Print environment diagnostics without requiring Streamlit.",
    )
    args = parser.parse_args(argv)

    if args.self_test:
        run_self_tests()
        return

    if args.diagnose:
        run_diagnostics()
        return

    run_app()


if __name__ == "__main__":
    main(sys.argv[1:])
