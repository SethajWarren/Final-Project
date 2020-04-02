########################################################################
# Team Members: Seth Warren
#               Carter Ray
#               Timothy Oliver
# 
# Project Summary: we make cool things yo
#                   
########################################################################

from Tkinter import *
import time
from random import randint


######################
######## Main ########
######################
class Card(object):
    val = {"s2":2, "c2":2, "d2":2, "h2":2, "s3":3, "c3":3, "d3":3, "h3":3, "s4":4, "c4":4, "d4":4, "h4":4, "s5":5, "c5":5, "d5":5, "h5":5, "s6":6, "c6":6, "d6":6, "h6":6, "s7":7, "c7":7, "d7":7, "h7":7, "s8":8, "c8":8, "d8":8, "h8":8, "s9":9, "c9":9, "d9":9, "h9":9, "s10":10, "c10":10, "d10":10, "h10":10, "sJ":11, "cJ":11, "dJ":11, "hJ":11, "sQ":12, "cQ":12, "dQ":12, "hQ":12, "sK":13, "cK":13, "dK":13, "hK":13, "sA":14, "cA":14, "dA":14, "hA":14}
    def __init__(self, name, image = None):
        self.name = name
        self.image = image
        self.value = Card.val[name]
    
    def __str__(self):
        return self.name
        

class Battle(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg = "olivedrab")
        self.pack(fill = BOTH, expand = 1)

    def mainScreen(self):
        #main screen: options to play, go to store, equip modifiers: (eg. table backgrounds, deck colors)
        pass
    
    def store(self):
        #option to purchase in-game items, decks, backgrounds
        pass

    def options(self):
        #settings screen, equip modifiers
        pass

    def save(self):
        #save money and high scores, stuff unlocked, etc
        pass

    def bet(self):
        #bet from your pool of money, calculates the money you get after each hand
        pass

    def setupCards(self):
        s2 = Card("s2")
        c2 = Card("c2")
        d2 = Card("d2")
        h2 = Card("h2")
        s3 = Card("s3")
        c3 = Card("c3")
        d3 = Card("d3")
        h3 = Card("h3")
        s4 = Card("s4")
        c4 = Card("c4")
        d4 = Card("d4")
        h4 = Card("h4")
        s5 = Card("s5")
        c5 = Card("c5")
        d5 = Card("d5")
        h5 = Card("h5")
        s6 = Card("s6")
        c6 = Card("c6")
        d6 = Card("s6")
        h6 = Card("h6")
        s7 = Card("s7")
        c7 = Card("c7")
        d7 = Card("d7")
        h7 = Card("h7")
        s8 = Card("s8")
        c8 = Card("c8")
        d8 = Card("d8")
        h8 = Card("h8")
        s9 = Card("s9")
        c9 = Card("c9")
        d9 = Card("d9")
        h9 = Card("h9")
        s10 = Card("s10")
        c10 = Card("c10")
        d10 = Card("d10")
        h10 = Card("h10")
        sJ = Card("sJ")
        cJ = Card("cJ")
        dJ = Card("dJ")
        hJ = Card("hJ")
        sQ = Card("sQ")
        cQ = Card("cQ")
        dQ = Card("dQ")
        hQ = Card("hQ")
        sK = Card("sK")
        cK = Card("cK")
        dK = Card("dK")
        hK = Card("hK")
        sA = Card("sA")
        cA = Card("cA")
        dA = Card("dA")
        hA = Card("hA")

        Battle.myCard

    def shuffle(self):
        #starts the game by shuffling and distributing cards
        suits = ["spades", "clubs", "diamonds", "hearts"]
        mydeck = []
        otherdeck = []
        for i in range(26):
            x = randint(0, len(deck)-1)
            mydeck.append(deck[x])
            del deck[x]
            y = randint(0, len(deck)-1)
            otherdeck.append(deck[y])
            del deck[y]
        print deck
        print
        print mydeck
        print
        print otherdeck
        return mydeck, otherdeck

    def play():
        mydeck, otherdeck = shuffle()
        #runs the game
        pass
    

    
    
WIDTH = 1080
HEIGHT = 720
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("War")
g = Battle(window)
g.setupCards()
print hA
#window.mainloop()
