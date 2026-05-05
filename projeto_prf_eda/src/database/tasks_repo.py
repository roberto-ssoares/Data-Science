import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional


BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "02-database" / "tasks.db"


def get_connection() -> sqlite3.Connection:
    """Cria conexão com o banco SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def create_task(
    titulo: str,
    descricao: str,
    status: str = "Pendente",
    prioridade: str = "Média",
    br: Optional[str] = None,
    km: Optional[float] = None,
    municipio: Optional[str] = None,
    uf: Optional[str] = None,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
) -> int:
    """Cria uma nova tarefa e retorna o ID gerado."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO tasks (
                titulo,
                descricao,
                status,
                prioridade,
                br,
                km,
                municipio,
                uf,
                latitude,
                longitude
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                titulo,
                descricao,
                status,
                prioridade,
                br,
                km,
                municipio,
                uf,
                latitude,
                longitude,
            ),
        )
        conn.commit()
        return cursor.lastrowid


def list_tasks() -> List[Dict[str, Any]]:
    """Lista todas as tarefas, mais recentes primeiro."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM tasks
            ORDER BY data_criacao DESC, id DESC
            """
        )
        return [dict(row) for row in cursor.fetchall()]


def get_task_by_id(task_id: int) -> Optional[Dict[str, Any]]:
    """Busca uma tarefa pelo ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )
        row = cursor.fetchone()
        return dict(row) if row else None


def update_task_status(task_id: int, new_status: str) -> None:
    """Atualiza apenas o status da tarefa."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE tasks
            SET status = ?
            WHERE id = ?
            """,
            (new_status, task_id),
        )
        conn.commit()


def update_task(
    task_id: int,
    titulo: str,
    descricao: str,
    status: str,
    prioridade: str,
    br: Optional[str] = None,
    km: Optional[float] = None,
    municipio: Optional[str] = None,
    uf: Optional[str] = None,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
) -> None:
    """Atualiza os principais campos da tarefa."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE tasks
            SET
                titulo = ?,
                descricao = ?,
                status = ?,
                prioridade = ?,
                br = ?,
                km = ?,
                municipio = ?,
                uf = ?,
                latitude = ?,
                longitude = ?
            WHERE id = ?
            """,
            (
                titulo,
                descricao,
                status,
                prioridade,
                br,
                km,
                municipio,
                uf,
                latitude,
                longitude,
                task_id,
            ),
        )
        conn.commit()


def delete_task(task_id: int) -> None:
    """Remove uma tarefa pelo ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )
        conn.commit()


def list_tasks_by_status(status: str) -> List[Dict[str, Any]]:
    """Lista tarefas filtradas por status."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM tasks
            WHERE status = ?
            ORDER BY data_criacao DESC, id DESC
            """,
            (status,),
        )
        return [dict(row) for row in cursor.fetchall()]


def list_tasks_by_location(br: str, km: Optional[float] = None) -> List[Dict[str, Any]]:
    """Lista tarefas por BR e, opcionalmente, KM."""
    with get_connection() as conn:
        cursor = conn.cursor()

        if km is None:
            cursor.execute(
                """
                SELECT *
                FROM tasks
                WHERE br = ?
                ORDER BY data_criacao DESC, id DESC
                """,
                (br,),
            )
        else:
            cursor.execute(
                """
                SELECT *
                FROM tasks
                WHERE br = ? AND km = ?
                ORDER BY data_criacao DESC, id DESC
                """,
                (br, km),
            )

        return [dict(row) for row in cursor.fetchall()]


if __name__ == "__main__":
    print("🧪 Testando repositório de tarefas...")

    try:
        task_id = create_task(
            titulo="Intervenção preventiva em trecho crítico",
            descricao="Trecho identificado no dashboard como ponto recorrente de acidentes.",
            status="Pendente",
            prioridade="Alta",
            br="116",
            km=232.5,
            municipio="Registro",
            uf="SP",
            latitude=-24.4971,
            longitude=-47.8449,
        )

        print(f"✅ Tarefa criada com ID: {task_id}")

        task = get_task_by_id(task_id)
        print("📌 Tarefa criada:")
        print(task)

        tasks = list_tasks()
        print(f"📋 Total de tarefas: {len(tasks)}")

    except Exception as e:
        print(f"❌ Erro no teste: {e}")

        