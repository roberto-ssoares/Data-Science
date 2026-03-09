import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "02-database" / "tasks.db"


def init_db():
    print(f"🗄️ Inicializando banco de dados em: {DB_PATH}")

    # Garantir que a pasta existe
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Criar tabela de tarefas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT,
        status TEXT NOT NULL DEFAULT 'Pendente',
        prioridade TEXT NOT NULL DEFAULT 'Média',
        br TEXT,
        km REAL,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    conn.close()
    print("✅ Tabela 'tasks' criada/verificada com sucesso!")


if __name__ == "__main__":
    init_db()
