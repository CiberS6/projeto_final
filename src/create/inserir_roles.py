import sqlite3

connection = sqlite3.connect('C:\\users\\ba2490\\Desktop\\projeto_final\\projeto_final\\sqlite_database\\lol.db')
cursor = connection.cursor()

cursor.execute('INSERT INTO roles (nome_role) VALUES (?), (?), (?), (?), (?)', ("TOP", "JUNGLE", "MID", "ADC", "SUPPORT"))

connection.commit()
connection.close()
