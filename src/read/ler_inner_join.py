import sqlite3

connection = sqlite3.connect('C:\\users\\ba2490\\Desktop\\projeto_final\\projeto_final\\sqlite_database\\lol.db')
cursor = connection.cursor()

cursor.execute('''
                SELECT picks.nome_pick, champions.nome_champion, roles.nome_role, builds.nome_build
                FROM picks
                INNER JOIN champions ON picks.id_champion = champions.id_champion
                INNER JOIN roles ON picks.id_roles = roles.id_role
                INNER JOIN builds ON picks.id_builds = builds.id_build
''')

# Resultados do inner join
resultaldos = cursor.fetchall()
for i in resultaldos:
    print(i)