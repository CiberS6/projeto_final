import sqlite3

connection = sqlite3.connect('C:\\users\\ba2490\\Desktop\\projeto_final\\projeto_final\\sqlite_database\\lol.db')
cursor = connection.cursor()

cursor.execute('INSERT INTO builds (nome_build) VALUES (?), (?), (?), (?), (?), (?)', ("AP", "AD", "LETHALITY", "BRUISER", "TANK", "SUPPORT"))

connection.commit()
connection.close()