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

cursor.execute('''
                CREATE TABLE IF NOT EXISTS picks (
                id_pick INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_pick TEXT NOT NULL,
                id_champion INTEGER NOT NULL,
                id_roles INTEGER NOT NULL,
                id_builds INTEGER NOT NULL
                )
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS jogo (
               id_jogo INTEGER PRIMARY KEY AUTOINCREMENT,
               id_pick INTEGER NOT NULL,
               kills INTEGER NOT NULL,
               deaths INTEGER NOT NULL,
               assists INTEGER NOT NULL,
               vitoria_derrota BOOL NOT NULL
               )
               ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS champions (
                id_champion INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_champion TEXT NOT NULL
                )               
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS roles (
                id_role INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_role TEXT NOT NULL 
                )               
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS builds (
                id_build INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_build TEXT NOT NULL
                )               
                ''')

connection.commit()
connection.close()