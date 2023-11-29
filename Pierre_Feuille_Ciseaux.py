import Tools
def Game(message: str):
    response: [str] = ["y", "n"]
    while message == "y":
        print(Tools.Three_Wins_or_Loses())
        message = Tools.Response_replay(response)
    print("Merci d'avoir joué !")



Game("y")









