import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

# Current file directory
current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
db_path = os.path.join(base_dir, 'sqlite_database', 'lol.db')

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute('SELECT id_champion, nome_champion FROM champions')
resultados = cursor.fetchall()
for champions in resultados:
    print(champions)

cursor.execute('SELECT id_champion, nome_champion FROM champions WHERE nome_champion = "Akali"\n')
resultados = cursor.fetchall()
for champions in resultados:
    print(champions)