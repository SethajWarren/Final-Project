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

    #returns the name jack, queen, king, and ace instead of 11, 12, 13, and 14
    def getRank(self):
        value = self.rank
        if (self.rank == 11):
            value = "Jack"
        if (self.rank == 12):
            value = "Queen"
        if (self.rank == 13):
            value = "King"
        if (self.rank == 14):
            value = "Ace"
        return value
    
    def __str__(self):
        rankA = self.rank
        s = "{} of {}".format(self.getRank(), self.suit)
        return s
    

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

    # a battle function that take in itself and an opposing card and compares to determine the winner
    def battle(self):    
        myCard = Battle.me[0]
        oppCard = Battle.opponent[0]
        
        #gives the winner the 2 cards and puts them at the bottom of his deck,
        ###### this needs to be changed to have a second list of cards for each player, that when he runs out of cards his list of cards he got from winning is shuffled
        if (myCard.rank < oppCard.rank):
            winner = "opponent"
            loser = "me"
            Battle.opponent.append(myCard)
            Battle.opponent.append(oppCard)

        elif (myCard.rank > oppCard.rank):
            winner = "me"
            loser = "opponent"
            Battle.me.append(myCard)
            Battle.me.append(oppCard)

        # in the case of a tie we just start another battle, however we need to find a way
        # to return the cards from both encounters, that however depends on how we initiate the battle
        elif (myCard.rank == oppCard.rank):
            my3 = []
            other3 = []
            for i in range(3):
                winner = "tie"
                #tie stuff to be implemented sometime later
                pass

        print "My Card: {}".format(Battle.me[0])
        print "His Card: {}".format(Battle.opponent[0])

        
        del Battle.me[0]
        del Battle.opponent[0]
        print winner + "\n"
                                
    def createCards(self):
        s2 = Card("Spades", 2, "s2.png")
        c2 = Card("Clubs", 2, "c2.png")
        d2 = Card("Diamonds", 2,"d2.png")
        h2 = Card("Hearts", 2, "h2.png")
        s3 = Card("Spades", 3, "s3.png")
        c3 = Card("Clubs", 3, "c3.png")
        d3 = Card("Diamonds", 3,"d3.png")
        h3 = Card("Hearts", 3, "h3.png")
        s4 = Card("Spades", 4, "s4.png")
        c4 = Card("Clubs", 4, "c4.png")
        d4 = Card("Diamonds", 4,"d4.png")
        h4 = Card("Hearts", 4, "h4.png")
        s5 = Card("Spades", 5, "s5.png")
        c5 = Card("Clubs", 5, "c5.png")
        d5 = Card("Diamonds", 5,"d5.png")
        h5 = Card("Hearts", 5, "h5.png")
        s6 = Card("Spades", 6, "s6.png")
        c6 = Card("Clubs", 6, "c6.png")
        d6 = Card("Diamonds", 6,"d6.png")
        h6 = Card("Hearts", 6, "h6.png")
        s7 = Card("Spades", 7, "s2.png")
        c7 = Card("Clubs", 7, "c7.png")
        d7 = Card("Diamonds", 7,"d7.png")
        h7 = Card("Hearts", 7, "h7.png")
        s8 = Card("Spades", 8, "s8.png")
        c8 = Card("Clubs", 8, "c8.png")
        d8 = Card("Diamonds", 8,"d8.png")
        h8 = Card("Hearts", 8, "h8.png")
        s9 = Card("Spades", 9, "s9.png")
        c9 = Card("Clubs", 9, "c9.png")
        d9 = Card("Diamonds", 9,"d9.png")
        h9 = Card("Hearts", 9, "h9.png")
        s10 = Card("Spades", 10, "s10.png")
        c10 = Card("Clubs", 10, "c10.png")
        d10 = Card("Diamonds", 10,"d10.png")
        h10 = Card("Hearts", 10, "h10.png")
        sJ = Card("Spades", 11, "sJ.png")
        cJ = Card("Clubs", 11, "cJ.png")
        dJ = Card("Diamonds", 11,"dJ.png")
        hJ = Card("Hearts", 11, "hJ.png")
        sQ = Card("Spades", 12, "sQ.png")
        cQ = Card("Clubs", 12, "cQ.png")
        dQ = Card("Diamonds", 12,"dQ.png")
        hQ = Card("Hearts", 12, "hQ.png")
        sK = Card("Spades", 13, "sK.png")
        cK = Card("Clubs", 13, "cK.png")
        dK = Card("Diamonds", 13,"dK.png")
        hK = Card("Hearts", 13, "hK.png")
        sA = Card("Spades", 14, "sA.png")
        cA = Card("Clubs", 14, "cA.png")
        dA = Card("Diamonds", 14,"dA.png")
        hA = Card("Hearts", 14, "hA.png")
        
        deck = [s2, c2, d2, h2, s3, c3, d3, h3, s4, c4, d4, h4, s5, c5, d5, h5, s6, c6, d6, h6, s7, c7, d7, h7, s8, c8, d8, h8, s9, c9, d9, h9, s10, c10, d10, h10, sJ, cJ, dJ, hJ, sQ, cQ, dQ, hQ, sK, cK, dK, hK, sA, cA, dA, hA]
        Battle.me, Battle.opponent = self.shuffleStart(deck)


    def setImage(self):
        #sets the images of the cards on screen for the player to see
        pass
    
    def shuffleStart(self, deck):
        #starts the game by shuffling and distributing cards
        mydeck = []
        oppdeck = []
        for i in range(26):
            x = randint(0, len(deck)-1)
            mydeck.append(deck[x])
            del deck[x]
            y = randint(0, len(deck)-1)
            oppdeck.append(deck[y])
            del deck[y]
            
        print deck
        return mydeck, oppdeck

    def play(self):
        self.createCards()
        self.setImage()

        #right now this just battles 10 times so you can see what's going on.
        for i in range(10):
            self.battle()        
        #runs the game
        pass
    


#########################################################

WIDTH = 1080
HEIGHT = 720
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("War")
g = Battle(window)
g.play()
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


# Carter: I used Seth's card class and made it initialize all the cards and put them into a big list called deck, from there we can shuffle like we did before.
#         The cards are now able to be called everywhere because of the varibles Card.me and Card.opponent.
#         Card.me and Card.opponent contain a list of all of the card object in their respective decks.
#         Their decks are created by shuffling the main deck.
#         Things that need to be done: tie system that gets 3 cards from each opponent (but doesnt tell anyone which cards they are). Whoever wins on their 4th cards gets the whole pot
#         The GUI still needs to be done.














