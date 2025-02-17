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

nome_pick = input("Escreva o nome do pick: ")

# Função para obter um ID válido a partir da tabela correspondente
def obter_id_valido(tabela, id_coluna, nome_coluna):
    cursor.execute(f"SELECT {id_coluna}, {nome_coluna} FROM {tabela}")
    itens = cursor.fetchall()
    
    print(f"\nOpções disponíveis em {tabela}:")
    for item in itens:
        print(f"{item[0]} - {item[1]}")

    while True:
        try:
            escolha = int(input(f"Digite o ID do {nome_coluna} desejado: "))
            if any(escolha == item[0] for item in itens):
                return escolha
            else:
                print("ID inválido, tente novamente.")
        except ValueError:
            print("Entrada inválida, digite um número.")

# Perguntar ao usuário os IDs para cada categoria
id_champion = obter_id_valido("champions", "id_champion", "nome_champion")
id_role = obter_id_valido("roles", "id_role", "nome_role")
id_build = obter_id_valido("builds", "id_build", "nome_build")

# Inserir os dados na tabela picks
cursor.execute('''
    INSERT INTO picks (nome_pick, id_champion, id_roles, id_builds)
    VALUES (?, ?, ?, ?)
''', (nome_pick, id_champion, id_role, id_build))

# Confirmar e fechar conexão
connection.commit()
connection.close()