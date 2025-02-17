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

cursor.execute('SELECT id_role, nome_role FROM roles')
resultados = cursor.fetchall()
for roles in resultados:
    print(roles)

cursor.execute('SELECT id_role, nome_role FROM roles WHERE nome_role = "MID";')
for roles in resultados:
    print(roles)