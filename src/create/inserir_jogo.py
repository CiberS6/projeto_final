
import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from src.read.ler_picks import ler_picks
# Current file directory
current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
db_path = os.path.join(base_dir, 'sqlite_database', 'lol.db')

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

def inserir_jogo():

    ler_picks()
    pick = input("Insira o id do pick: ")

    kils= int(input("Quantas kills: "))
    deaths= int(input("Quantas deaths: "))
    assists= int(input("Quantas assists: "))
    win_lose= bool(input("Win(1) Lose(0): "))

    cursor.execute('''
    INSERT INTO jogo (id_pick, kills, deaths, assists, vitoria_derrota)
    VALUES (?, ?, ?, ?, ?)
''', (pick, kils, deaths, assists, win_lose))
    
    connection.commit()
    connection.close()
    

