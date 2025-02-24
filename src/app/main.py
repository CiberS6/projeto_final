import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from src.functions.menu import menu 


menu()