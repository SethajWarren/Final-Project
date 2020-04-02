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
class Battle(Canvas):
    val = {"s2": "2", "c2":"2", "d2":2, "h2":2, "s3":3, "c3":3, "d3":3, "h3":3, "s4":4, "c4":4, "d4":4, "h4":4, "s5":5, "c5":5, "d5":5, "h5":5, "s6":6, "c6":6, "d6":6, "h6":6, "s7":7, "c7":7, "d7":7, "h7":7, "s8":8, "c8":8, "d8":8, "h8":8, "s9":9, "c9":9, "d9":9, "h9":9, "s10":10, "c10":10, "d10":10, "h10":10, "sJ":11, "cJ":11, "dJ":11, "hJ":11, "sQ":12, "cQ":12, "dQ":12, "hQ":12, "sK":13, "cK":13, "dK":13, "hK":13, "sA":14, "cA":14, "dA":14, "hA":14}
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

    def shuffle(self):
        #starts the game by shuffling and distributing cards
        deck = ["s2", "c2", "d2", "h2", "s3", "c3", "d3", "h3", "s4", "c4", "d4", "h4", "s5", "c5", "d5", "h5", "s6", "c6", "d6", "h6", "s7", "c7", "d7", "h7", "s8", "c8", "d8", "h8", "s9", "c9", "d9", "h9", "s10", "c10", "d10", "h10", "sJ", "cJ", "dJ", "hJ", "sQ", "cQ", "dQ", "hQ", "sK", "cK", "dK", "hK", "sA", "cA", "dA", "hA"]
        mydeck = []
        otherdeck = []
        for i in range(26):
            x = randint(0, len(deck)-1)
            mydeck.append(deck[x])
            del deck[x]
            y = randint(0, len(deck)-1)
            otherdeck.append(deck[y])
            del deck[y]

        #this is just an example on how to call all of the values that we have for cards
        for i in range(len(mydeck)):
            print mydeck[i],
            print Battle.val[mydeck[i]],
            image1 = mydeck[i]+".png"
            print image1,
            print "\t",
            print otherdeck[i],
            print Battle.val[otherdeck[i]],
            image2 = otherdeck[i]+".png"
            print image2

        
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
g.shuffle()
window.mainloop()
