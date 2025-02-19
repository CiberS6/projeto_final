import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from src.create.inserir_picks import insert_picks
from src.update.atualizar_picks import update_this
from src.read.ler_picks import ler_picks
from src.delete.eliminar_picks import eliminar_pick
from src.create.inserir_jogo import inserir_jogo
from src.functions.math import winrate



# Current file directory
current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
db_path = os.path.join(base_dir, 'sqlite_database', 'lol.db')

connection = sqlite3.connect(db_path)
cursor = connection.cursor()
def menu():
    try:
        while(True):
            print('''
                **********Menu*************\n
                1-Inserir picks\n
                2-Atualizar picks\n
                3-Ler picks\n
                4-Eliminar picks\n
                5-Inserir jogo\n
                6-Winrate\n
                7-Sair\n
                    ''')
            opc = int(input("Escolha uma opção(de 1 a 7)\n=>"))
            match(opc):
                case 1:
                    insert_picks()
                case 2:
                    update_this()
                case 3:
                    ler_picks()
                case 4:
                    eliminar_pick()
                case 5:
                    inserir_jogo()
                case 6:
                    winrate()
                case 7:
                    break 
                case _:
                    print("Escolha uma opção de 1 a 7")
                
    except SyntaxError as e:
        print(e)