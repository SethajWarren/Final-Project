#################################################################################
# This file holds the functions used to save and retrieve data for the game
#################################################################################

def save(money, difficulty, bg, cardBack):
    #save money and high scores, stuff unlocked, etc
    saveFile = open("save.txt", "w")
    s = "{} {} {} {}".format(money, difficulty, bg, cardBack)
    saveFile.write(s)
    saveFile.close()

def retrieve():
    saveFile = open("save.txt", "r")
    fileread = saveFile.read()
    money, difficulty, bg, cardBack = fileread.split()
    money = int(money)
    saveFile.close()

    return money, difficulty, bg, cardBack
