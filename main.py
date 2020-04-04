###################################################################################
# Team Members: Seth Warren
#               Carter Ray
#               Timothy Oliver
# 
# Project Summary: In this project we are going to be remaking and
#                  reimagining the card game "War" to include changes
#                  like a betting system, modifiers, and other
#                  improvements.                   
###################################################################################

from Tkinter import *
import time
from random import randint


######################
######## Main ########
######################

# a card class that will be used for the actual cards.
# this will make the interactions with cards a lot cleaner
# and easier to debug.
class Card(object):
    # a constructor that takes in suit, value, and image as instance variables
    def __init__(self, suit, rank, image):
        self.suit = suit
        self.rank = rank
        self.image = image

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        self._suit = value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    # a battle function that take in itself and an opposing card and compares to determine the winner
    def battle(self, opponent):

        if (self.rank < opponent.rank):
            winner = opponent
            loser = self
            return winner, loser

        elif (self.rank > opponent.rank):
            winner = self
            loser = opponent
            return winner, loser

        # in the case of a tie we just start another battle, however we need to find a way
        # to return the cards from both encounters, that however depends on how we initiate the battle
        elif (self.rank == opponent.rank):
            pass
        
    def __str__(self):
        s = "{} of {}".format(self.rank,self.suit)
        return s


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
    

# testing the card objects
c1 = Card("Spades", 1, "s1.png")
c2 = Card("Hearts", 4, "h4.png")

winner, loser = c1.battle(c2)

print winner

#########################################################

WIDTH = 1080
HEIGHT = 720
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("War")
g = Battle(window)
g.shuffle()
window.mainloop()


### NOTES ###

# this is a place where we can further document and explain our changes and additions because we are only allowed so much space to explain in GitHub
# just state your name and explain what you did and what you see the outcome being

# Seth: I created a new class Card. I made the suit and rank (or number of the card) as instance variables. My idea is that the Battle class seems to have too much going on
#       and we can break thing up into different classes and functions. I added a battle method to the Card class however I do believe it could be possible to create a function
#       outside of classes that could achieve the same thing.
#
#       As for the decks and such, I think it would be better to have those be dicitonaries outside of any class so they can be passed to any
#       class, funciton, or object that is needed. It might bring up complications with the GUI but I think we can find a way to work with it
#       cause it would make our lives a lot easier.
















