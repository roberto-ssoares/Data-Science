import sys
from pathlib import Path

# Garantir import da raiz do projeto
ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import pandas as pd
import streamlit as st

from src.database.tasks_repo import (
    create_task,
    delete_task,
    list_tasks,
    update_task_status,
)

st.set_page_config(
    page_title="Gestor de Tarefas",
    page_icon="📋",
    layout="wide",
)

STATUS_OPTIONS = ["Pendente", "Em Andamento", "Concluída", "Cancelada"]
PRIORIDADE_OPTIONS = ["Baixa", "Média", "Alta", "Crítica"]


def render_task_form():
    st.subheader("➕ Nova Tarefa")

    with st.form("task_form", clear_on_submit=True):
        titulo = st.text_input("Título da tarefa")
        descricao = st.text_area("Descrição")
        prioridade = st.selectbox("Prioridade", PRIORIDADE_OPTIONS, index=1)
        status = st.selectbox("Status inicial", STATUS_OPTIONS, index=0)

        col1, col2 = st.columns(2)
        with col1:
            br = st.text_input("BR", placeholder="Ex.: 116")
            municipio = st.text_input("Município", placeholder="Ex.: Registro")
            latitude = st.text_input("Latitude", placeholder="Ex.: -24.4971")
        with col2:
            km = st.text_input("KM", placeholder="Ex.: 232.5")
            uf = st.text_input("UF", placeholder="Ex.: SP")
            longitude = st.text_input("Longitude", placeholder="Ex.: -47.8449")

        submitted = st.form_submit_button("Criar tarefa")

        if submitted:
            if not titulo.strip():
                st.error("Informe um título para a tarefa.")
                return

            km_value = None
            lat_value = None
            lon_value = None

            try:
                km_value = float(km) if km.strip() else None
            except ValueError:
                st.error("KM deve ser numérico.")
                return

            try:
                lat_value = float(latitude) if latitude.strip() else None
            except ValueError:
                st.error("Latitude deve ser numérica.")
                return

            try:
                lon_value = float(longitude) if longitude.strip() else None
            except ValueError:
                st.error("Longitude deve ser numérica.")
                return

            create_task(
                titulo=titulo.strip(),
                descricao=descricao.strip(),
                status=status,
                prioridade=prioridade,
                br=br.strip() or None,
                km=km_value,
                municipio=municipio.strip() or None,
                uf=uf.strip() or None,
                latitude=lat_value,
                longitude=lon_value,
            )

            st.success("Tarefa criada com sucesso!")
            st.rerun()


def render_task_card(task: dict):
    prioridade = task.get("prioridade", "Média")
    status_atual = task.get("status", "Pendente")

    with st.container(border=True):
        col1, col2 = st.columns([4, 2])

        with col1:
            st.markdown(f"### {task['titulo']}")
            st.markdown(f"**Descrição:** {task.get('descricao') or '-'}")

            local_parts = []
            if task.get("br"):
                local_parts.append(f"BR {task['br']}")
            if task.get("km") is not None:
                local_parts.append(f"KM {task['km']}")
            if task.get("municipio"):
                local_parts.append(task["municipio"])
            if task.get("uf"):
                local_parts.append(task["uf"])

            localizacao = " • ".join(local_parts) if local_parts else "Não informada"
            st.markdown(f"**Localização:** {localizacao}")

            coords = []
            if task.get("latitude") is not None:
                coords.append(f"Lat: {task['latitude']}")
            if task.get("longitude") is not None:
                coords.append(f"Lon: {task['longitude']}")
            if coords:
                st.caption(" | ".join(coords))

            st.caption(f"Criada em: {task.get('data_criacao', '-')}")
            st.markdown(f"**Prioridade:** {prioridade}")

        with col2:
            novo_status = st.selectbox(
                "Status",
                STATUS_OPTIONS,
                index=STATUS_OPTIONS.index(status_atual)
                if status_atual in STATUS_OPTIONS
                else 0,
                key=f"status_{task['id']}",
            )

            if st.button("Atualizar status", key=f"update_{task['id']}"):
                update_task_status(task["id"], novo_status)
                st.success("Status atualizado!")
                st.rerun()

            if st.button("Excluir tarefa", key=f"delete_{task['id']}"):
                delete_task(task["id"])
                st.warning("Tarefa excluída.")
                st.rerun()


def render_task_filters(tasks_df: pd.DataFrame) -> pd.DataFrame:
    st.subheader("🔎 Filtros")

    col1, col2, col3 = st.columns(3)

    with col1:
        status_filter = st.multiselect(
            "Status",
            STATUS_OPTIONS,
            default=[],
        )

    with col2:
        prioridade_filter = st.multiselect(
            "Prioridade",
            PRIORIDADE_OPTIONS,
            default=[],
        )

    with col3:
        uf_options = sorted([uf for uf in tasks_df["uf"].dropna().unique().tolist() if uf])
        uf_filter = st.multiselect(
            "UF",
            uf_options,
            default=[],
        )

    search_text = st.text_input("Buscar por título, descrição, BR ou município")

    filtered = tasks_df.copy()

    if status_filter:
        filtered = filtered[filtered["status"].isin(status_filter)]

    if prioridade_filter:
        filtered = filtered[filtered["prioridade"].isin(prioridade_filter)]

    if uf_filter:
        filtered = filtered[filtered["uf"].isin(uf_filter)]

    if search_text.strip():
        term = search_text.strip().lower()

        def contains_term(value):
            if pd.isna(value):
                return False
            return term in str(value).lower()

        mask = (
            filtered["titulo"].apply(contains_term)
            | filtered["descricao"].apply(contains_term)
            | filtered["br"].apply(contains_term)
            | filtered["municipio"].apply(contains_term)
        )
        filtered = filtered[mask]

    return filtered


def render_kpis(tasks_df: pd.DataFrame):
    total = len(tasks_df)
    pendentes = (tasks_df["status"] == "Pendente").sum() if not tasks_df.empty else 0
    andamento = (tasks_df["status"] == "Em Andamento").sum() if not tasks_df.empty else 0
    concluidas = (tasks_df["status"] == "Concluída").sum() if not tasks_df.empty else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total de Tarefas", total)
    c2.metric("Pendentes", int(pendentes))
    c3.metric("Em Andamento", int(andamento))
    c4.metric("Concluídas", int(concluidas))


def main():
    st.title("📋 Gestor de Tarefas Operacionais")
    st.markdown(
        "Gerencie ações de intervenção associadas aos pontos críticos identificados na análise de acidentes."
    )
    st.divider()

    col_form, col_list = st.columns([1, 2])

    with col_form:
        render_task_form()

    with col_list:
        tasks = list_tasks()

        if not tasks:
            st.info("Nenhuma tarefa cadastrada até o momento.")
            return

        tasks_df = pd.DataFrame(tasks)

        render_kpis(tasks_df)
        st.divider()

        filtered_df = render_task_filters(tasks_df)
        st.divider()

        st.subheader("🗂️ Lista de Tarefas")

        if filtered_df.empty:
            st.warning("Nenhuma tarefa encontrada com os filtros atuais.")
            return

        for _, row in filtered_df.iterrows():
            render_task_card(row.to_dict())


if __name__ == "__main__":
    main()