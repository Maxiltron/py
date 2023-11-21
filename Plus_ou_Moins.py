import random


def Ask_only_number(a: str):
    while a.isdigit() != True:
        a=input("Donnez un nombre: ")
    return int(a)







def Replay():
    rep: str = input("Voulez vous rejouer ? (Yes/No): ")
    while rep == "Yes":
        essai: int = 10
        a = input("Choisissez le nb minimum à deviner: ")
        a=Ask_only_number(a)
        b = input("Choisissez le nb maximum à deviner: ")
        b=Ask_only_number(b)
        c = input("Deviner le nombre mystère: ")
        nb=Ask_only_number(c)

        nb_mystère: int = random.randint(a,b)
        while nb != nb_mystère and essai > 1:
            if nb < nb_mystère:
                print("Plus", "(Il vous reste", str(essai - 1), "essai sur 10)")

            elif nb > nb_mystère:
                print("Moins", "(Il vous reste", str(essai - 1), "essai sur 10)")

            essai = essai - 1
            d: int = int(input("Deviner le nombre mystère: "))
            nb=Ask_only_number(d)
        if essai == 1:
            print("Perdu")
            rep: str = input("Voulez vous rejouer ? (Yes/No): ")
        else:
            print("Victoire")
            rep: str = input("Voulez vous rejouer ? (Yes/No): ")
    else :
        print("Merci d'avoir joué !")


def More_or_Less():
    nb: int = int(input("Deviner le nombre mystère: "))
    nb_mystère: int = random.randint(a, b)
    while nb != n and c > 1:
        if nb < n:
            print("Plus","(Il vous reste", str(c-1), "essai sur 10)")

        elif nb > n:
            print("Moins","(Il vous reste", str(c-1), "essai sur 10)")

        c=c-1
        nb: int = int(input("Deviner le nombre mystère: "))
    if c == 1:
        print("Perdu")
        Replay()
    else :
        print("Victoire")
        Replay()







Replay()
