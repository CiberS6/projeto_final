import sqlite3

connection = sqlite3.connect('C:\\users\\ba2490\\Desktop\\projeto_final\\projeto_final\\sqlite_database\\lol.db')
cursor = connection.cursor()

cursor.execute('SELECT id_role, nome_role FROM roles')
resultados = cursor.fetchall()
for roles in resultados:
    print(roles)