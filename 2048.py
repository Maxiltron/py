#Fonction qui permet d'afficher la grille de jeu
from typing import List
import random

def display_board(list: List[str]):
    for row in list:
        print(" | ".join(row))
        print("-" * (4 * len(row) - 1))



board_size = int(input("Choisissez la taille du plateau: "))
board = [[" " for _ in range(board_size)] for _ in range(board_size)]

display_board(board)



def generate_tiles():
    tile_2: str = "2"
    tile_4: str = "4"
    apparition_chance: int = random.randint(1,10)
    
    if apparition_chance != 1:

