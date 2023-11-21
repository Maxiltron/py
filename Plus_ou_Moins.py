import random

def Replay():
    rep: str = input("Voulez vous rejouer ? (Yes/No): ")
    while rep == "Yes":
        essai: int = 10
        a = input("Choisissez le nb minimum à deviner: ")
        b = input("Choisissez le nb maximum à deviner: ")
        n= input("Deviner le nombre mystère: ")
        while a.isdigit() != True and b.isdigit() != True and n.isdigit() != True:
            a = input("Choisissez le nb minimum à deviner: ")
            b = input("Choisissez le nb maximum à deviner: ")
            n= input("Deviner le nombre mystère: ")
        a=int(a)
        b=int(b)
        n=int(nb)
        nb_mystère: int = random.randint(a,b)
        while n != nb_mystère and essai > 1:
            if n < nb_mystère:
                print("Plus", "(Il vous reste", str(essai - 1), "essai sur 10)")

            elif n > nb_mystère:
                print("Moins", "(Il vous reste", str(essai - 1), "essai sur 10)")

            essai = essai - 1
            n: int = int(input("Deviner le nombre mystère: "))
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