import sys
import streamlit as st
from pathlib import Path
from src.database.init_db import init_db

# Garantir que a raiz do projeto esteja no sys.path
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

# Inicializa banco de dados ao subir o app
init_db()

st.set_page_config(
    page_title="PRF Analytics & Action",
    page_icon="🚔",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS customizado
st.markdown(
    """
    <style>
        .main {
            background-color: #0e1117;
        }

        .stMetric {
            background-color: #1e2130;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #3e4451;
        }

        h1, h2, h3 {
            color: #ffffff;
            font-family: 'Inter', sans-serif;
        }

        .stSidebar {
            background-color: #161b22;
        }

        div[data-testid="stButton"] > button {
            width: 100%;
            border-radius: 8px;
            font-weight: 600;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    st.title("🚔 PRF Data Analytics & Action Plan")
    st.markdown("---")

    st.markdown(
        """
        Plataforma interativa para **análise de acidentes rodoviários** e **gestão de ações operacionais**,
        conectando inteligência analítica a intervenções práticas em pontos críticos da malha viária.
        """
    )

    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Analytics Dashboard")
        st.info(
            "Explore os dados de acidentes, identifique pontos críticos e gere insights geográficos e temporais."
        )

        if st.button("Ir para Analytics"):
            st.switch_page("pages/01_analysis.py")

    with col2:
        st.subheader("📋 Gestor de Tarefas")
        st.success(
            "Transforme insights em ação. Crie, priorize e acompanhe planos de intervenção baseados nos dados."
        )

        if st.button("Ir para Tarefas"):
            st.switch_page("pages/02_tasks.py")

    st.markdown("---")

    st.markdown("### 🛠️ Stack do Projeto")
    st.code(
        "Python + Polars + DuckDB + SQLite + Streamlit + Plotly + PyDeck",
        language="text",
    )

    st.markdown("### 🧭 Fluxo do Sistema")
    st.markdown(
        """
        - **Ingestão** de arquivos CSV da PRF  
        - **Tratamento e consolidação** em Parquet  
        - **Análise interativa** com dashboard  
        - **Seleção de pontos críticos** no mapa  
        - **Criação de tarefas operacionais**
        """
    )


if __name__ == "__main__":
    main()