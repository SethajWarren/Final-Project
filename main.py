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
import tkMessageBox as mb
from random import randint
from save import *
from betSys import *
from card import *

######################
######## Main ########
######################

class Battle(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
##################################################################################################
#############################################  GAME  #############################################
##################################################################################################

                        ##################### SETUP  #####################
    def createCards(self):
        Battle.money = 10
        Battle.widgets = []
        
        
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
        s7 = Card("Spades", 7, "s7.gif")
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
            
            self.gameScreen("update")

            print myCard.rank
            print oppCard.rank
            if (myCard.rank < oppCard.rank):
                winner = "opponent"
                Battle.oppQ.append(myCard)
                Battle.oppQ.append(oppCard)
                Battle.loss += 1
                if (len(Battle.history) < 3):
                    Battle.history.append(str(myCard) + " vs. " + str(oppCard) + "\n(Loss)")
                else:
                    del Battle.history[0]
                    Battle.history.append(str(myCard) + " vs. " + str(oppCard) + "\n(Loss)")

            if (myCard.rank > oppCard.rank):
                winner = "me"
                Battle.meQ.append(myCard)
                Battle.meQ.append(oppCard)
                Battle.wins += 1
                if (len(Battle.history) < 3):
                    Battle.history.append(str(myCard) + " vs. " + str(oppCard) + "\n(Win)")
                else:
                    del Battle.history[0]
                    Battle.history.append(str(myCard) + " vs. " + str(oppCard) + "\n(Win)")
            
            if (myCard.rank == oppCard.rank):
                self.gameScreen("update")
                battleButton = Button(self.master, bg = Battle.bg, text = "BATTLE", font = ("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, command = lambda: self.megaBattle())
                battleButton.grid(row = 6, column = 2, sticky = NSEW, columnspan = 2)
                Battle.widgets.append(battleButton)
            else:
                self.bet(winner, Battle.money, Battle.currentBet)
                                          
                del Battle.me[0]
                del Battle.opponent[0]
                print winner
                print "\t" + str(myCard),
                print "\t" + str(oppCard)
                print Battle.wins
                print Battle.loss
                print Battle.history
                    
        except:
            Battle.going = False
            self.gameScreen("update")
                
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
            myMega = len(Battle.me) - 2
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
            
        elif (clicks > myMega):
            try:
                    
                myCard = Battle.me[0]
                oppCard = Battle.opponent[0]
                Battle.megabattle.append(myCard)
                Battle.megabattle.append(oppCard)

                
                if (myCard.rank < oppCard.rank):
                    winner = "opponent"
                    for item in Battle.megabattle:
                        Battle.oppQ.append(item)
                    Battle.wins += 1
                    if (len(Battle.history) < 3):
                        Battle.history.append(str(myCard) + " vs. " + str(oppCard) + "\n(Win)")
                    else:
                        del Battle.history[0]
                        Battle.history.append(str(myCard) + " vs. " + str(oppCard) + "\n(Win)")
                    
                    
                if (myCard.rank > oppCard.rank):
                    winner = "me"
                    for item in Battle.megabattle:
                        Battle.meQ.append(item)
                    Battle.wins += 1
                    if (len(Battle.history) < 3):
                        Battle.history.append(str(myCard) + " vs. " + str(oppCard) + "\n(Win)")
                    else:
                        del Battle.history[0]
                        Battle.history.append(str(myCard) + " vs. " + str(oppCard) + "\n(Win)")
                    

                if (myCard.rank == oppCard.rank):
                    Battle.megabattle.remove(myCard)
                    Battle.megabattle.remove(oppCard)
                    winner = "tie"
                    self.battle(winner)
                else:
                    self.bet(winner, Battle.money, Battle.currentBet)
                    self.gameScreen("update")
                    del Battle.me[0]
                    del Battle.opponent[0]
                    Battle.megabattle = []

                print winner
                print "\t" + str(myCard)
                print "\t" + str(oppCard)
            except:
                Battle.going = False
                self.gameScreen("update")

    def bet(self, value, money, currentBet):
        #bet from your pool of money, calculates the money you get after each hand
        Battle.currentBet, Battle.money = bet(value, money, currentBet)

        # overwrites the current label in the GUI to display the players bet
        currentBet = Label(self.master, bg = Battle.bg, font = ("Arial", 20), text = "+" + str(Battle.currentBet), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        currentBet.grid(row=6, column=0, sticky = NSEW)

        
            # overwrites the current label in the GUI to display the players currency
        moneyL = Label(self.master, bg = Battle.bg, text = "Coins\n" + str(Battle.money), font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, padx = 50)
        moneyL.grid(row=0, column=0, sticky = NSEW, rowspan = 4)
        

        Battle.widgets.append(currentBet)
        Battle.widgets.append(moneyL)
        

    def endGameScreen(self):
        Battle.going = False
        Battle.ownedMoney += Battle.money
        if (len(Battle.me)+ len(Battle.meQ) > len(Battle.opponent) + len(Battle.oppQ)):
            Battle.money += 100
            endText = "Congratulations!\n You Won!"
            endText += "\n You earned ${}!".format(Battle.money)
        if (len(Battle.me) + len(Battle.meQ) < len(Battle.opponent)+ len(Battle.oppQ)):
            endText = "Aw, too Bad...\nBetter Luck Next Time"
            
        save(Battle.bg, Battle.ownedMoney, Card.cardBack, Battle.unlocks)

        gameover = Label(self.master, bg = Battle.bg, text = endText, font=("Arial", 50), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        gameover.grid(row=0, column=0, sticky=NSEW, ipadx = 20, ipady = 20)

        stats = Label(self.master, bg = Battle.bg, text = "Wins: {}\n\nLosses: {}\n\nWin/Loss: {}".format(Battle.wins, Battle.loss, self.stats(Battle.wins,Battle.loss)), justify = LEFT,\
                      font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        stats.grid(row=1, column = 0, sticky=NSEW, ipadx = 20, ipady = 20)

        leave = Button(self.master, text = "Quit", borderwidth=0, highlightthickness=0, font=("Arial", 30), background = Battle.bg, command = lambda:self.changeScreen("mainScreen"))
        leave.grid(row=2, column=0, sticky=NSEW, ipadx = 20, ipady = 20)

        Battle.widgets = [gameover, leave, stats]


                        ##################### SCREENS #####################
        
    def gameScreen(self, update = "", winner = ""):
        print Battle.widgets
        if (update == "update"):
            while (len(Battle.widgets) > 0):
                Battle.widgets[0].destroy()
                del Battle.widgets[0]
                    
        if(Card.cardBack == "Pictures/blackcard.gif"):
            textcolor = "white"
        else:
            textcolor = "black"
            
        if (Battle.going == None):
            
            self.createCards()

            Battle.history = ["","",""]

            Battle.wins = 0
            Battle.loss = 0
            
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

            battleButton = Label(self.master, bg = Battle.bg, text = " ", font = ("Arial", 20), borderwidth=0, highlightthickness=0, pady = 10, activebackground=Battle.bg, padx = 50)
            battleButton.grid(row=6, column = 2, sticky = NSEW, columnspan = 2)
            
            oppCard = Label(self.master, bg = Battle.bg, text = "\t\t\t\t\t", borderwidth=0)
            oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6, ipadx = 35, ipady = 20)
            
            playerCard = Label(self.master, bg = Battle.bg, text = "\t\t\t\t\t", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
            playerCard.grid(row=7, column=2, sticky=NSEW, rowspan = 6, ipadx = 35, ipady = 20)

            pool = Label(self.master, bg = Battle.bg, text = "\t\t\t")
            pool.grid(row=0, column=1, sticky=N+S+E+W, rowspan = 13)

            leave = Button(self.master, bg = Battle.bg, text = "Quit", font = ("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, command = lambda: self.changeScreen("mainScreen"))
            leave.grid(row = 12, column = 4, sticky = NSEW, columnspan = 2, ipadx = 96)

            currentBet = Label(self.master, bg = Battle.bg,font=("Arial", 20), text = "+" + str(Battle.currentBet), activebackground=Battle.bg)
            currentBet.grid(row=6, column=0, sticky = NSEW)

            
            Battle.going = True
            
            i = 0

            
            Battle.persistWidgets = [superBetDown, betDown, betUp, superBetUp, text, battleButton, pool, leave, oppCard, playerCard, currentBet]


            
        elif (Battle.going == True):
        

            img = PhotoImage(file = Battle.opponent[0].image)
            oppCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
            oppCard.image = img
            oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6, ipadx = 30, ipady = 20)
            
            img = PhotoImage(file = Battle.me[0].image)
            playerCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
            playerCard.image = img
            playerCard.grid(row=7, column=2, sticky=NSEW, rowspan = 6, ipadx = 30, ipady = 20)

            widgets = [oppCard, playerCard]

            for item in widgets:
                Battle.widgets.append(item)

            i = 1
        else:
            i = 0
        
        
        img = PhotoImage(file = Card.cardBack)
        oppDeck = Label(self.master, bg = Battle.bg, image = img, compound = "center", fg = textcolor, font=("Arial", 50), text = (len(Battle.opponent) + len(Battle.oppQ)-i),activebackground=Battle.bg)
        oppDeck.image = img
        oppDeck.grid(row=0, column=3, sticky=N+S+E+W, rowspan = 6, ipadx = 35, ipady = 20)

        img = PhotoImage(file = Card.cardBack)
        playerDeck = Button(self.master, bg = Battle.bg, image = img, compound = "center", fg = textcolor, activeforeground = textcolor, font=("Arial", 50), text = (len(Battle.me) + len(Battle.meQ)-i),borderwidth=0,\
                            highlightthickness=0, activebackground=Battle.bg, command = lambda: self.battle())
        playerDeck.image = img
        playerDeck.grid(row=7, column=3, rowspan = 6, sticky = NSEW, ipadx = 35, ipady = 20)

        stats = Label(self.master, bg = Battle.bg, text = "Wins:" + str(Battle.wins) + "\n\n Losses:" + str(Battle.loss) + "\n\nW/L:" + str(self.stats(Battle.wins, Battle.loss)), \
                      font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        stats.grid(row=0, column = 4, sticky = NSEW, columnspan = 2, rowspan = 6)

        history = Label(self.master, bg = Battle.bg, text = Battle.history[0] + "\n\n"+Battle.history[1] + "\n\n"+Battle.history[2], justify = LEFT, font = ("Arial", 10), borderwidth = 0, highlightthickness = 0, activebackground = Battle.bg)
        history.grid(row=6, column = 4, sticky = NSEW, columnspan = 2, rowspan = 6)

        totalMoney = Label(self.master, bg = Battle.bg, text = "Coins:\n" + str(Battle.money), font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, padx = 50)
        totalMoney.grid(row=0, column=0, sticky = NSEW, rowspan = 4)

        
        widgets = [oppDeck, playerDeck, stats, history, totalMoney]


        for item in widgets:
            Battle.widgets.append(item)

        if(Battle.going == False):
            while len(Battle.persistWidgets) > 0:
                Battle.persistWidgets[0].destroy()
                del Battle.persistWidgets[0]
            self.changeScreen("endGameScreen")

    def battleScreen(self, myMega, clicks):

        if(Card.cardBack == "Pictures/blackcard.gif"):
            textcolor = "white"
        else:
            textcolor = "black"

        
        image = Card.cardBack.split(".")
        image = image[0] + "_." + image[1]    
        img = PhotoImage(file = image)
        pool = Label(self.master, bg = Battle.bg, image = img, compound = "center", font=("Arial", 20), fg = textcolor, text = len(Battle.megabattle), activebackground=Battle.bg)
        pool.image = img
        pool.grid(row=0, column=1, sticky=N+S+E+W, rowspan = 13)

        oppCard = Label(self.master, bg = Battle.bg, text = "", borderwidth=0)
        oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6, ipadx = 35, ipady = 20)
        
        playerCard = Label(self.master, bg = Battle.bg, text = "", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        playerCard.grid(row=7, column=2, sticky=NSEW, rowspan = 6, ipadx = 35, ipady = 20)

        img = PhotoImage(file = Card.cardBack)
        playerDeck = Button(self.master, bg = Battle.bg, image = img, activeforeground = textcolor, compound = "center", fg = textcolor, font=("Arial", 50), text = (len(Battle.me) + len(Battle.meQ)),borderwidth=0, highlightthickness=0, activebackground=Battle.bg, command = lambda: self.megabattle2(myMega, clicks))
        playerDeck.image = img
        playerDeck.grid(row=7, column=3, rowspan = 6, sticky = NSEW, ipadx = 35, ipady = 20)

        battleButton = Label(self.master, bg = Battle.bg, text = " ", font = ("Arial", 20), borderwidth=0, pady = 10, highlightthickness=0, activebackground=Battle.bg)
        battleButton.grid(row=6, column = 2, sticky = NSEW, columnspan = 2)
        

        widgets = [pool, oppCard, playerCard, playerDeck, battleButton]

        for item in widgets:
            Battle.widgets.append(item)



##################################################################################################
#############################################  MAIN  #############################################
##################################################################################################

                        ##################### SCREENS #####################

    def mainScreen(self):
        
        Battle.going = None
        
        Battle.bg, Battle.ownedMoney, Card.cardBack, Battle.unlocks = retrieve()

        leftSpace = Label(self.master, text = "\t", borderwidth=0, font=("Arial", 30), highlightthickness=0, background = Battle.bg)
        leftSpace.grid(row=0, column=0, sticky=NSEW, rowspan = 8, ipadx = 106)

        img = PhotoImage(file = "Pictures/WARtitle.gif")
        title = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
        title.image = img
        title.grid(row=1, column=1, sticky=NSEW, ipadx = 57)

        topSpace = Label(self.master, text = "\t", borderwidth=0, font=("Arial", 30), highlightthickness=0, background = Battle.bg)
        topSpace.grid(row=0, column=1, sticky=NSEW)

        midSpace = Label(self.master, text = "\t", borderwidth=0, font=("Arial", 30), highlightthickness=0, background = Battle.bg)
        midSpace.grid(row=2, column=1, sticky=NSEW, ipady = 12)

        money = Label(self.master, justify = "center", text = "Coins:\n" + str(Battle.ownedMoney), font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        money.grid(row=0, column = 2, sticky=NSEW, rowspan = 1, ipady = 10, ipadx = 20)

        rightSpace = Label(self.master, text = "\t", borderwidth=0, font=("Arial", 30), highlightthickness=0, background = Battle.bg)
        rightSpace.grid(row=1, column=2, sticky=NSEW, rowspan = 7, ipadx = 106)

        botSpace = Label(self.master, text = "\t", borderwidth=0, highlightthickness=0, font=("Arial", 20), background = Battle.bg)
        botSpace.grid(row=7, column=1, sticky=NSEW, ipadx = 20, ipady = 20)
        
        play = Button(self.master, text = "Play", borderwidth=0, highlightthickness=0, font=("Arial", 20), background = Battle.bg, command = lambda:self.changeScreen("gameScreen"))
        play.grid(row=3, column=1, sticky=NSEW, ipadx = 20, ipady = 20)

        options = Button(self.master, text = "Options", borderwidth=0, highlightthickness=0, font=("Arial", 20), background = Battle.bg, command = lambda:self.changeScreen("optionsScreen"))
        options.grid(row=4, column=1, sticky=NSEW, ipadx = 20, ipady = 20)

        store = Button(self.master, text = "Store", borderwidth=0, highlightthickness=0, font=("Arial", 20), background = Battle.bg, command = lambda:self.changeScreen("storeScreen"))
        store.grid(row=5, column=1, sticky=NSEW,  ipadx = 20, ipady = 20)

        leave = Button(self.master, text = "Quit", borderwidth=0, highlightthickness=0, font=("Arial", 20), background = Battle.bg, command = lambda:quit(0))
        leave.grid(row=6, column=1, sticky=NSEW, ipadx = 20, ipady = 20)



        Battle.widgets = [leftSpace, topSpace, midSpace, botSpace, rightSpace, play, options, store, leave, money, title]
        Battle.persistWidgets = []

                    
    def storeScreen(self):

        money = Label(self.master, justify = "center", text = "Coins:\n" + str(Battle.ownedMoney), font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        money.grid(row=0, column = 5, sticky=NSEW, rowspan = 1, ipady = 20, ipadx = 20)

        textB = Label(self.master, justify = "center", text = "New Backgrounds\n(1500 coins)", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        textB.grid(row=0, column = 1, sticky=NSEW, rowspan = 1, ipady = 10, ipadx = 15)

        textC = Label(self.master, justify = "center", text = "New Decks\n(5000 coins)", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        textC.grid(row=0, column = 3, sticky=NSEW, rowspan = 1, ipady = 10, ipadx = 21)

        space1 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = "black")
        space1.grid(row=0, column = 0, sticky=NSEW, rowspan = 13, ipadx = 1)

        space2 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = "black")
        space2.grid(row=0, column = 2, sticky=NSEW, rowspan = 13, ipadx = 1)

        space3 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = "black")
        space3.grid(row=0, column = 4, sticky=NSEW, rowspan = 13, ipadx = 1)

        space4 = Label(self.master, justify = "center", text = "", borderwidth=0, font = ("Arial", 1), highlightthickness=0, background = "black")
        space4.grid(row=1, column = 0, sticky=NSEW, columnspan = 13)

        space5 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = "black")
        space5.grid(row=0, column = 6, sticky=NSEW, rowspan = 13, ipadx = 1)

        space6 = Label(self.master, justify = "center", text = "", borderwidth=0, font = ("Arial", 1), highlightthickness=0, background = "black")
        space6.grid(row=11, column = 0, sticky=NSEW, columnspan = 6)
        

        grey = Button(self.master, bg = "slategrey", text = "Grey", font=("Arial", 20), borderwidth=0, highlightthickness=0, fg="black", padx = 25, pady = 5,\
                         command = lambda:self.purchase("bg", "slategrey"))
        

        brown = Button(self.master, bg = "sienna4", text = "Brown", font=("Arial", 20), borderwidth=0, highlightthickness=0, fg="black", padx = 25, pady = 5,\
                         command = lambda:self.purchase("bg", "sienna4"))


        blue = Button(self.master, bg = "dodgerblue4", text = "Blue", font=("Arial", 20), borderwidth=0, highlightthickness=0, fg="black", padx = 25, pady = 5,\
                         command = lambda:self.purchase("bg", "dodgerblue4"))
                

        red = Button(self.master, bg = "red4", text = "Red", font=("Arial", 20), borderwidth=0, highlightthickness=0, fg="black", padx = 25, pady = 5,\
                         command = lambda:self.purchase("bg", "red4"))
        

        purple = Button(self.master, bg = "purple4", text = "Purple", font=("Arial", 20), borderwidth=0, highlightthickness=0, fg="black", padx = 25, pady = 5,\
                         command = lambda:self.purchase("bg", "purple4"))

        #card backs
        img = PhotoImage(file = "Pictures/redcard_.gif")
        redCard = Button(self.master, image = img, bg = Battle.bg, borderwidth=0, highlightthickness=0, fg="black",\
                         command = lambda:self.purchase("card", "redcard.gif"))
        redCard.image = img

        img = PhotoImage(file = "Pictures/blackcard_.gif")
        blackCard = Button(self.master, image = img, bg = Battle.bg, borderwidth=0, highlightthickness=0, fg="black",\
                         command = lambda:self.purchase("card", "blackcard.gif"))
        blackCard.image = img



        bgs = {"slategrey": grey, "sienna4": brown, "dodgerblue4": blue, "red4": red, "purple4": purple}
        cbs = {"redcard.gif": redCard, "blackcard.gif": blackCard}

        
        b = 2
        c = 2
        for item in bgs:
            if item not in Battle.unlocks:
                bgs[item].grid(row = b, column = 1, sticky = NSEW)
                b += 1
        for item in cbs:
            if item not in Battle.unlocks:
                cbs[item].grid(row = c, column = 3, sticky = NSEW, rowspan = 2, ipadx = 50, ipady = 5)
                c += 2

        rs_1 = 11 - b
        rs_2 =  11 - c

        leave = Button(self.master, text = "Main Screen", font=("Arial", 20), borderwidth=0, bg = Battle.bg, highlightthickness=0, command = lambda:self.changeScreen("mainScreen"))
        leave.grid(row= 12, column=1, sticky=NSEW, ipady = 3)

        play = Button(self.master, text = "Play", font=("Arial", 20), borderwidth=0, bg = Battle.bg, highlightthickness=0, command = lambda:self.changeScreen("gameScreen"))
        play.grid(row= 12, column=5, sticky=NSEW, ipady = 3)

        options = Button(self.master, text = "Options", font=("Arial", 20), borderwidth=0, bg = Battle.bg, highlightthickness=0, command = lambda:self.changeScreen("optionsScreen"))
        options.grid(row= 12, column=3, sticky=NSEW, ipady = 3)

        empty4 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, bg = Battle.bg)
        empty4.grid(row=11, column = 7, sticky=NSEW, columnspan = 2, rowspan = 2)

        empty1 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = Battle.bg)
        empty1.grid(row = b, column = 1, sticky=NSEW, rowspan = rs_1)

        empty2 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = Battle.bg)
        empty2.grid(row = c, column = 3, sticky=NSEW, rowspan = rs_2)

        img = PhotoImage(file = "Pictures/suits.gif")
        empty3 = Label(self.master, image = img,borderwidth=0, highlightthickness=0, background = Battle.bg)
        empty3.image = img
        empty3.grid(row=2, column = 5, sticky=NSEW, rowspan = 9, ipadx = 10)


        previewText = Label(self.master, justify = "center", text = "Preview", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        previewText.grid(row=0, column = 7, columnspan = 2, sticky=NSEW, ipadx = 10)
        
        img = PhotoImage(file = Card.cardBack)
        previewCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
        previewCard.image = img
        previewCard.grid(row=2, column=8, sticky=NSEW, rowspan = 5, ipadx = 37, ipady = 50)

        image = Card.cardBack.split(".")
        image = image[0] + "_." + image[1]    
        img = PhotoImage(file = image)
        previewCard_ = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
        previewCard_.image = img
        previewCard_.grid(row=2, column=7, sticky=NSEW, rowspan = 5, ipadx = 55, ipady = 20)

        img = PhotoImage(file = "Pictures/superBetUp.gif")
        superBetUp = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, activebackground=Battle.bg)
        superBetUp.image = img
        superBetUp.grid(row=7, column=7, sticky = NSEW, ipady = 23)

        img = PhotoImage(file = "Pictures/superBetDown.gif")
        superBetDown = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, activebackground=Battle.bg)
        superBetDown.image = img
        superBetDown.grid(row = 8, column=7, sticky = NSEW, ipady = 23)

        previewtextText = Label(self.master, justify = "center", text = "Ace of Spades\nVS\n10 of Hearts", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        previewtextText.grid(row=7, column = 8, rowspan = 2, sticky=NSEW, ipadx = 10)
        
        Battle.widgets = [previewCard, previewCard_, superBetDown, superBetUp, empty4, previewtextText, grey, brown, blue, red, purple, redCard, leave, money, textB, textC, space1, space2, space3, space4, space5, space6, empty1, empty2, blackCard, empty3, play, options, previewText]

        grey.bind("<Enter>", lambda event:self.on_enter_color(event, "slate grey"))
        grey.bind("<Leave>", self.on_leave_color)

        brown.bind("<Enter>", lambda event:self.on_enter_color(event, "sienna4"))
        brown.bind("<Leave>", self.on_leave_color)
        
        blue.bind("<Enter>", lambda event:self.on_enter_color(event, "dodgerblue4"))
        blue.bind("<Leave>", self.on_leave_color)

        red.bind("<Enter>", lambda event:self.on_enter_color(event, "red4"))
        red.bind("<Leave>", self.on_leave_color)

        purple.bind("<Enter>", lambda event:self.on_enter_color(event, "purple4"))
        purple.bind("<Leave>", self.on_leave_color)

        redCard.bind("<Enter>", lambda event:self.on_enter_card(event, "Pictures/redcard.gif"))
        redCard.bind("<Leave>", self.on_leave_card)

        blackCard.bind("<Enter>", lambda event:self.on_enter_card(event, "Pictures/blackcard.gif"))
        blackCard.bind("<Leave>", self.on_leave_card)
        

    def on_enter_color(self, event, color):
        for i in range(6):
            Battle.widgets[i].configure(bg = color)
        
        
    def on_leave_color(self, enter):
        for i in range(6):
            Battle.widgets[i].configure(bg = Battle.bg)


    def on_enter_card(self, event, cardBack):
        img = PhotoImage(file = cardBack)
        Battle.widgets[0].configure(image = img)
        Battle.widgets[0].image = img

        image = cardBack.split(".")
        image = image[0] + "_." + image[1]    
        img = PhotoImage(file = image)
        Battle.widgets[1].configure(image = img)
        Battle.widgets[1].image = img
        
        
    def on_leave_card(self, enter):
        img = PhotoImage(file = Card.cardBack)
        Battle.widgets[0].configure(image = img)
        Battle.widgets[0].image = img

        image = Card.cardBack.split(".")
        image = image[0] + "_." + image[1]    
        img = PhotoImage(file = image)
        Battle.widgets[1].configure(image = img)
        Battle.widgets[1].image = img

        


                
    def purchase(self, item, value):
        if (item == "card"):
            price = 5000
                
        if (item == "bg"):
            price = 1500

            
        if(Battle.ownedMoney >= price):
            purchase = mb.askyesno(title = "Purchase Item", message = "Would you like to purchase this item?")
            if (purchase):
                Battle.ownedMoney -= price
                Battle.unlocks.append(value)
                self.select(item, value, "store")
                mb.showinfo("Purchase Item", "Item Purchased!")
                
        else:
            mb.showinfo("Purchase Item", "Sorry! You don't have enough money")
            
            
    def changeScreen(self, newScreen):
        while (len(Battle.persistWidgets) > 0):
            Battle.persistWidgets[0].destroy()
            del Battle.persistWidgets[0]

        
        while (len(Battle.widgets) > 0):
            Battle.widgets[0].destroy()
            del Battle.widgets[0]
        
            
        if (newScreen == "mainScreen"):
            self.mainScreen()
        if (newScreen == "gameScreen"):
            self.gameScreen()
        if (newScreen == "optionsScreen"):
            self.optionsScreen()
        if (newScreen == "storeScreen"):
            self.storeScreen()
        if (newScreen == "endGameScreen"):
            self.endGameScreen()
            

    def optionsScreen(self):
        #backgrounds
                
        grey = Button(self.master, bg = "slategrey", text = "Grey", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground="slategrey", fg="black", padx = 50,\
                         command = lambda:self.select("bg", "slategrey", "options"))
        

        brown = Button(self.master, bg = "sienna4", text = "Brown", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground="sienna4", fg="black", padx = 50,\
                         command = lambda:self.select("bg", "sienna4", "options"))


        blue = Button(self.master, bg = "dodgerblue4", text = "Blue", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground="dodgerblue4", fg="black", padx = 50,\
                         command = lambda:self.select("bg", "dodgerblue4", "options"))
        

        green = Button(self.master, bg = "darkolivegreen", text = "Green", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground="darkolivegreen", fg="black", padx = 50,\
                         command = lambda:self.select("bg", "darkolivegreen", "options"))
        

        red = Button(self.master, bg = "red4", text = "Red", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground="red4", fg="black", padx = 50,\
                         command = lambda:self.select("bg", "red4", "options"))
        

        purple = Button(self.master, bg = "purple4", text = "Purple", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground="purple4", fg="black", padx = 50,\
                         command = lambda:self.select("bg", "purple4", "options"))

        #card backs
        img = PhotoImage(file = "Pictures/redcard_.gif")
        redCard = Button(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black",\
                         command = lambda:self.select("card", "redcard.gif", "options"))
        redCard.image = img

        img = PhotoImage(file = "Pictures/bluecard_.gif")
        blueCard = Button(self.master, image = img, bg = Battle.bg, borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black",\
                         command = lambda:self.select("card", "bluecard.gif", "options"))
        blueCard.image = img


        img = PhotoImage(file = "Pictures/blackcard_.gif")
        blackCard = Button(self.master, image = img, bg = Battle.bg, borderwidth=0, highlightthickness=0, activebackground = Battle.bg, fg="black",\
                         command = lambda:self.select("card", "blackcard.gif", "options"))
        blackCard.image = img


        space1 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = "black")
        space1.grid(row=0, column = 0, sticky=NSEW, rowspan = 13, ipadx = 1)

        space2 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = "black")
        space2.grid(row=0, column = 2, sticky=NSEW, rowspan = 13, ipadx = 1)

        space3 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = "black")
        space3.grid(row=0, column = 4, sticky=NSEW, rowspan = 13, ipadx = 1)

        space5 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = "black")
        space5.grid(row=0, column = 6, sticky=NSEW, rowspan = 13, ipadx = 1)

        space4 = Label(self.master, justify = "center", text = "", borderwidth=0, font = ("Arial", 1), highlightthickness=0, background = "black")
        space4.grid(row=1, column = 0, sticky=NSEW, columnspan = 12)

        space6 = Label(self.master, justify = "center", text = "", borderwidth=0, font = ("Arial", 1), highlightthickness=0, background = "black")
        space6.grid(row=11, column = 0, sticky=NSEW, columnspan = 6)

        textB = Label(self.master, justify = "center", text = "Backgrounds", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        textB.grid(row=0, column = 1, sticky=NSEW, rowspan = 1, ipady = 10, ipadx = 20)

        textC = Label(self.master, justify = "center", text = "Decks", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        textC.grid(row=0, column = 3, sticky=NSEW, rowspan = 1, ipady = 10, ipadx = 57)

        bgs = {"slategrey": grey, "sienna4": brown, "dodgerblue4": blue, "darkolivegreen": green, "red4": red, "purple4": purple}
        cbs = {"bluecard.gif": blueCard, "redcard.gif": redCard, "blackcard.gif": blackCard}

        money = Label(self.master, justify = "center", text = "Coins:\n" + str(Battle.ownedMoney), font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        money.grid(row=0, column = 5, sticky=NSEW, ipady = 20, ipadx = 20)

        b = 2
        c = 2

        for item in Battle.unlocks:
            if item in bgs:
                bgs[item].grid(row = b, column = 1, sticky = NSEW, ipadx = 30)
                b += 1
            if item in cbs:
                cbs[item].grid(row = c, column = 3, rowspan = 2, sticky = NSEW, ipadx = 50, ipady = 5)
                c += 2

        rs_1 = 11 - b
        rs_2 = 11 - c

        
        empty1 = Label(self.master, text = "", font = ("Arial", 1), borderwidth=0, highlightthickness=0, background = Battle.bg)
        empty1.grid(row = b, column = 1, sticky=NSEW, rowspan = rs_1)

        empty2 = Label(self.master, text = "", font = ("Arial", 1), borderwidth=0, highlightthickness=0, background = Battle.bg)
        empty2.grid(row = c, column = 3, sticky=NSEW, rowspan = rs_2)

        img = PhotoImage(file = "Pictures/suits.gif")
        empty3 = Label(self.master, image = img,borderwidth=0, highlightthickness=0, background = Battle.bg)
        empty3.image = img
        empty3.grid(row=2, column = 5, sticky=NSEW, rowspan = 9, ipadx = 10)
        

        previewText = Label(self.master, justify = "center", text = "Preview", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        previewText.grid(row=0, column = 7, columnspan = 2, sticky=NSEW, ipadx = 10)
        
        img = PhotoImage(file = Card.cardBack)
        previewCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
        previewCard.image = img
        previewCard.grid(row=2, column=8, sticky=NSEW, rowspan = 5, ipadx = 37, ipady = 50)

        image = Card.cardBack.split(".")
        image = image[0] + "_." + image[1]    
        img = PhotoImage(file = image)
        previewCard_ = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
        previewCard_.image = img
        previewCard_.grid(row=2, column=7, sticky=NSEW, rowspan = 5, ipadx = 55, ipady = 20)

        img = PhotoImage(file = "Pictures/superBetUp.gif")
        superBetUp = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, activebackground=Battle.bg)
        superBetUp.image = img
        superBetUp.grid(row=7, column=7, sticky = NSEW, ipady = 23)

        img = PhotoImage(file = "Pictures/superBetDown.gif")
        superBetDown = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, activebackground=Battle.bg)
        superBetDown.image = img
        superBetDown.grid(row = 8, column=7, sticky = NSEW, ipady = 23)

        previewtextText = Label(self.master, justify = "center", text = "Ace of Spades\nVS\n10 of Hearts", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        previewtextText.grid(row=7, column = 8, rowspan = 2, sticky=NSEW, ipadx = 10)

        leave = Button(self.master, text = "Main Screen", font=("Arial", 20), borderwidth=0, bg = Battle.bg, highlightthickness=0, command = lambda:self.changeScreen("mainScreen"))
        leave.grid(row= 12, column=1, sticky=NSEW, ipady = 3)

        play = Button(self.master, text = "Play", font=("Arial", 20), borderwidth=0, bg = Battle.bg, highlightthickness=0, command = lambda:self.changeScreen("gameScreen"))
        play.grid(row= 12, column=5, sticky=NSEW, ipady = 3)

        store = Button(self.master, text = "Store", font=("Arial", 20), borderwidth=0, bg = Battle.bg, highlightthickness=0, command = lambda:self.changeScreen("storeScreen"))
        store.grid(row= 12, column=3, sticky=NSEW, ipady = 3)

        empty4 = Label(self.master, justify = "center", text = "", borderwidth=0, font = ("Arial", 1), highlightthickness=0, bg = Battle.bg)
        empty4.grid(row=11, column = 7, sticky=NSEW, columnspan = 2, rowspan = 2)
        

        Battle.widgets = [previewCard, previewCard_, superBetUp, superBetDown, empty4, previewtextText, previewText, grey, blue, green, red, purple, brown, redCard, blueCard, blackCard, leave, money, space1, space2, space3, space4, space5, space6, textB, textC, empty1, empty2, empty3, play, store]

        green.bind("<Enter>", lambda event:self.on_enter_color(event, "darkolivegreen"))
        green.bind("<Leave>", self.on_leave_color)

        grey.bind("<Enter>", lambda event:self.on_enter_color(event, "slate grey"))
        grey.bind("<Leave>", self.on_leave_color)

        brown.bind("<Enter>", lambda event:self.on_enter_color(event, "sienna4"))
        brown.bind("<Leave>", self.on_leave_color)
        
        blue.bind("<Enter>", lambda event:self.on_enter_color(event, "dodgerblue4"))
        blue.bind("<Leave>", self.on_leave_color)

        red.bind("<Enter>", lambda event:self.on_enter_color(event, "red4"))
        red.bind("<Leave>", self.on_leave_color)

        purple.bind("<Enter>", lambda event:self.on_enter_color(event, "purple4"))
        purple.bind("<Leave>", self.on_leave_color)

        blueCard.bind("<Enter>", lambda event:self.on_enter_card(event, "Pictures/bluecard.gif"))
        blueCard.bind("<Leave>", self.on_leave_card)

        redCard.bind("<Enter>", lambda event:self.on_enter_card(event, "Pictures/redcard.gif"))
        redCard.bind("<Leave>", self.on_leave_card)

        blackCard.bind("<Enter>", lambda event:self.on_enter_card(event, "Pictures/blackcard.gif"))
        blackCard.bind("<Leave>", self.on_leave_card)
        
                        #####################  CODE   #####################

    def select(self, item, value, update):
        if item == "bg":
            Battle.bg = value
        if item == "card":
            Card.cardBack = "Pictures/" + value

        save(Battle.bg, Battle.ownedMoney, Card.cardBack, Battle.unlocks)

        if (update == "options"):
            self.changeScreen("optionsScreen")
        if (update == "store"):
            self.changeScreen("storeScreen")

    def stats(self, wins, loss):

        try:
            winLoss = (float(wins)/float(loss))

        except:
            winLoss = float(0)

        winLoss = round(winLoss, 2)

        return winLoss

        

    
#########################################################
WIDTH = 1072
HEIGHT = 712
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("War")
g = Battle(window)
g.mainScreen()
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


# Timothy: Allowed the bet function to display the currentBet amount on the GUI screen
#           the (bet) buttons also had their borderwidth changed to account for more button-like looks
#           though they are quite large; I am considering making
#           an UpdateButton function to make that process easier later
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








