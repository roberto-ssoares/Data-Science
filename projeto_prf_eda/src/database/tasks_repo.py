import sqlite3
from pathlib import Path
from typing import List, Dict, Any

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "02-database" / "tasks.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_task(
    titulo: str,
    descricao: str,
    status: str,
    prioridade: str,
    br: str = None,
    km: float = None,
) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO tasks (titulo, descricao, status, prioridade, br, km)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (titulo, descricao, status, prioridade, br, km),
        )
        return cursor.lastrowid


def list_tasks() -> List[Dict[str, Any]]:
    with get_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks ORDER BY data_criacao DESC")
        return [dict(row) for row in cursor.fetchall()]


def update_task_status(task_id: int, new_status: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id)
        )


def delete_task(task_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))


if __name__ == "__main__":
    # Teste rápido do repositório
    print("🧪 Testando repositório de tarefas...")
    try:
        tid = create_task(
            "Teste Iniciais", "Descrição de teste", "Pendente", "Alta", "BR-101", 10.5
        )
        print(f"✅ Tarefa criada com ID: {tid}")
        tasks = list_tasks()
        print(f"📋 Total de tarefas: {len(tasks)}")
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
