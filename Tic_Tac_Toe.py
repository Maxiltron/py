J1: str = "O"
J2: str = "X"
empty: list[str] = []

def board_game():
    i_max = 3
    empty: list[str] = []
    for i in range(0, i_max):
        print(empty,empty,empty)

def positon_J1():
    coordinates_x = input("Dans quelle ligne voulez vous placer votre symbole ?: ")
    coordinates_y = input("Dans quelle colonne voulez vous placer votre symbole ?: ")
    return coordinates_x,coordinates_y


def Update_board():
    coordinates_J1 = positon_J1()
    i_max = 3
    for i in range(0, i_max):
        print(empty, empty, empty)
