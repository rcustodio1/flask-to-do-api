import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    concluida INTEGER NOT NULL
)
""")

con.commit()
con.close()

print("Banco de dados criado com sucesso!")
