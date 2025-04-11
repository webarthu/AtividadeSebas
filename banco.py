import sqlite3

def conectar():
    return sqlite3.connect('meubanco.db')

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()
