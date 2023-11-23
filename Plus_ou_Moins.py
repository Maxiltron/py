import random


def Ask_only_number(message: str):
    while True:
        value: str = input(message)

        if value.isdigit():
            return int(value)

        print("Erreur")



def Ask_Min_Max():
    while True:
        min: str = Ask_only_number("Donnez un nombre minimum: ")
        max: str = Ask_only_number("Donnez un nombre maximum: ")

        if min < max:
            return min, max
        print("Erreur")

def nb_random():
    (a,b) = Ask_Min_Max()
    nb: int = random.randint(a,b)
    return nb


def Replay(message: str):
    while message == "yes":
        essai: int = 10
        nb_AI: int = nb_random()
        while True:
            nb: int = Ask_only_number("Donnez un nombre: ")
            if essai == 0:
                print("Perdu")
                return False
            elif nb < nb_AI:
                print("Plus", "(Il vous reste", str(essai - 1), "essai sur 10)")
            elif nb > nb_AI:
                print("Moins", "(Il vous reste", str(essai - 1), "essai sur 10)")
            else:
                print("Victoire")
                return False
            essai=essai-1


def More_or_Less(a: int,b: int):
    if a < b:
        value: str = "Plus"
    elif a > b:
        value: str = "Moins"
    else:
        value: str = "Victoire"
    return value

def Game():
    essai: int = 10
    nb_AI: int = nb_random()
    while essai >= 1:
        nb: int = Ask_only_number("Donner un nombre: ")
        result: str = More_or_Less(nb,nb_AI)
        if result == "Victoire":
            print(result)

            return
        else:
            print(result,str(essai-1),"sur 10")
            essai=essai-1
    print("Perdu")
    return
Game()
Replay()
