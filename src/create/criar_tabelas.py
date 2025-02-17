import sqlite3

connection = sqlite3.connect('C:\\users\\ba2490\\Desktop\\projeto_final\\projeto_final\\sqlite_database\\lol.db')
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