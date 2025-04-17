import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE,
        saldo REAL NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        valor REAL,
        data TEXT
    )
''')

usuarios = [
    ('joao', 100.0),
    ('maria', 150.0),
    ('ana', 200.0)
]

cursor.executemany('INSERT OR IGNORE INTO usuarios (nome, saldo) VALUES (?, ?)', usuarios)

conn.commit()
conn.close()

print("Banco de dados 'banco.db' criado com sucesso!")
