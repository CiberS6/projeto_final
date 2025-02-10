import sqlite3

connection = sqlite3.connect('C:\\users\\ba2490\\Desktop\\projeto_final\\projeto_final\\sqlite_database\\lol.db')
cursor = connection.cursor()

def selecionar_pick():
    while True:
        cursor.execute("SELECT id_pick, nome_pick FROM picks")
        picks = cursor.fetchall()

        if not picks:
            print("Nenhum pick encontrado.")
            return None  # Se não houver picks, retorna None

        print("\nPicks disponíveis:")
        for pick in picks:
            print(f"{pick[0]} - {pick[1]}")

        try:
            id_pick = int(input("\nDigite o ID do pick que deseja editar (ou 0 para voltar): "))
            if id_pick == 0:
                return "voltar"  # Sinaliza que o usuário quer voltar
            if any(id_pick == pick[0] for pick in picks):
                return id_pick
            else:
                print("ID inválido, tente novamente.")
        except ValueError:
            print("Entrada inválida, digite um número.")

# Função para mostrar opções e obter um ID válido
def obter_id_valido(tabela, id_coluna, nome_coluna):
    while True:
        cursor.execute(f"SELECT {id_coluna}, {nome_coluna} FROM {tabela}")
        itens = cursor.fetchall()

        print(f"\nOpções disponíveis em {tabela}:")
        for item in itens:
            print(f"{item[0]} - {item[1]}")

        try:
            escolha = int(input(f"Digite o ID do {nome_coluna} desejado (ou 0 para voltar): "))
            if escolha == 0:
                return None  # Retorna None para indicar que o usuário quer voltar
            if any(escolha == item[0] for item in itens):
                return escolha
            else:
                print("ID inválido, tente novamente.")
        except ValueError:
            print("Entrada inválida, digite um número.")

# Função para atualizar o pick
def atualizar_pick():
    while True:
        id_pick = selecionar_pick()
        if id_pick == "voltar":  # Se o usuário quiser voltar, reinicia o fluxo
            print("\nVoltando ao menu principal...\n")
            return  # Sai da função sem encerrar o script

        if not id_pick:  # Se nenhum pick foi encontrado
            print("\nOperação cancelada.")
            return

        while True:
            print("\nCampos disponíveis para atualização:")
            print("1 - Nome do Pick")
            print("2 - Champion")
            print("3 - Role")
            print("4 - Build")
            print("0 - Voltar para a seleção de pick")

            escolha = input("\nDigite o número do campo que deseja atualizar: ")

            if escolha == "1":
                novo_valor = input("Digite o novo nome do pick (ou pressione Enter para voltar): ")
                if novo_valor == "":
                    continue  # Volta para o menu de seleção de campos
                cursor.execute("UPDATE picks SET nome_pick = ? WHERE id_pick = ?", (novo_valor, id_pick))

            elif escolha == "2":
                novo_valor = obter_id_valido("champions", "id_champion", "nome_champion")
                if novo_valor is None:
                    continue  # Volta para o menu de seleção de campos
                cursor.execute("UPDATE picks SET id_champion = ? WHERE id_pick = ?", (novo_valor, id_pick))

            elif escolha == "3":
                novo_valor = obter_id_valido("roles", "id_role", "nome_role")
                if novo_valor is None:
                    continue  # Volta para o menu de seleção de campos
                cursor.execute("UPDATE picks SET id_roles = ? WHERE id_pick = ?", (novo_valor, id_pick))

            elif escolha == "4":
                novo_valor = obter_id_valido("builds", "id_build", "nome_build")
                if novo_valor is None:
                    continue  # Volta para o menu de seleção de campos
                cursor.execute("UPDATE picks SET id_builds = ? WHERE id_pick = ?", (novo_valor, id_pick))

            elif escolha == "0":
                print("\nVoltando para a seleção de pick...\n")
                break  # Sai do loop e volta para selecionar outro pick

            else:
                print("Opção inválida. Tente novamente.")
                continue

            connection.commit()
            print("\nCampo atualizado com sucesso!")

            continuar = input("\nDeseja alterar outro campo deste pick? (s/n): ").strip().lower()
            if continuar != 's':
                break  # Sai do loop de edição de campos

# Executar a função
while True:
    atualizar_pick()
    continuar_script = input("\nDeseja editar outro pick? (s/n): ").strip().lower()
    if continuar_script != 's':
        break

# Fechar conexão
connection.close()