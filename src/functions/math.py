
import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from read import ler_picks 
# Current file directory
current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
db_path = os.path.join(base_dir, 'sqlite_database', 'lol.db')

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

def winrate():
    print()
    ler_picks()
    pick = input("Escreva o numero pick para calcular a winrate: ")
    cursor.execute(f'SELECT vitoria_derrota FROM jogo WHERE id_pick = {pick}')
