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
    list_AI: [str] = ["p", "f", "c"]
    nb_AI: int = random.randint(0, 2)
    return list_AI[nb_AI]


def Win_Or_Lose_PFC(player: str, opponent: str):
    winner_list: [str] = ["pc", "fp", "cf"]
    value_1: str = "Victoire"
    value_2: str = "Défaite"
    play: str = player + opponent
    if play in winner_list:
        return value_1
    return value_2


def PFC(player: str, opponent: str) -> str:
    equal: str = "Egalité"
    if player == opponent:
        return equal
    value: str = Win_Or_Lose_PFC(player, opponent)
    return value


def Three_Wins_or_Loses():
    rounds: list[str] = []
    while rounds.count("1") != 3 and rounds.count("0") != 3:
        choice_user: str = Ask_PFC("Choisissez entre (Pierre:p, Feuille:f, Ciseaux:c): ")
        choice_AI: str = Get_random_PFC()
        result: str = PFC(choice_user, choice_AI)
        rounds.append(result)
        print(result, "Choix de l'ordi:", choice_AI)
        print("Wins:", str(rounds.count("Victoire")) + "/3")
        print("Loses:", str(rounds.count("Défaite")) + "/3")
    return rounds[len(rounds) - 1]


