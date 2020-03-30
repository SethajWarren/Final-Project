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
        deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]
        rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
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
window.mainloop()
