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
        return "/Pictures" + self._image

    @image.setter
    def image(self, value):
        self._image = value

    def __str__(self):
        value = self.rank
        if (self.rank == 11):
            value = "Jack"
        if (self.rank == 12):
            value = "Queen"
        if (self.rank == 13):
            value = "King"
        if (self.rank == 14):
            value = "Ace"
        s = "{} of {}".format(value, self.suit)
        return s
    

class Battle(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

    def main(self):
        self.retrieve()
        #self.mainScreen()
        self.gameScreen()
        pass
    
    def mainScreen(self):
        pass
        
    def gameScreen(self):
        #game screen
        Battle.bg = "darkolivegreen"

        Battle.currentBet = 100

        superBetUp = Button(self.master, bg = Battle.bg, text="superBetUp.gif", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        superBetUp.grid(row=0, column=0, sticky=N+S+E+W)
        
        betUp = Button(self.master, bg = Battle.bg, text="betUp.gif", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        betUp.grid(row=1, column=0, sticky=N+S+E+W)
        
        currentBet = Label(self.master, bg = Battle.bg, text=str(Battle.currentBet), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        currentBet.grid(row=2, column=0, sticky=N+S+E+W)
        
        betDown = Button(self.master, bg = Battle.bg, text="betDown.gif", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        betDown.grid(row=3, column=0, sticky=N+S+E+W)
        
        superBetDown = Button(self.master, bg = Battle.bg, text="superBetDown.gif", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        superBetDown.grid(row=4, column=0, sticky=N+S+E+W)

        totalMoney = Label(self.master, bg = Battle.bg, text=str(Battle.money), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        totalMoney.grid(row=5, column=0, sticky=N+S+E+W)
        
        oppCard = Label(self.master, bg = Battle.bg, text="Battle.opponentCard.image", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        oppCard.grid(row=0, column=2, rowspan=3, sticky=N+S+E+W)
        
        oppDeck = Label(self.master, bg = Battle.bg, image = Card.back, borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        oppDeck.grid(row=0, column=3, rowspan=3, sticky=N+S+E+W)

        playerCard = Label(self.master, bg = Battle.bg, text = "Battle.playerCard.image" , borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        playerCard.grid(row=3, column=2, rowspan=3, sticky=N+S+E+W)
        
        playerDeck = Button(self.master, bg = Battle.bg, image = Card.back, borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        playerDeck.grid(row=3, column=3, rowspan=3, sticky=N+S+E+W)
    
    def store(self):
        #option to purchase in-game items, decks, backgrounds
        pass

    def options(self):
        pass

    def save(self):
        savefile = open("save.txt", "w")
        s = "{} {} {} {}".format(money, difficulty, color, cardback)
        savefile.write(s)
        savefile.close()

    def retrieve(self):
        savefile = open("save.txt", "r")
        fileread = savefile.read()
        Battle.money, Battle.difficulty, Battle.color, Battle.cardback = fileread.split()
        Battle.money = int(Battle.money)
        savefile.close()

    def bet(self):
        #bet from your pool of money, calculates the money you get after each hand
        pass

    def shuffle(self, Odeck, deck):
        deck_ = []
        while (len(Odeck) > 0):
            deck_.append(Odeck[0])
            del Odeck[0]
        while (len(deck) > 0):
            x = randint(0, len(deck)-1)
            deck_.append(deck[x])
            del deck[x]
        if (len(deck_) == 0):
            self.endGame()
            
        return deck_

    def endGame(self):
        Battle.going = False
        Winner = ""
        if (len(Battle.me) > len(Battle.opponent)):
            Winner = "me"
        if (len(Battle.me) < len(Battle.opponent)):
            Winner = "opponent"
        print Winner
        print Battle.i
        print len(Battle.me) + len(Battle.meQ)
        print len(Battle.opponent) + len(Battle.oppQ)
        
    # a battle function that take in itself and an opposing card and compares to determine the winner
    def battle(self):
        myCard = Battle.me[0]
        oppCard = Battle.opponent[0]
        del Battle.me[0]
        del Battle.opponent[0]
        
        if (myCard.rank < oppCard.rank):
            winner = "opponent"
            Battle.oppQ.append(myCard)
            Battle.oppQ.append(oppCard)

        elif (myCard.rank > oppCard.rank):
            winner = "me"
            Battle.meQ.append(myCard)
            Battle.meQ.append(oppCard)
        
        elif (myCard.rank == oppCard.rank):
            megabattle = [myCard, oppCard]
            while (True):
                #adds the queue to the players decks if  they dont have enough to mega battle
                if (len(Battle.me) < 4):
                    Battle.me = self.shuffle(Battle.me, Battle.meQ)
                if (len(Battle.opponent) < 4):
                    Battle.opponent = self.shuffle(Battle.opponent, Battle.oppQ)

                #if they still dont have enough, they battle with however many they have
                if (len(Battle.me) < 4 and len(Battle.me) > 0):
                    for i in range(len(Battle.me) - 2):
                        megabattle.append(Battle.me[0])
                        del Battle.me[0]
                else:
                    for i in range(3):
                        megabattle.append(Battle.me[0])
                        del Battle.me[0]
 
                if (len(Battle.opponent) < 4 and len(Battle.opponent) > 0):
                    for i in range(len(Battle.opponent) - 2):
                        megabattle.append(Battle.opponent[0])
                        del Battle.opponent[0]
                else:
                    for i in range(3):
                        megabattle.append(Battle.opponent[0])
                        del Battle.opponent[0]

                print len(Battle.me)
                print len(Battle.opponent)
                
                if (len(Battle.me) > 0):
                    myCard = Battle.me[0]
                    del Battle.me[0]
                    megabattle.append(myCard)
                    
                if (len(Battle.opponent) > 0):
                    oppCard = Battle.opponent[0]
                    del Battle.opponent[0]
                    megabattle.append(oppCard)
                
                
                if (myCard.rank < oppCard.rank):
                    winner = "opponent"
                    for item in megabattle:
                        Battle.oppQ.append(item)
                    break

                elif (myCard.rank > oppCard.rank):
                    winner = "me"
                    for item in megabattle:
                        Battle.meQ.append(item)
                    break
                
                                
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

        Battle.meQ = []
        Battle.oppQ = []

        Battle.going = True
    
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
            
        return mydeck, oppdeck

    def play(self):
        Battle.i = 0
        self.createCards()
        self.gameScreen()

        #right now this just battles 10 times so you can see what's going on.
        while (True):
            Battle.i += 1
            self.battle()
            if(len(Battle.me) == 0):
                if (len(Battle.meQ) == 0):
                    self.endGame()
                    break
                else:
                    Battle.me = self.shuffle(Battle.me, Battle.meQ)
                    
            if(len(Battle.opponent) == 0):
                if (len(Battle.oppQ) == 0):
                    self.endGame()
                    break
                else:
                    Battle.opponent = self.shuffle(Battle.opponent, Battle.oppQ)
            
        #runs the game
    


#########################################################

WIDTH = 1080
HEIGHT = 720
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("War")
g = Battle(window)
g.main()
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

# Seth: I modeled the GUI but it is nowhere close to being done. The background for all the GUI components so far are set to a variable in the game class, this will allow us to easily
#       change the background for the entire GUI when we impliment cosmetics. As you can see the GUI does not use any pictures yet but instead displays the text that will be used to
#       refer to each image. For some reason the back.gif file was not working so I did the same for that too. I put all the pictures in a file named Pictures, so we will need to research
#       how to acess that file for pictures in python but I think we can do it. Lastly, I converted all the images we need into .gif format to work. I dont know why I didn't do that to
#       begin with but it's done.
#
#       As for the next steps would be to fully flesh out the backend of the game. This will make the GUI much easier to program as we would be able to refer to
#       pre-existing variables and methods to use with the GUI instead of having to make iit up as the GUI is created. So that being said, the battle system is close to being done so
#       finishing that and creating the betting system are our top priorities right now. After that and the GUI we can get working on saving and reading to a file. Carter and Tim have
#       done some work on that already and it doesn't seem to be that difficult.

# Carter: Handles ties, and how you win.,
#         if the player runs out of cards, etc.
#         added some random variables that are tracking the number of games played, those will be removed later
#         NEEDS: user input to move on, gui, etc.
#         This is just the base game logic working. if you see any issues (probably are some) let me know












