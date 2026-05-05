import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "02-database" / "tasks.db"


def get_connection() -> sqlite3.Connection:
    """Retorna uma conexão SQLite com foreign keys habilitadas."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def column_exists(conn: sqlite3.Connection, table_name: str, column_name: str) -> bool:
    """Verifica se uma coluna já existe na tabela."""
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    return any(col[1] == column_name for col in columns)


def ensure_column(
    conn: sqlite3.Connection,
    table_name: str,
    column_name: str,
    column_definition: str,
) -> None:
    """Adiciona coluna se ela ainda não existir."""
    if not column_exists(conn, table_name, column_name):
        cursor = conn.cursor()
        cursor.execute(
            f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_definition}"
        )


def init_db() -> None:
    """Inicializa o banco e garante a estrutura necessária da tabela tasks."""
    print(f"🗄️ Inicializando banco de dados em: {DB_PATH}")

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with get_connection() as conn:
        cursor = conn.cursor()

        # Criação base da tabela
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                status TEXT NOT NULL DEFAULT 'Pendente',
                prioridade TEXT NOT NULL DEFAULT 'Média',
                br TEXT,
                km REAL,
                municipio TEXT,
                uf TEXT,
                latitude REAL,
                longitude REAL,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        )

        # Migração segura para bases antigas
        ensure_column(conn, "tasks", "municipio", "TEXT")
        ensure_column(conn, "tasks", "uf", "TEXT")
        ensure_column(conn, "tasks", "latitude", "REAL")
        ensure_column(conn, "tasks", "longitude", "REAL")

        # Índices úteis
        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_tasks_status
            ON tasks(status);
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_tasks_prioridade
            ON tasks(prioridade);
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_tasks_br_km
            ON tasks(br, km);
            """
        )

        conn.commit()

    print("✅ Banco inicializado e estrutura da tabela 'tasks' validada com sucesso!")


if __name__ == "__main__":
    init_db()