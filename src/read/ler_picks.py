import sqlite3

connection = sqlite3.connect('C:\\users\\ba2490\\Desktop\\projeto_final\\projeto_final\\sqlite_database\\lol.db')
cursor = connection.cursor()
def ler_picks():
    cursor.execute('SELECT id_pick, id_champion, id_role FROM picks WHERE id_champion = 95')
    resultados = cursor.fetchall()
    for champions in resultados:
        print(champions)