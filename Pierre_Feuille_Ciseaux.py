import Tools
def Game():
    choice_user: str = Tools.Ask_PFC("Choisissez entre (Pierre:p, Feuille:f, Ciseaux:c): ")
    choice_AI: str = Tools.Get_random_PFC()
    equal: str = "Egalité"
    while choice_AI == choice_user:
        print("Choix de l'ordi:",choice_AI,equal)
    result: str = Tools.Win_Or_Lose_PFC(choice_user,choice_AI)
    print("Choix de l'ordi:",choice_AI,result)





Game()










