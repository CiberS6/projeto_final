import sqlite3

connection = sqlite3.connect('')
cursor = connection.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS picks (
                id_pick INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_pick TEXT NOT NULL,
                id_champion FOREIGN KEY INTEGER NOT NULL,
                id_roles INTEGER FOREIGN KEY NOT NULL,
                id_builds INTEGER FOREIGN KEY NOT NULL
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