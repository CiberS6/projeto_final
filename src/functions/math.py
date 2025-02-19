
import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from src.read.ler_picks import ler_picks 
from src.read.ler_inner_join import pick_name
# Current file directory
current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
db_path = os.path.join(base_dir, 'sqlite_database', 'lol.db')

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

def winrate():
    print()

    #pick_name()
    ler_picks()
    

    pick = input("Escreva o numero pick para calcular a winrate: ")

    cursor.execute(f'SELECT vitoria_derrota FROM jogo WHERE id_pick = {pick}')

    win_lose = cursor.fetchall()
    win_count = 0
    play = 0

    for win in win_lose:
        print(win)
        
        if win[0] == 1:
            win_count += 1 
        
        play +=1

    win_rate = win_count*100/play
    print(win_count)
    print(f"A winrate de {pick} é {win_rate}")        


winrate()

