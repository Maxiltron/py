import os
import random
import keyboard

board: list[list[str]] = [[" " for _ in range(4)] for _ in range(4)]


def display_board(list: list[list[str]]):
    for row in list:
        print(" | ".join(row))
        print("-" * (4 * len(row) - 1))
    print(" ")


def generate_tiles():
        tile_2: str = "2"
        tile_4: str = "4"
        apparition_chance: int = random.randint(1, 5)
        if apparition_chance != 1:
            coordinates=check_empty()
            board[coordinates[0]][coordinates[1]] = tile_2
            display_board(board)
            if keyboard.wait("Left"):
                move_left(coordinates[0],coordinates[1],tile_2)
            elif keyboard.wait("Right") :
                move_right(coordinates[0],coordinates[1],tile_2)
        else:
            coordinates = check_empty()
            board[coordinates[0]][coordinates[1]] = tile_4
            display_board(board)
            move_down(coordinates[0],coordinates[1],tile_4)








def check_empty():
    while True:
        i: int = random.randint(0,3)
        j: int = random.randint(0,3)
        if board[i][j] == " ":
            return i,j



def move_left(coordinates_x: int,coordinates_y: int, value: str):
    new_coordinates_y: int = coordinates_y
    for j in range(coordinates_y-1,-1,-1):
        if board[coordinates_x][j] == value:
            break
        elif board[coordinates_x][j] == " ":
            new_coordinates_y: int = j
        elif board[coordinates_x][j] == value:
            return display_board(board)
        else:
            break
    board[coordinates_x][coordinates_y] = " "
    board[coordinates_x][new_coordinates_y] = value
    return display_board(board)


def move_right(coordinates_x: int,coordinates_y: int, value: str):
    new_coordinates_y: int = coordinates_y
    for j in range(coordinates_y+1,4,1):
        if board[coordinates_x][j] == value:
            break
        elif board[coordinates_x][j] == " ":
            new_coordinates_y: int = j
        elif board[coordinates_x][j] == value:
            return display_board(board)
        else:
            break
    board[coordinates_x][coordinates_y] = " "
    board[coordinates_x][new_coordinates_y] = value
    return display_board(board)

def move_up(coordinates_x: int,coordinates_y: int, value: str):
    new_coordinates_x: int = coordinates_x
    for j in range(coordinates_x-1,-1,-1):
        if board[j][coordinates_y] == value:
            break
        elif board[j][coordinates_y] == " ":
            new_coordinates_x: int = j
        elif board[j][coordinates_y] == value:
            return display_board(board)
        else:
            break
    board[coordinates_x][coordinates_y] = " "
    board[new_coordinates_x][coordinates_y] = value
    return display_board(board)


def move_down(coordinates_x: int,coordinates_y: int, value: str):
    new_coordinates_x: int = coordinates_x
    for j in range(coordinates_x+1,4,1):
        if board[j][coordinates_y] == value:
            break
        elif board[j][coordinates_y] == " ":
            new_coordinates_x: int = j
        elif board[j][coordinates_y] == value:
            return display_board(board)
        else:
            break
    board[coordinates_x][coordinates_y] = " "
    board[new_coordinates_x][coordinates_y] = value
    return display_board(board)


generate_tiles()



def input_movement(coordinates_x: int,coordinates_y: int, value: str):
    keyboard.wait()
    if keyboard.is_pressed("Left"):
        move_left()
    elif keyboard.is_pressed("Right"):
        move_right()
    elif keyboard.is_pressed()