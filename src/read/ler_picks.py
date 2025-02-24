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
    cursor.execute('SELECT id_pick FROM picks')
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

def ler_jogo():
    cursor.execute('SELECT id_jogo FROM jogo')
    do_ = cursor.fetchall()
    cursor.execute('''
                    SELECT picks.nome_pick FROM jogo
                    INNER JOIN picks ON jogo.id_pick = picks.id_pick
''')
    do = cursor.fetchall()
    cursor.execute('SELECT kills, deaths, assists FROM jogo')
    do__ = cursor.fetchall()
    
    for pick,jogo,kda in zip(do,do_,do__):
        print(jogo," ",pick," ",kda)
    
