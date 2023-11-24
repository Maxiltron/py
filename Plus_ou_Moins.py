import random


def response_replay(message:str):
    value: str = input(message)
    value_2: str = "yes"
    value_3: str = "no"
    while True:
        if value == value_2:
            return value
        elif value == value_3:
            return value
        else:
            value = input("Erreur ! Répétez votre réponse : ")
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

def get_random():
    (a,b) = Ask_Min_Max()
    nb: int = random.randint(a,b)
    return nb

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


def Replay(message: str):
    while message == "yes":
        nb_AI: int = get_random()
        essai: int = 10
        while True:
            essai = essai - 1
            nb: int = Ask_only_number("Donner un nombre: ")
            result: str = More_or_Less(nb, nb_AI, essai)
            print(result,"il vous reste",str(essai), "essai")

            if result == "Victoire" or result == "Perdu":
                message:str =response_replay("Voulez vous rejouer ? (yes/no): ")
                break
    print("Merci d'avoir joué !")


Replay("yes")
