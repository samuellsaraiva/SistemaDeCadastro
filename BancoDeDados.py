import sqlite3

conn = sqlite3.connect('UserData.db')
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Tb_Usuarios(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT UNIQUE NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Usuario TEXT UNIQUE NOT NULL,
    Senha TEXT NOT NULL
    );
""")
