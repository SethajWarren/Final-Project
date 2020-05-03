#################################################################################
# This file holds the functions used to save and retrieve data for the game
#################################################################################

def save(bg, ownedMoney, cardBack, unlocks):
    #save money and high scores, stuff unlocked, etc
    saveFile = open("save.txt", "w")
    s = "{} {} {}\n".format(bg, ownedMoney, cardBack)
    for item in unlocks:
        s += str(item) + " "
    saveFile.write(s)
    saveFile.close()

def retrieve():
    saveFile = open("save.txt", "r")
    bg, ownedMoney, cardBack = saveFile.readline().split()
    unlocks = saveFile.readline().split()
    ownedMoney = int(ownedMoney)

    saveFile.close()

    return bg, ownedMoney, cardBack, unlocks

