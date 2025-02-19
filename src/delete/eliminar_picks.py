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

def eliminar_pick():
    # Conectar ao banco de dados
    
    # Exibir a lista de picks disponíveis
    cursor.execute('''
                SELECT id_pick, picks.nome_pick, champions.nome_champion, roles.nome_role, builds.nome_build
                FROM picks
                INNER JOIN champions ON picks.id_champion = champions.id_champion
                INNER JOIN roles ON picks.id_roles = roles.id_role
                INNER JOIN builds ON picks.id_builds = builds.id_build
    ''')
    picks = cursor.fetchall()
    if picks:
        print("Picks disponíveis:")
        for pick in picks:
            print(f"ID: {pick[0]}, Nome Pick: {pick[1]}, Champion: {pick[2]}, Role: {pick[3]}, Build: {pick[4]}")
    else:
        print("Nenhum pick disponível.")
        connection.close()
        return
    
    # Solicitar o ID do pick a ser excluído
    id_pick = input("Digite o ID do pick que deseja eliminar: ")
    
    try:
        id_pick = int(id_pick)
        cursor.execute("DELETE FROM picks WHERE id_pick = ?", (id_pick,))
        connection.commit()
        
        if cursor.rowcount > 0:
            print(f"Pick com ID {id_pick} foi eliminado com sucesso!")
        else:
            print(f"Nenhum pick encontrado com ID {id_pick}.")
    except ValueError:
        print("Por favor, insira um ID válido.")
    except sqlite3.Error as e:
        print("Erro ao deletar pick:", e)
    finally:
        connection.close()



