import streamlit as st

st.set_page_config(
    page_title="PRF Analytics & Action",
    page_icon="🚔",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS para estética Premium
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
</style>
""",
    unsafe_allow_html=True,
)


def main():
    st.title("🚔 PRF Data Analytics & Action Plan")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Analytics Dashboard")
        st.info(
            "Explore os dados de acidentes de 2023, identifique pontos críticos e gere insights geográficos e temporais."
        )
        if st.button("Ir para Analytics"):
            st.switch_page("pages/01_analysis.py")

    with col2:
        st.subheader("📋 Gestor de Tarefas")
        st.success(
            "Transforme insights em ação. Crie, priorize e gerencie planos de intervenção baseados nos dados."
        )
        if st.button("Ir para Tarefas"):
            st.switch_page("pages/02_tasks.py")

    st.markdown("---")
    st.markdown("### 🛠️ Stack do Projeto")
    st.code("Python + Polars + DuckDB + SQLite + Streamlit", language="text")


if __name__ == "__main__":
    main()
