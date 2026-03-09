import streamlit as st

from src.database.tasks_repo import (
    create_task,
    list_tasks,
    update_task_status,
    delete_task,
)

st.set_page_config(page_title="Gestor de Tarefas", page_icon="📋", layout="wide")


def main():
    st.title("📋 Plano de Ação & Gestão de Tarefas")
    st.markdown(
        "Use esta página para gerenciar as intervenções e estudos preventivos baseados nos insights do dashboard."
    )

    # Sidebar para Novo Cadastro
    with st.sidebar:
        st.header("✨ Nova Tarefa")
        with st.form("new_task_form"):
            titulo = st.text_input(
                "Título da Tarefa", placeholder="Ex: Estudo de sinalização BR-101"
            )
            descricao = st.text_area("Descrição detalhada")
            col1, col2 = st.columns(2)
            status = col1.selectbox("Status", ["Pendente", "Em Progresso", "Concluído"])
            prioridade = col2.selectbox("Prioridade", ["Baixa", "Média", "Alta"])

            st.subheader("📍 Geolocalização (Opcional)")
            br = st.text_input("Rodovia (BR)", placeholder="Ex: 101")
            km = st.number_input("KM", min_value=0.0, step=0.1)

            submit = st.form_submit_button("Criar Tarefa")

            if submit:
                if titulo:
                    tid = create_task(titulo, descricao, status, prioridade, br, km)
                    st.success(f"Tarefa #{tid} criada com sucesso!")
                    st.rerun()
                else:
                    st.error("O título é obrigatório.")

    # Listagem de Tarefas
    st.subheader("✅ Tarefas Registradas")
    tasks = list_tasks()

    if not tasks:
        st.info("Nenhuma tarefa cadastrada ainda. Use a barra lateral para começar!")
    else:
        for task in tasks:
            with st.expander(f"#{task['id']} - {task['titulo']} | [{task['status']}]"):
                c1, c2, c3 = st.columns([2, 1, 1])

                c1.markdown(f"**Descrição:** {task['descricao']}")
                c1.markdown(f"**Local:** BR-{task['br']} KM {task['km']}")

                # Ações
                new_status = c2.selectbox(
                    "Alterar Status",
                    ["Pendente", "Em Progresso", "Concluído"],
                    index=["Pendente", "Em Progresso", "Concluído"].index(
                        task["status"]
                    ),
                    key=f"status_{task['id']}",
                )

                if new_status != task["status"]:
                    update_task_status(task["id"], new_status)
                    st.rerun()

                if c3.button("🗑️ Deletar", key=f"del_{task['id']}"):
                    delete_task(task["id"])
                    st.rerun()


if __name__ == "__main__":
    main()
