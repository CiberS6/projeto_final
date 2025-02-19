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

try:
    print('''
        **********Menu*************\n
        1-\n
        2-\n
        3-\n
        4-\n
            ''')
    opc = int(input("Escolha uma opção"))
    match(opc):
        case 1:
            print()
        case 2:
            print()
        case _:
            print()
        
except SyntaxError as e:
    print(e)