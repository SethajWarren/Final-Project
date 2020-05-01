#################################################################################
# This file holds the functions used to save and retrieve data for the game
#################################################################################

def save(bg, ownedMoney, cardBack):
    #save money and high scores, stuff unlocked, etc
    saveFile = open("save.txt", "w")
    s = "{} {} {}".format(bg, ownedMoney, cardBack)
    saveFile.write(s)
    saveFile.close()

def retrieve():
    saveFile = open("save.txt", "r")
    fileread = saveFile.read()
    bg, ownedMoney, cardBack = fileread.split()
    ownedMoney = int(ownedMoney)
    saveFile.close()

    print bg
    return bg, ownedMoney, cardBack

