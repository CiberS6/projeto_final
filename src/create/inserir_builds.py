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

cursor.execute('INSERT INTO builds (nome_build) VALUES (?), (?), (?), (?), (?), (?)', ("AP", "AD", "LETHALITY", "BRUISER", "TANK", "SUPPORT"))

connection.commit()
connection.close()