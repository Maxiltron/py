import random
def Ask_only_number_1_2_3():
    a: str =input("Choisissez entre (1:Pierre, 2:Ciseaux, 3:Feuille): ")
    while a.isdigit() != True:
        a=input("Donnez un nombre: ")
    a: int=int(a)
    while a < 1 or a > 3:
        a: str =input("Donnez seulement (1,2 ou 3): ")
        while a.isdigit() != True:
            a = input("Donnez un nombre: ")
        a: int = int(a)
    return a
def Choice_user():
    user=Ask_only_number_1_2_3()
    return user

def Choice_AI():
    AI: int = random.randint(1,3)
    return AI

def Game():
    J1: int =Choice_user()
    AI: int =Choice_AI()
    if J1 == AI:
        print("Egalité")
    elif J1 == 1  and AI == 2:
        print("Gagné")
    elif J1 == 2  and AI == 3:
        print("Gagné")
    elif J1 == 3  and AI == 1:
        print("Gagné")
    else:
        print("Perdu")
    Replay()
def Replay():
    rep: str = input("Voulez vous rejouer ? (Yes/No): ")
    while rep == "Yes":
        J1: int = Choice_user()
        AI: int = Choice_AI()
        if J1 == AI:
            print("Egalité")
        elif J1 == 1 and AI == 2:
            print("Gagné")
        elif J1 == 2 and AI == 3:
            print("Gagné")
        elif J1 == 3 and AI == 1:
            print("Gagné")
        else:
            print("Perdu")
        rep: str = input("Voulez vous rejouer ? (Yes/No): ")
    print("Merci d'avoir joué !")

Game()