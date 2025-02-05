import sqlite3

connection = sqlite3.connect('C:\\users\\ba2490\\Desktop\\projeto_final\\projeto_final\\sqlite_database\\lol.db')
cursor = connection.cursor()

cursor.execute('SELECT id_champion, nome_champion FROM champions')
resultados = cursor.fetchall()
for champions in resultados:
    print(champions)