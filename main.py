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
from random import randint
from save import *
from betSys import *
from card import *

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
        self._image = "Pictures/" + value

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
        
##################################################################################################
#############################################  GAME  #############################################
##################################################################################################

                        ##################### SETUP  #####################
    def createCards(self):
        Battle.money = 10
        s2 = Card("Spades", 2, "s2.gif")
        c2 = Card("Clubs", 2, "c2.gif")
        d2 = Card("Diamonds", 2,"d2.gif")
        h2 = Card("Hearts", 2, "h2.gif")
        s3 = Card("Spades", 3, "s3.gif")
        c3 = Card("Clubs", 3, "c3.gif")
        d3 = Card("Diamonds", 3,"d3.gif")
        h3 = Card("Hearts", 3, "h3.gif")
        s4 = Card("Spades", 4, "s4.gif")
        c4 = Card("Clubs", 4, "c4.gif")
        d4 = Card("Diamonds", 4,"d4.gif")
        h4 = Card("Hearts", 4, "h4.gif")
        s5 = Card("Spades", 5, "s5.gif")
        c5 = Card("Clubs", 5, "c5.gif")
        d5 = Card("Diamonds", 5,"d5.gif")
        h5 = Card("Hearts", 5, "h5.gif")
        s6 = Card("Spades", 6, "s6.gif")
        c6 = Card("Clubs", 6, "c6.gif")
        d6 = Card("Diamonds", 6,"d6.gif")
        h6 = Card("Hearts", 6, "h6.gif")
        s7 = Card("Spades", 7, "s2.gif")
        c7 = Card("Clubs", 7, "c7.gif")
        d7 = Card("Diamonds", 7,"d7.gif")
        h7 = Card("Hearts", 7, "h7.gif")
        s8 = Card("Spades", 8, "s8.gif")
        c8 = Card("Clubs", 8, "c8.gif")
        d8 = Card("Diamonds", 8,"d8.gif")
        h8 = Card("Hearts", 8, "h8.gif")
        s9 = Card("Spades", 9, "s9.gif")
        c9 = Card("Clubs", 9, "c9.gif")
        d9 = Card("Diamonds", 9,"d9.gif")
        h9 = Card("Hearts", 9, "h9.gif")
        s10 = Card("Spades", 10, "s10.gif")
        c10 = Card("Clubs", 10, "c10.gif")
        d10 = Card("Diamonds", 10,"d10.gif")
        h10 = Card("Hearts", 10, "h10.gif")
        sJ = Card("Spades", 11, "sJ.gif")
        cJ = Card("Clubs", 11, "cJ.gif")
        dJ = Card("Diamonds", 11,"dJ.gif")
        hJ = Card("Hearts", 11, "hJ.gif")
        sQ = Card("Spades", 12, "sQ.gif")
        cQ = Card("Clubs", 12, "cQ.gif")
        dQ = Card("Diamonds", 12,"dQ.gif")
        hQ = Card("Hearts", 12, "hQ.gif")
        sK = Card("Spades", 13, "sK.gif")
        cK = Card("Clubs", 13, "cK.gif")
        dK = Card("Diamonds", 13,"dK.gif")
        hK = Card("Hearts", 13, "hK.gif")
        sA = Card("Spades", 14, "sA.gif")
        cA = Card("Clubs", 14, "cA.gif")
        dA = Card("Diamonds", 14,"dA.gif")
        hA = Card("Hearts", 14, "hA.gif")
        
        deck = [s2, c2, d2, h2, s3, c3, d3, h3, s4, c4, d4, h4, s5, c5, d5, h5, s6, c6, d6, h6, s7, c7, d7, h7, s8, c8, d8, h8, s9, c9, d9, h9, s10, c10, d10, h10, sJ, cJ, dJ, hJ, sQ, cQ, dQ, hQ, sK, cK, dK, hK, sA, cA, dA, hA]
        Battle.me, Battle.opponent = shuffleStart(self, deck)

        Battle.meQ = []
        Battle.oppQ = []

        playerCard = Label(self.master, bg = Battle.bg, text = "\t\t\t\t\t\t", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        playerCard.grid(row=7, column=2, sticky=NSEW, rowspan = 6, ipadx = 20, ipady = 20)
        
        oppCard = Label(self.master, bg = Battle.bg, text = "\t\t\t\t\t\t", borderwidth=0)
        oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6, ipadx = 20, ipady = 20)       

        Battle.megabattle = []


                        #####################  GAME  #####################
        
    def battle(self, winner = None):
        try:
            if(len(Battle.me) == 0):
                Battle.me = shuffle(self, Battle.me, Battle.meQ)

            if(len(Battle.opponent) == 0):
                Battle.opponent = shuffle(self, Battle.opponent, Battle.oppQ)
                    
            myCard = Battle.me[0]
            oppCard = Battle.opponent[0]
            self.gameScreen(winner)
            
            if (myCard.rank < oppCard.rank):
                winner = "opponent"
                Battle.oppQ.append(myCard)
                Battle.oppQ.append(oppCard)

            if (myCard.rank > oppCard.rank):
                winner = "me"
                Battle.money += 1
                print Battle.money
                Battle.meQ.append(myCard)
                Battle.meQ.append(oppCard)
            
            if (myCard.rank == oppCard.rank):
                self.gameScreen("tie")
                battleButton = Button(self.master, bg = Battle.bg, text = "BATTLE", borderwidth=0, highlightthickness=0, activebackground=Battle.bg, command = lambda: self.megaBattle())
                battleButton.grid(row = 6, column = 2, sticky = NSEW, columnspan = 2)
            else:
                Battle.currentbet, Battle.money = bet(winner, Battle.money, Battle.currentBet)
                                          
                del Battle.me[0]
                del Battle.opponent[0]
                print winner
                print "\t" + str(myCard),
                print "\t" + str(oppCard)
                
        except:
            self.endGame()
                
    def megaBattle(self):
        megabattle = []
        Battle.megabattle.append(Battle.me[0])
        Battle.megabattle.append(Battle.opponent[0])
        del Battle.me[0]
        del Battle.opponent[0]

        if (len(Battle.me) < 4):
            Battle.me = shuffle(self, Battle.me, Battle.meQ)
            print "me shuffled"
        if (len(Battle.opponent) < 4):
            Battle.opponent = shuffle(self, Battle.opponent, Battle.oppQ)
            print "opp shuffled"

    #if they still dont have enough, they battle with however many they have
        if (len(Battle.me) < 4):
            myMega = len(Battle.me) -2
        else:
            myMega = 3
            
        clicks = 0
        self.battleScreen(myMega, clicks)


    def megabattle2(self, myMega, clicks):
        if (clicks < myMega):
            clicks += 1
            Battle.megabattle.append(Battle.me[0])
            del Battle.me[0]
            self.battleScreen(myMega, clicks)
        elif (clicks == myMega):
            if (len(Battle.opponent) < 4):
                for i in range(len(Battle.opponent) - 2):
                    Battle.megabattle.append(Battle.opponent[0])
                    del Battle.opponent[0]
            else:
                for i in range(3):
                    Battle.megabattle.append(Battle.opponent[0])
                    del Battle.opponent[0]
                    
            clicks += 1
            self.battleScreen(myMega, clicks)
            
        if (clicks == myMega + 1):
            
            myCard = Battle.me[0]
            oppCard = Battle.opponent[0]
            Battle.megabattle.append(myCard)
            Battle.megabattle.append(oppCard)

            
            if (myCard.rank < oppCard.rank):
                winner = "opponent"
                for item in Battle.megabattle:
                    Battle.oppQ.append(item)
                
            if (myCard.rank > oppCard.rank):
                winner = "me"
                for item in Battle.megabattle:
                    Battle.meQ.append(item)
                Battle.money += 1
                

            if (myCard.rank == oppCard.rank):
                Battle.megabattle.remove(myCard)
                Battle.megabattle.remove(oppCard)
                winner = "tie"
                self.battle(winner)
            else:
                Battle.currentBet, Battle.money = bet(winner, Battle.money, Battle.currentBet)
                self.gameScreen()
                del Battle.me[0]
                del Battle.opponent[0]
                Battle.megabattle = []

            print winner
            print "\t" + str(myCard)
            print "\t" + str(oppCard)

    def bet(self, value, money, currentBet):
        #bet from your pool of money, calculates the money you get after each hand
        Battle.currentBet, Battle.money = bet(value, money, currentBet)

        # overwrites the current label in the GUI to display the players bet
        currentBet = Label(self.master, bg = Battle.bg, text = "+" + str(Battle.currentBet), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        currentBet.grid(row=6, column=0, sticky = NSEW)

        # overwrites the current label in the GUI to display the players currency
        money = Label(self.master, bg = Battle.bg, text = "Money:\n" + str(Battle.money), font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, padx = 50)
        money.grid(row=0, column=0, sticky = NSEW, rowspan = 4)

    def endGame(self):
        Battle.going = False
        Battle.ownedMoney += Battle.money
        if (len(Battle.me)+ len(Battle.meQ) > len(Battle.opponent) + len(Battle.oppQ)):
            Battle.money += 100
            endText = "Congratulations!\n You Won!"
            endText += "\n You earned ${}!".format(Battle.money)
        if (len(Battle.me) + len(Battle.meQ) < len(Battle.opponent)+ len(Battle.oppQ)):
            endText = "Aw, too Bad...\nBetter Luck Next Time"
            
        save(Battle.bg, Battle.ownedMoney, Card.cardBack)
        
        gameover = Label(self.master, bg = Battle.bg, text = endText, font=("Arial", 50), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        gameover.grid(row=0, column=0, sticky=NSEW, rowspan = 13, columnspan = 4, ipadx = 20, ipady = 20)


                        ##################### SCREENS #####################
    def gameScreen(self, winner = None):
        if (Battle.going == None):
            self.createCards()
            
            Battle.currentBet = 0
            
            img = PhotoImage(file = "Pictures/superBetUp.gif")
            superBetUp = Button(self.master, bg = Battle.bg, image = img, borderwidth=0, activebackground=Battle.bg,\
                                command = lambda:self.bet("supUp", Battle.money, Battle.currentBet))
            superBetUp.image = img
            superBetUp.grid(row=4, column=0, sticky = NSEW)

            img = PhotoImage(file = "Pictures/betUp.gif")
            betUp = Button(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg,\
                           command = lambda:self.bet("up", Battle.money, Battle.currentBet))
            betUp.image = img
            betUp.grid(row=5, column=0, sticky = NSEW)

            img = PhotoImage(file = "Pictures/betDown.gif")
            betDown = Button(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg,\
                             command = lambda:self.bet("down", Battle.money, Battle.currentBet))
            betDown.image = img
            betDown.grid(row=7, column=0, sticky = NSEW)

            img = PhotoImage(file = "Pictures/superBetDown.gif")
            superBetDown = Button(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg,\
                                  command = lambda:self.bet("supDown", Battle.money, Battle.currentBet))
            superBetDown.image = img
            superBetDown.grid(row=8, column=0, sticky = NSEW)


            text = Label(self.master, bg = Battle.bg, text = "", borderwidth=0, highlightthickness=0, activebackground=Battle.bg, padx = 50)
            text.grid(row=9, column=0, sticky = NSEW, rowspan = 4)

            battleButton = Label(self.master, bg = Battle.bg, text = "", borderwidth=0, highlightthickness=0, activebackground=Battle.bg, padx = 50)
            battleButton.grid(row=6, column = 2, sticky = NSEW, columnspan = 2)
            
            oppCard = Label(self.master, bg = Battle.bg, text = "", borderwidth=0)
            oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6, ipadx = 20, ipady = 20)
            
            playerCard = Label(self.master, bg = Battle.bg, text = "", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
            playerCard.grid(row=7, column=2, sticky=NSEW, rowspan = 6, ipadx = 20, ipady = 20)
            
            Battle.going = True
            
            i = 0
        else:
            img = PhotoImage(file = Battle.opponent[0].image)
            oppCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
            oppCard.image = img
            oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6, ipadx = 20, ipady = 20)
            
            img = PhotoImage(file = Battle.me[0].image)
            playerCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
            playerCard.image = img
            playerCard.grid(row=7, column=2, sticky=NSEW, rowspan = 6, ipadx = 20, ipady = 20)

            i = 1

        totalMoney = Label(self.master, bg = Battle.bg, text = "Money:\n" + str(Battle.money), font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, padx = 50)
        totalMoney.grid(row=0, column=0, sticky = NSEW, rowspan = 4)

        currentBet = Label(self.master, bg = Battle.bg, text = "+" + str(Battle.currentBet), activebackground=Battle.bg)
        currentBet.grid(row=6, column=0, sticky = NSEW)


        img = PhotoImage(file = Card.cardBack)
        oppCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6)

        battleButton = Label(self.master, bg = Battle.bg, text = "", borderwidth=0, highlightthickness=0, activebackground=Battle.bg, padx = 50)
        battleButton.grid(row=6, column = 2, sticky = NSEW, columnspan = 2)


        img = PhotoImage(file = Card.cardBack)
        oppDeck = Label(self.master, bg = Battle.bg, image = img, compound = "center", font=("Arial", 50), text = (len(Battle.opponent) + len(Battle.oppQ)-i),activebackground=Battle.bg)
        oppDeck.image = img
        oppDeck.grid(row=0, column=3, sticky=N+S+E+W, rowspan = 6, ipadx = 20, ipady = 20)

        # deleted "player/oppCard.image = img" lines because the cardback remained behind the player's card when present
        img = PhotoImage(file = Card.cardBack)
        playerCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        playerCard.grid(row=7, column=2, sticky=S, rowspan = 6)
        playerDeck = Button(self.master, bg = Battle.bg, image = img, compound = "center", font=("Arial", 50), text = (len(Battle.me) + len(Battle.meQ)-i),borderwidth=0,\
                            highlightthickness=0, activebackground=Battle.bg, command = lambda: self.battle())
        playerDeck.image = img
        playerDeck.grid(row=7, column=3, rowspan = 6, sticky = NSEW, ipadx = 20, ipady = 20)

        if (winner != "tie"):
            pool = Label(self.master, bg = Battle.bg, font=("Arial", 20), text = "\t\t")
            pool.grid(row=0, column=1, sticky=N+S+E+W, rowspan = 13)

    def battleScreen(self, myMega, clicks):
        image = Card.cardBack.split(".")
        image = image[0] + "_." + image[1]    
        img = PhotoImage(file = image)
        pool = Label(self.master, bg = Battle.bg, image = img, compound = "center", font=("Arial", 20), text = len(Battle.megabattle), activebackground=Battle.bg)
        pool.image = img
        pool.grid(row=0, column=1, sticky=N+S+E+W, rowspan = 13)

        oppCard = Label(self.master, bg = Battle.bg, text = "", borderwidth=0)
        oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6, ipadx = 20, ipady = 20)
        
        playerCard = Label(self.master, bg = Battle.bg, text = "", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        playerCard.grid(row=7, column=2, sticky=NSEW, rowspan = 6, ipadx = 20, ipady = 20)

        # might need a pressed boolean so the initial gamescreen does not show the first battle's cards
        img = PhotoImage(file = Card.cardBack)
        playerDeck = Button(self.master, bg = Battle.bg, image = img, compound = "center", font=("Arial", 50), text = (len(Battle.me) + len(Battle.meQ)),borderwidth=0, highlightthickness=0, activebackground=Battle.bg, command = lambda: self.megabattle2(myMega, clicks))
        playerDeck.image = img
        playerDeck.grid(row=7, column=3, rowspan = 6, sticky = NSEW, ipadx = 20, ipady = 20)

    # update the money part of the GUI
    def updateCurrentMoney(self):
        totalMoney = Label(self.master, bg = Battle.bg, text = "Money:\n" + str(Battle.money), font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, padx = 50)
        totalMoney.grid(row=0, column=0, sticky = NSEW, rowspan = 4)

    # update the currentBet of the GUI
    def updateCurrentBet(self):
        currentBet = Label(self.master, bg = Battle.bg, text = "+" + str(Battle.currentBet), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        currentBet.grid(row=6, column=0, sticky = NSEW)

    # update the players' cards in the GUI
    def updatePlayers(self, card1, card2):
        img = PhotoImage(file = card1.image)
        oppCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        oppCard.image = img
        oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6)

        img = PhotoImage(file = card2.image)
        playerCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        playerCard.image = img
        playerCard.grid(row=7, column=2, sticky=S, rowspan = 6)


    def store(self):
        #option to purchase in-game items, decks, backgrounds
        pass

    def options(self):
        pass

    def save(self):
        #save money and high scores, stuff unlocked, etc
        saveFile = open("save.txt", "w")
        s = "{} {} {} {}".format(Battle.money, Battle.difficulty, Battle.bg, Card.cardBack)
        saveFile.write(s)
        saveFile.close()     

    def retrieve(self):
        # retireves the settings from the save.txt file
        saveFile = open("save.txt", "r")
        fileread = saveFile.read()
        Battle.money, Battle.difficulty, Battle.bg, Card.cardBack = fileread.split()
        Battle.money = int(Battle.money)
        saveFile.close()

    def bet(self, value=None):
        #bet from your pool of money, calculates the money you get after each hand
        battleButton = Label(self.master, bg = Battle.bg, text = " ", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        battleButton.grid(row=6, column = 2, sticky = NSEW, columnspan = 2)
        
        totalMoney = Label(self.master, bg = Battle.bg, text = "Money:\n" + str(Battle.money), font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, padx = 50)
        totalMoney.grid(row=0, column=0, sticky = NSEW, rowspan = 4)



##################################################################################################
#############################################  MAIN  #############################################
##################################################################################################


                        ##################### SCREENS #####################

    def mainScreen(self):
        Battle.bg, Battle.ownedMoney, Card.cardBack = retrieve()
        
        play = Button(self.master, text = "Play", borderwidth=0, highlightthickness=0, padx = 50, command = lambda:self.gameScreen())
        play.grid(row=0, column=3, sticky=NSEW, rowspan = 1, columnspan = 4, ipadx = 20, ipady = 20)

        options = Button(self.master, text = "Options", borderwidth=0, highlightthickness=0, padx = 50, command = lambda:self.optionsScreen())
        options.grid(row=1, column=3, sticky=NSEW, rowspan = 1, columnspan = 4, ipadx = 20, ipady = 20)

        # overwrites the current label in the GUI to display
        self.updateCurrentBet()
            
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
        store = Button(self.master, text = "Store", borderwidth=0, highlightthickness=0, padx = 50, command = lambda:self.storeScreen())
        store.grid(row=2, column=3, sticky=NSEW, rowspan = 1, columnspan = 4, ipadx = 20, ipady = 20)

        leave = Button(self.master, text = "Quit", borderwidth=0, highlightthickness=0, padx = 50, command = lambda:quit(0))
        leave.grid(row=3, column=3, sticky=NSEW, rowspan = 1, columnspan = 4, ipadx = 20, ipady = 20)

        
    # a battle function that take in itself and an opposing card and compares to determine the winner
    def battle(self):
        myCard = Battle.me[0]
        oppCard = Battle.opponent[0]
        del Battle.me[0]
        del Battle.opponent[0]
        # displays current my/oppCard
        self.updatePlayers(oppCard, myCard)
        Battle.going = None
        

                        #####################  CODE   #####################

            
    def storeScreen(self):
        pass
        ###need to add a gui and purchase options, automatically save the purchases somehow, etc
        

            

    def optionsScreen(self):
        ############## customization buttons ########################       
        custom1 = Button(self.master, bg = Battle.bg, text = "Grey", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
                         command = lambda:self.select("bg", "slategrey"))
        custom1.grid(row=0, column=3, sticky = NSEW)

        custom2 = Button(self.master, bg = Battle.bg, text = "Brown", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
                         command = lambda:self.select("bg", "sienna4"))
        custom2.grid(row=1, column=3, sticky = NSEW)

        custom3 = Button(self.master, bg = Battle.bg, text = "Blue", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
                         command = lambda:self.select("bg", "dodgerblue4"))
        custom3.grid(row=2, column=3, sticky = NSEW)

                
                                
    def createCards(self):
        s2 = Card("Spades", 2, "s2.gif")
        c2 = Card("Clubs", 2, "c2.gif")
        d2 = Card("Diamonds", 2,"d2.gif")
        h2 = Card("Hearts", 2, "h2.gif")
        s3 = Card("Spades", 3, "s3.gif")
        c3 = Card("Clubs", 3, "c3.gif")
        d3 = Card("Diamonds", 3,"d3.gif")
        h3 = Card("Hearts", 3, "h3.gif")
        s4 = Card("Spades", 4, "s4.gif")
        c4 = Card("Clubs", 4, "c4.gif")
        d4 = Card("Diamonds", 4,"d4.gif")
        h4 = Card("Hearts", 4, "h4.gif")
        s5 = Card("Spades", 5, "s5.gif")
        c5 = Card("Clubs", 5, "c5.gif")
        d5 = Card("Diamonds", 5,"d5.gif")
        h5 = Card("Hearts", 5, "h5.gif")
        s6 = Card("Spades", 6, "s6.gif")
        c6 = Card("Clubs", 6, "c6.gif")
        d6 = Card("Diamonds", 6,"d6.gif")
        h6 = Card("Hearts", 6, "h6.gif")
        s7 = Card("Spades", 7, "s2.gif")
        c7 = Card("Clubs", 7, "c7.gif")
        d7 = Card("Diamonds", 7,"d7.gif")
        h7 = Card("Hearts", 7, "h7.gif")
        s8 = Card("Spades", 8, "s8.gif")
        c8 = Card("Clubs", 8, "c8.gif")
        d8 = Card("Diamonds", 8,"d8.gif")
        h8 = Card("Hearts", 8, "h8.gif")
        s9 = Card("Spades", 9, "s9.gif")
        c9 = Card("Clubs", 9, "c9.gif")
        d9 = Card("Diamonds", 9,"d9.gif")
        h9 = Card("Hearts", 9, "h9.gif")
        s10 = Card("Spades", 10, "s10.gif")
        c10 = Card("Clubs", 10, "c10.gif")
        d10 = Card("Diamonds", 10,"d10.gif")
        h10 = Card("Hearts", 10, "h10.gif")
        sJ = Card("Spades", 11, "sJ.gif")
        cJ = Card("Clubs", 11, "cJ.gif")
        dJ = Card("Diamonds", 11,"dJ.gif")
        hJ = Card("Hearts", 11, "hJ.gif")
        sQ = Card("Spades", 12, "sQ.gif")
        cQ = Card("Clubs", 12, "cQ.gif")
        dQ = Card("Diamonds", 12,"dQ.gif")
        hQ = Card("Hearts", 12, "hQ.gif")
        sK = Card("Spades", 13, "sK.gif")
        cK = Card("Clubs", 13, "cK.gif")
        dK = Card("Diamonds", 13,"dK.gif")
        hK = Card("Hearts", 13, "hK.gif")
        sA = Card("Spades", 14, "sA.gif")
        cA = Card("Clubs", 14, "cA.gif")
        dA = Card("Diamonds", 14,"dA.gif")
        hA = Card("Hearts", 14, "hA.gif")
        
        deck = [s2, c2, d2, h2, s3, c3, d3, h3, s4, c4, d4, h4, s5, c5, d5, h5, s6, c6, d6, h6, s7, c7, d7, h7, s8, c8, d8, h8, s9, c9, d9, h9, s10, c10, d10, h10, sJ, cJ, dJ, hJ, sQ, cQ, dQ, hQ, sK, cK, dK, hK, sA, cA, dA, hA]
        Battle.me, Battle.opponent = self.shuffleStart(deck)
        custom4 = Button(self.master, bg = Battle.bg, text = "Green", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
                         command = lambda:self.select("bg", "darkolivegreen"))
        custom4.grid(row=3, column=3, sticky = NSEW)

        custom5 = Button(self.master, bg = Battle.bg, text = "Red", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
                         command = lambda:self.select("bg", "red4"))
        custom5.grid(row=4, column=3, sticky = NSEW)

        custom6 = Button(self.master, bg = Battle.bg, text = "Purple", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
                         command = lambda:self.select("bg", "purple4"))
        custom6.grid(row=5, column=3, sticky = NSEW)



        leave = Button(self.master, text = "Quit", borderwidth=0, highlightthickness=0, padx = 50, command = lambda:self.mainScreen())
        leave.grid(row=6, column=3, sticky=NSEW, rowspan = 1, columnspan = 4, ipadx = 20, ipady = 20)

    def select(self, item, value):
        if item == "bg":
            Battle.bg = value
        if item == "card":
            Card.cardBack = value

        print Battle.bg
        print Card.cardBack
        save(Battle.bg, Battle.ownedMoney, Card.cardBack)
        self.optionsScreen()

        

   

        
        

    
#########################################################

WIDTH = 1080
HEIGHT = 720
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("War")
g = Battle(window)
g.mainScreen()
window.mainloop()
Battle.going = None


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


# Timothy: Allowed the bet function to display the currentBet amount on the GUI screen
#           the (bet) buttons also had their borderwidth changed to account for more button-like looks
#           though they are quite large; I am considering making
#           an UpdateButton function to make that process easier later

# Timothy: made functions to update the GUI with new money and card appearances after each battle
#           Upon running battle, the player's and opponent's cards appear face up;
#           the size is a fraction of the cardback's;
#           However, the updateMoney function does not work after battles for some reason (it does
#            update with changing the bet if you alter the value it should state and when it runs)
#       

# Seth: Completed the save function with a save button that works, also cleaned up the betting system so now it displays the players money in real time along with letting the player
#       get money if they have no money. Additionally, I started the migration of functions to different files.
#
#       Me and Carter talked about it a bit and decided that moving fucntions out of the main.py file and into seperate .py files would clean up the code in here and also show better
#       knowledge of the python language. I have already done so for the save() and bet() functions. The plan is to get all backend functions that don't use GUI into other files. Then
#       possibly moving those GUI files into other files so the user runs a small run.py file and everyting from the other files come together.
#
#       If you noticed I have created multiple buttons for the GUI that are commented out. These are to serve as the customization that we have discussed. The plan is to create a main
#       screen to play and customize. I have wrote and tested them and they work fine, all that's left is to create the GUI for those screens. Carter told me he can take care of that
#       since he's the best with GUI.
#
#       I'll be continuing to migrate fucntions out of this main file over the next couple days and will note them in the pushes I make to the repository.
#
#       EDIT: Just got done migrating when I found a pretty weird one when there is a tie in the game. I didn't notice it while testing before hand and only noticed it after migrating.
#             which is odd because I didn't remove anything with the GUI while doing so. So check it out and see if you can find out what's wrong.

# Carter : Added barebones GUI for a lot of things. It needs prettying up and bug fixing. changed the money system to allow for only money earned in a battle can be used during that
#       battle. at the end it displays a boring screen about whether you won or lost, and awards you with your bet winnings + 100 coins for winning.
#       Changed it so the player starts out with 10 coins and gains 1 coin every hand win (incase you lose everything betting).
#       Organized the code into categories Main, Game, etc. with subcategories Screens and Code. Try to use this format to help easily find functions that we need to tweak.
#       I made the game automatically save the money at the end of the game / when any customizations are made. I feel this change prevents the user from forgetting to save their
#       hard gambled/earned money.
#
#       Side Note: if something like the bet money isnt updating properly, call just the money logo, if you call the screen later it can mess up how the game output lines up with the screen
#
#       Looking good guys.
#








