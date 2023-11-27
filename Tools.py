import random


def Response_replay(list: [str]):
    while True:
        answer: str = input("Voulez vous rejouer ? (y/n) : ").lower()
        if answer in list:
            return answer
        print("Erreur")


def Ask_only_number(message: str):
    while True:
        value: str = input(message)

        if value.isdigit():
            return int(value)

        print("Erreur")


def Ask_Min_Max():
    while True:
        min: int = Ask_only_number("Donnez un nombre minimum: ")
        max: int = Ask_only_number("Donnez un nombre maximum: ")

        if min < max:
            return min, max
        print("Erreur")


def Get_random():
    (a, b) = Ask_Min_Max()
    nb_AI: int = random.randint(a, b)
    return nb_AI


def More_or_Less(a: int, b: int, c: int):
    if c == 0:
        value: str = "Perdu"
    elif a < b:
        value: str = "Plus"
    elif a > b:
        value: str = "Moins"
    else:
        value: str = "Victoire"
    return value


def Ask_PFC(message: str):
    list: [str] = ["p", "f", "c"]
    while True:
        value: str = input(message).lower()
        while value in list:
            return value
        print("Erreur")

def Get_random_PFC():
    list_AI: [str] = ["p","f","c"]
    nb_AI: int = random.randint(0, 2)
    return list_AI[nb_AI]


def Win_Or_Lose_PFC(choice_1: str,choice_2: str):
    list_Win: [str] = ["pc", "fp", "cf"]
    value_1: str = "Victoire"
    value_2: str = "Perdu"
    play: str = choice_1 + choice_2
    while play in list_Win:
        return value_1
    return value_2



