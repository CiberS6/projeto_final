import sqlite3

connection = sqlite3.connect('C:\\users\\ba2490\\Desktop\\projeto_final\\projeto_final\\sqlite_database\\lol.db')
cursor = connection.cursor()

cursor.execute('SELECT id_build, nome_build FROM builds')
resultados = cursor.fetchall()
for builds in resultados:
    print(builds)