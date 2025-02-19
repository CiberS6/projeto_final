
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


def ler_picks():
    cursor.execute('SELECT id_pick, id_champion, id_roles FROM picks')
    resultados = cursor.fetchall()

    cursor.execute('''
                    SELECT picks.nome_pick, champions.nome_champion, roles.nome_role, builds.nome_build
                    FROM picks
                    INNER JOIN champions ON picks.id_champion = champions.id_champion
                    INNER JOIN roles ON picks.id_roles = roles.id_role
                    INNER JOIN builds ON picks.id_builds = builds.id_build
    ''')

    # Resultados do inner join
    resultados_ = cursor.fetchall()
    for i,champions in zip(resultados_,resultados):
        print(i," ",champions)
    
    

