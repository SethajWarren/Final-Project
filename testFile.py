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

########### imports the libraries needed for the program ######################
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

                        ##################### GAME SETUP  #####################

    # a function to create the cards
    def createCards(self):

        # sets variables that will be used later
        Battle.money = 10
        Battle.widgets = []
        
        #creates all the cards
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

        # adds all the cards to a list titled deck
        deck = [s2, c2, d2, h2, s3, c3, d3, h3, s4, c4, d4, h4, s5, c5, d5, h5, s6, c6, d6, h6, s7, c7, d7, h7, s8, c8, d8, h8, s9, c9, d9, h9, s10, c10, d10, h10, sJ, cJ, dJ, hJ, sQ, cQ, dQ, hQ, sK, cK, dK, hK, sA, cA, dA, hA]
        # uses the shuffle function to randomize the cards that the player and computer will receive
        Battle.me, Battle.opponent = shuffleStart(self, deck)

        # sets lists that will be used for special circumstances
        Battle.meQ = []
        Battle.oppQ = []

        Battle.megabattle = []

        # sets more variables that will be used throughout the game
        Battle.history = ["\n\n\n","\n\n\n","\n\n\n","\n\n\n"]
        Battle.ties = 0
        Battle.wins = 0
        Battle.loss = 0
        Battle.currentBet = 0
        
                        #####################  GAME LOGIC #####################

    # a battle function that will be called when two cards battle   
    def battle(self, winner = None):
        
        try:
            # if the length of the players deck is 0 it shuffles the deck of gained cards and uses that
            # as the players deck
            if(len(Battle.me) == 0):
                Battle.me = shuffle(self, Battle.me, Battle.meQ)

            # likewise for the opponent
            if(len(Battle.opponent) == 0):
                Battle.opponent = shuffle(self, Battle.opponent, Battle.oppQ)

            # sets the cards that are battling as the first card in the list
            myCard = Battle.me[0]
            oppCard = Battle.opponent[0]

            # updates the screen to show the correct card on the GUI
            self.gameScreen("update")

            # if the player's card is a lower rank than the opponent, then the player loses
            # and both cards get added to the opponent's win deck
            if (myCard.rank < oppCard.rank):
                winner = "Loss"
                Battle.oppQ.append(myCard)
                Battle.oppQ.append(oppCard)
                Battle.loss += 1

            # if the player's card outranks the opponents, then the player wins
            # and both cards get added to the player's win deck
            if (myCard.rank > oppCard.rank):
                winner = "Win"
                Battle.meQ.append(myCard)
                Battle.meQ.append(oppCard)
                Battle.wins += 1
                
            # if the player's card is the same rank as the opponents than a tie commences
            if (myCard.rank == oppCard.rank):
                self.gameScreen("update")
                # creates a button that displays the mega battle has commenced and when pressed calls the mega battle funciton
                img = PhotoImage(file = "Pictures/battle.gif")
                battleButton = Button(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg, command = lambda: self.megaBattle())
                battleButton.image = img
                battleButton.grid(row = 6, column = 2, sticky = NSEW, columnspan = 2)
                Battle.widgets.append(battleButton)

            # if the tie does not commence then it updates the screen
            else:
                # adds the last battle to the history displayed
                Battle.history.append("   {} vs. {}\n   ({})\n\n".format(myCard, oppCard, winner))
                if (len(Battle.history) > 4):
                    del Battle.history[0]

                # calculates any bets the player might have made in the last battle
                self.bet(winner, Battle.money, Battle.currentBet)

                # deletes the cards used from the players and opponents deck to avoid duplicates                     
                del Battle.me[0]
                del Battle.opponent[0]

        # in the event that this throws up an error, that means that there are no more cards left to be used
        # meaning that the game is oover
        except:
            # sets the game state to false and changes to the game screen
            Battle.going = False
            self.gameScreen("update")

    # a function that is called whenever there is a tie
    def megaBattle(self):
        
        # increments the tie counter by 1
        Battle.ties += 1
        # creates a list of the cards that will be used in the mega battle
        megabattle = []
        # adds the cards to the deck for the mega battle
        Battle.megabattle.append(Battle.me[0])
        Battle.megabattle.append(Battle.opponent[0])
        # deletes them to avoid any duplication
        del Battle.me[0]
        del Battle.opponent[0]

        # if the player's or opponent's deck is not big enough for a battle it adds the win deck to be used
        if (len(Battle.me) < 4):
            Battle.me = shuffle(self, Battle.me, Battle.meQ)
            
        if (len(Battle.opponent) < 4):
            Battle.opponent = shuffle(self, Battle.opponent, Battle.oppQ)
            
        # if they still dont have enough, they battle with however many they have
        if (len(Battle.me) < 4):
            myMega = len(Battle.me) - 2
        else:
            myMega = 3

        # sets the counter for clicks
        clicks = 0
        # creates the GUI element for the battle and passes the number of clicks
        self.battleScreen(myMega, clicks)

    # the second part of the mega battle that is called after the player clicks the button to commence it
    def megabattle2(self, myMega, clicks):
        
        # checks if the umber of clicks is less than the cards needed for the battle
        if (clicks < myMega):
            # increments the clicks by 1
            clicks += 1
            # appends another card to the mega battle deck
            Battle.megabattle.append(Battle.me[0])
            # deletes the card to avoid duplication
            del Battle.me[0]
            # updates the GUI to show the correct number of clicks
            self.battleScreen(myMega, clicks)

        # if the number of clicks is equal the the number of cards needed for the battle
        elif (clicks == myMega):
            # checks if the opponent's deck is less than four
            if (len(Battle.opponent) < 4):
                # if so, it appends half of their deck deleting each to avoid duplication
                for i in range(len(Battle.opponent) - 2):
                    Battle.megabattle.append(Battle.opponent[0])
                    del Battle.opponent[0]
            # if not
            else:
                # it adds 3 of the opponents card to the deck
                for i in range(3):
                    Battle.megabattle.append(Battle.opponent[0])
                    del Battle.opponent[0]
            
            # increments the clicks by 1        
            clicks += 1
            # updates the GUI to corrently show the number of cards
            self.battleScreen(myMega, clicks)

        # if the clicks are more than the number of cards needed for the battle
        elif (clicks > myMega):
            
            try:
                # it playes the next card in the player's and opponent's deck
                myCard = Battle.me[0]
                oppCard = Battle.opponent[0]
                # it appends them to the mega battle deck
                Battle.megabattle.append(myCard)
                Battle.megabattle.append(oppCard)

                # if the card played by the player is less than the card played by the opponent, the player loses
                # and the cards from the mega battle deck are given to the opponent
                if (myCard.rank < oppCard.rank):
                    winner = "Loss"
                    for item in Battle.megabattle:
                        Battle.oppQ.append(item)
                    Battle.loss += 1                    

                # if the card played by the player is greater than the card played by the opponent, the player wins
                # and the cards from the mega battle deck are given to the player
                if (myCard.rank > oppCard.rank):
                    winner = "Win"
                    Battle.money += 40
                    for item in Battle.megabattle:
                        Battle.meQ.append(item)
                    Battle.wins += 1                    

                # if the cards are again equal to each other, then another tie breaker is commenced using the same deck
                if (myCard.rank == oppCard.rank):
                    Battle.megabattle.remove(myCard)
                    Battle.megabattle.remove(oppCard)
                    winner = "Tie"
                    self.battle(winner)
                    
                # if no tie commences, then
                else:
                    # the battle is added to the history
                    Battle.history.append("   {} vs. {}\n   ({})\n\n".format(myCard, oppCard, winner))
                    if (len(Battle.history) > 4):
                        del Battle.history[0]

                    # any bets the player made are calculated
                    self.bet(winner, Battle.money, Battle.currentBet)
                    # the GUI are updated to reflect these changes
                    self.gameScreen("update")
                    # cards are deleted to avoid duplication
                    del Battle.me[0]
                    del Battle.opponent[0]
                    # the mega battle deck is set to empty
                    Battle.megabattle = []

            # in the event that there is an error, that means that one of the player's has run out of cards
            # meaning the game is over
            except:
                # sets the battle state to false
                Battle.going = False
                # updates the GUI
                self.gameScreen("update")

    def bet(self, value, money, currentBet):
        
        #bet from your pool of money, calculates the money you get after each hand
        Battle.currentBet, Battle.money = bet(value, money, currentBet)

        # overwrites the current label in the GUI to display the players bet
        currentBet = Label(self.master, bg = Battle.bg, font = ("Arial", 20), text = "+" + str(Battle.currentBet), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        currentBet.grid(row=6, column=0, sticky = NSEW)

        
        # overwrites the current label in the GUI to display the players currency
        img = PhotoImage(file = "Pictures/coin.gif")
        moneyL = Label(self.master, compound = "left",image = img, justify = "left", text = " " + str(Battle.money), font=("Arial", 20),borderwidth=0, highlightthickness=0, background = Battle.bg)
        moneyL.image = img
        moneyL.grid(row=0, column = 0, sticky=NSEW, rowspan = 4)
        
        # appends the widgets used for the GUI to a list named widgets that are used for changing screens
        Battle.widgets.append(currentBet)
        Battle.widgets.append(moneyL)
        
    # this function is called when the game is over
    def endGameScreen(self):

        # if the total cards of the player is greater than the total cards of the opponent, they win the game
        if (len(Battle.me)+ len(Battle.meQ) > len(Battle.opponent) + len(Battle.oppQ)):
            Battle.money += 1000
            # they are told they win the game and how much money they won
            endText = "Congratulations!\n You Won!"
            endText += "\n You earned {} coins!".format(Battle.money)
            leavePad = 40
            Battle.ownedMoney += Battle.money

        # if the total cards of the player is less than the total cards of the opponent, they lose the game
        if (len(Battle.me) + len(Battle.meQ) < len(Battle.opponent)+ len(Battle.oppQ)):
            # they are told they have lost
            endText = "Aw, too Bad...\nBetter Luck Next Time"
            leavePad = 78
        
        # saves the game
        save(Battle.bg, Battle.ownedMoney, Card.cardBack, Battle.unlocks)
        
        # creates a label holding the text of the win/lose
        gameover = Label(self.master, bg = Battle.bg, text = endText, font=("Arial", 50), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        gameover.grid(row=0, column=0, sticky=NSEW, ipady = 30)

        # creates a label displaying the stats of the last game
        stats = Label(self.master, bg = Battle.bg, text = "Wins: {}\n\nLosses: {}\n\nBattles: {}\n\nWin/Loss: {}".format(Battle.wins, Battle.loss, Battle.ties, self.stats(Battle.wins,Battle.loss)), justify = LEFT,\
                      font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        stats.grid(row=1, column = 0, sticky=NSEW, ipadx = 20, ipady = 24)

        # adds a button with the text "Quit" that sends the player to the main menu screen
        img = PhotoImage(file = "Pictures/button.gif")
        leave = Button(self.master, text = "Quit", compound = "center", fg = "white", image = img, borderwidth=0, activebackground=Battle.bg, highlightthickness=0, font=("Arial", 30), background = Battle.bg, command = lambda:self.changeScreen("mainScreen"))
        leave.image = img
        leave.grid(row=2, column=0, sticky=NSEW, ipady = leavePad, ipadx = 446)

        # creates a list named widgets that include the GUI elements of the current screen
        Battle.widgets = [gameover, leave, stats]


                        ##################### GAME SCREENS #####################

    # a function that creates the screen used for the game
    def gameScreen(self, update = ""):

        # if the funciton is called with update
        if (update == "update"):
            # it destroys the widgets on the screen
            while (len(Battle.widgets) > 0):
                Battle.widgets[0].destroy()
                del Battle.widgets[0]

        # if the card back is the black card the text is changed to white for visibility
        if(Card.cardBack == "Pictures/blackcard.gif"):
            textcolor = "white"

        # if not it is the defualt black
        else:
            textcolor = "black"

        # if the battle state is set to None
        if (Battle.going == None):

            # it calls the createCards function
            self.createCards()

            # creates a button with the image of the super bet up that increases the amount the player bets
            img = PhotoImage(file = "Pictures/superBetUp.gif")
            superBetUp = Button(self.master, bg = Battle.bg, image = img, borderwidth=0, activebackground=Battle.bg,\
                                command = lambda:self.bet("supUp", Battle.money, Battle.currentBet))
            superBetUp.image = img
            superBetUp.grid(row=4, column=0, sticky = NSEW, ipadx = 70)

            # creates a button with the image of the bet up that increases the amount the player bets
            img = PhotoImage(file = "Pictures/betUp.gif")
            betUp = Button(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg,\
                           command = lambda:self.bet("up", Battle.money, Battle.currentBet))
            betUp.image = img
            betUp.grid(row=5, column=0, sticky = NSEW)

            # creates a button with the image of the bet down that decreases the amount the player bets
            img = PhotoImage(file = "Pictures/betDown.gif")
            betDown = Button(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg,\
                             command = lambda:self.bet("down", Battle.money, Battle.currentBet))
            betDown.image = img
            betDown.grid(row=7, column=0, sticky = NSEW)

            # creates a button with the image of the bet down that decreases the amount the player bets
            img = PhotoImage(file = "Pictures/superBetDown.gif")
            superBetDown = Button(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg,\
                                  command = lambda:self.bet("supDown", Battle.money, Battle.currentBet))
            superBetDown.image = img
            superBetDown.grid(row=8, column=0, sticky = NSEW)

            # creates a label that is used for padding
            text = Label(self.master, bg = Battle.bg, text = "", borderwidth=0, highlightthickness=0, activebackground=Battle.bg, padx = 50)
            text.grid(row=9, column=0, sticky = NSEW, rowspan = 4)

            # creates a label that reserves the space where the battle button will
            battleButton = Label(self.master, bg = Battle.bg, text = " ", font = ("Arial", 20), borderwidth=0, highlightthickness=0, pady = 10, activebackground=Battle.bg, padx = 50)
            battleButton.grid(row=6, column = 2, sticky = NSEW, columnspan = 2)

            # creates a label to reserve space where the opponent's card will be
            oppCard = Label(self.master, bg = Battle.bg, text = "\t\t\t\t\t", borderwidth=0)
            oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6, ipadx = 35, ipady = 20)

            # creates a label to reserve space where the player's card will be
            playerCard = Label(self.master, bg = Battle.bg, text = "\t\t\t\t\t", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
            playerCard.grid(row=7, column=2, sticky=NSEW, rowspan = 6, ipadx = 35, ipady = 20)

            # creates a label to reserve space where the pool of cards for the battle will be
            pool = Label(self.master, bg = Battle.bg, text = "\t\t\t")
            pool.grid(row=0, column=1, sticky=N+S+E+W, rowspan = 13)

            # creates a label that is used as a seperator for the GUI
            space = Label(self.master, bg = "black", text = "")
            space.grid(row=0, column=4, sticky=N+S+E+W, rowspan = 13)
            
            # creates the quit button that sends the player back to the main menu
            img = PhotoImage(file = "Pictures/buttonWide.gif")
            leave = Button(self.master, bg = Battle.bg, text = "Quit", compound = "center", fg = "white", image = img, font = ("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, command = lambda: self.changeScreen("mainScreen"))
            leave.image = img
            leave.grid(row = 12, column = 5, sticky = NSEW, columnspan = 1, ipadx = 11)

            # sets the battle state as True
            Battle.going = True

            # sets i to 0
            i = 0

            # creates a list named persistWidgets that hold the widgets that are persistent and do not need to be updated
            Battle.persistWidgets = [superBetDown, betDown, betUp, superBetUp, text, battleButton, pool, leave, oppCard, playerCard, space]


        # if the battle state is set to True
        elif (Battle.going == True):
        
            # creates a label that displays the opponents card being played
            img = PhotoImage(file = Battle.opponent[0].image)
            oppCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
            oppCard.image = img
            oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6, ipadx = 30, ipady = 20)

            # creates a label that displays the player's card being played
            img = PhotoImage(file = Battle.me[0].image)
            playerCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
            playerCard.image = img
            playerCard.grid(row=7, column=2, sticky=NSEW, rowspan = 6, ipadx = 30, ipady = 20)

            # adds these items to the widgets list
            widgets = [oppCard, playerCard]

            for item in widgets:
                Battle.widgets.append(item)

            # sets i to 1
            i = 1

        # if the battle state is not set to true
        else:
            # set i to 0
            i = 0

        # creates a label that displays the player's current bet
        currentBet = Label(self.master, bg = Battle.bg,font=("Arial", 20), text = "+" + str(Battle.currentBet), activebackground=Battle.bg)
        # creates a label that shows shows the opponent's deck and the number of cards it has
        currentBet.grid(row=6, column=0, sticky = NSEW)
        
        img = PhotoImage(file = Card.cardBack)
        oppDeck = Label(self.master, bg = Battle.bg, image = img, compound = "center", fg = textcolor, font=("Arial", 50), text = (len(Battle.opponent) + len(Battle.oppQ)-i),activebackground=Battle.bg)
        oppDeck.image = img
        oppDeck.grid(row=0, column=3, sticky=N+S+E+W, rowspan = 6, ipadx = 28, ipady = 20)

        # creates a button that shows the player's deck and the number of cards they have, when clicked it initiates a battle
        img = PhotoImage(file = Card.cardBack)
        playerDeck = Button(self.master, bg = Battle.bg, image = img, compound = "center", fg = textcolor, activeforeground = textcolor, font=("Arial", 50), text = (len(Battle.me) + len(Battle.meQ)-i),borderwidth=0,\
                            highlightthickness=0, activebackground=Battle.bg, command = lambda: self.battle())
        playerDeck.image = img
        playerDeck.grid(row=7, column=3, rowspan = 6, sticky = NSEW, ipadx = 28, ipady = 20)

        # creates a label that displays the stats from the game being played
        stats = Label(self.master, bg = Battle.bg, text = "Wins: " + str(Battle.wins) + "\n\n Losses: " + str(Battle.loss) + "\n\nBattles: {}".format(Battle.ties) + "\n\nW/L: " + str(self.stats(Battle.wins, Battle.loss)), \
                      font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        stats.grid(row=0, column = 5, sticky = NSEW, columnspan = 1, rowspan = 6)

        # creates a label that displays the past battles from the game and the cards used in that battle and who won
        history = Label(self.master, anchor = "w", bg = Battle.bg, text = "\n\n\n\n   Card History:\n\n" + Battle.history[0] +Battle.history[1] + Battle.history[2] + Battle.history[3], justify = LEFT, font = ("Arial", 10), borderwidth = 0, highlightthickness = 0, activebackground = Battle.bg)
        history.grid(row=6, column = 5, sticky = NSEW, columnspan = 1, rowspan = 6)

        # creates a label that displays the amount of money the player has in the game with a coin to signify what it is
        img = PhotoImage(file = "Pictures/coin.gif")
        totalMoney = Label(self.master, compound = "left",image = img, justify = "left", text = " " + str(Battle.money), font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        totalMoney.image = img
        totalMoney.grid(row=0, column = 0, sticky=NSEW, rowspan = 4)

        # adds all of these to the widgets list that will be used when screens are changed
        widgets = [oppDeck, playerDeck, stats, history, totalMoney, currentBet]

        for item in widgets:
            Battle.widgets.append(item)

        # if the battle state is set to false
        if(Battle.going == False):
            # destroy all the widgets on the screen
            while len(Battle.persistWidgets) > 0:
                Battle.persistWidgets[0].destroy()
                del Battle.persistWidgets[0]
            # change to the end game screen
            self.changeScreen("endGameScreen")

    # this function is called whenever there is a battle, or tie in the game
    def battleScreen(self, myMega, clicks):

        # checks the color of the card and sets the text accordingly for visibility
        if(Card.cardBack == "Pictures/blackcard.gif"):
            textcolor = "white"
        else:
            textcolor = "black"

        # I'm gonna be honest I have no clue what this does
        # it looks like it helps format the images to be easily used in this function
        image = Card.cardBack.split(".")
        image = image[0] + "_." + image[1]    
        img = PhotoImage(file = image)

        # creates a label named pool that displayes the number of cards from the mega battle deck
        pool = Label(self.master, bg = Battle.bg, image = img, compound = "center", font=("Arial", 20), fg = textcolor, text = len(Battle.megabattle), activebackground=Battle.bg)
        pool.image = img
        pool.grid(row=0, column=1, sticky=N+S+E+W, rowspan = 13)

        # createss a label that acts as padding
        oppCard = Label(self.master, bg = Battle.bg, text = "", borderwidth=0)
        oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6, ipadx = 35, ipady = 20)

        # creates a label that acts as padding
        playerCard = Label(self.master, bg = Battle.bg, text = "", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        playerCard.grid(row=7, column=2, sticky=NSEW, rowspan = 6, ipadx = 35, ipady = 20)

        # creates a button that displays the number of cards the player has, when pressed it calls the second mega battle function
        img = PhotoImage(file = Card.cardBack)
        playerDeck = Button(self.master, bg = Battle.bg, image = img, activeforeground = textcolor, compound = "center", fg = textcolor, font=("Arial", 50), text = (len(Battle.me) + len(Battle.meQ)),borderwidth=0, highlightthickness=0, activebackground=Battle.bg, command = lambda: self.megabattle2(myMega, clicks))
        playerDeck.image = img
        playerDeck.grid(row=7, column=3, rowspan = 6, sticky = NSEW, ipadx = 28, ipady = 20)

        # creates a label that displayes the number of cards the opponent has
        img = PhotoImage(file = Card.cardBack)
        oppDeck = Label(self.master, bg = Battle.bg, image = img, compound = "center", fg = textcolor, font=("Arial", 50), text = (len(Battle.opponent) + len(Battle.oppQ)),activebackground=Battle.bg)
        oppDeck.image = img
        oppDeck.grid(row=0, column=3, sticky=N+S+E+W, rowspan = 6, ipadx = 28, ipady = 20)

        # creates a label that reserves the space for the battle button
        battleButton = Label(self.master, bg = Battle.bg, text = " ", font = ("Arial", 20), borderwidth=0, pady = 10, highlightthickness=0, activebackground=Battle.bg)
        battleButton.grid(row=6, column = 2, sticky = NSEW, columnspan = 2)

        # creates a label that displays the current bet the player has
        currentBet = Label(self.master, bg = Battle.bg,font=("Arial", 20), text = "+" + str(Battle.currentBet), activebackground=Battle.bg)
        currentBet.grid(row=6, column=0, sticky = NSEW)
        
        # adds the widgets to a list that will be used when changing screens
        widgets = [pool, oppCard, playerCard, oppDeck, playerDeck, battleButton, currentBet]

        for item in widgets:
            Battle.widgets.append(item)



##################################################################################################
#############################################  MAIN  #############################################
##################################################################################################

                        ##################### MORE GAME SCREENS #####################

    # this function is called at the beginning of the program and creates the main screen
    def mainScreen(self):

        # sets the battle state to none
        Battle.going = None

        # retrieve the data from the save file
        Battle.bg, Battle.ownedMoney, Card.cardBack, Battle.unlocks = retrieve()

        # a label that is created for padding
        leftSpace = Label(self.master, text = "\t", borderwidth=0, font=("Arial", 30), highlightthickness=0, background = Battle.bg)
        leftSpace.grid(row=0, column=0, sticky=NSEW, rowspan = 8, ipadx = 106)

        # a label that displays the title of the game
        img = PhotoImage(file = "Pictures/WARtitle.gif")
        title = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
        title.image = img
        title.grid(row=1, column=1, sticky=NSEW, ipadx = 57)

        # a label that is created for padding
        topSpace = Label(self.master, text = "\t", borderwidth=0, font=("Arial", 30), highlightthickness=0, background = Battle.bg)
        topSpace.grid(row=0, column=1, sticky=NSEW)

        # a label that is created for padding
        midSpace = Label(self.master, text = "\t", borderwidth=0, font=("Arial", 30), highlightthickness=0, background = Battle.bg)
        midSpace.grid(row=2, column=1, sticky=NSEW, ipady = 12)

        # a label that displays the number of coins the player has alongside a picture of a coin to signify what it means
        img = PhotoImage(file = "Pictures/coin.gif")
        money = Label(self.master, compound = "left",image = img, justify = "left", text = " " + str(Battle.ownedMoney), font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        money.image = img
        money.grid(row=0, column = 2, sticky=NSEW, rowspan = 1, ipady = 15, ipadx = 20)

        # a label that is created for padding
        rightSpace = Label(self.master, text = "\t", borderwidth=0, font=("Arial", 30), highlightthickness=0, background = Battle.bg)
        rightSpace.grid(row=1, column=2, sticky=NSEW, rowspan = 7, ipadx = 106)

        # a label that is created for padding
        botSpace = Label(self.master, text = "\t", borderwidth=0, highlightthickness=0, font=("Arial", 20), background = Battle.bg)
        botSpace.grid(row=7, column=1, sticky=NSEW, ipadx = 20, ipady = 10)


        img = PhotoImage(file = "Pictures/button.gif")
        play = Button(self.master, text = "Play", compound = "center", borderwidth=0, image = img, activebackground=Battle.bg, highlightthickness=0, fg = "white", font=("Arial", 20), background = Battle.bg, command = lambda:self.changeScreen("gameScreen"))
        play.image = img
        play.grid(row=3, column=1, sticky=NSEW, ipadx = 20, ipady = 13)

        options = Button(self.master, text = "Options", compound = "center", image = img, fg = "white", borderwidth=0, activebackground=Battle.bg, highlightthickness=0, font=("Arial", 20), background = Battle.bg, command = lambda:self.changeScreen("optionsScreen"))
        options.image = img
        options.grid(row=4, column=1, sticky=NSEW, ipady = 13)

        store = Button(self.master, text = "Store", compound = "center", image = img, fg = "white", borderwidth=0, activebackground=Battle.bg, highlightthickness=0, font=("Arial", 20), background = Battle.bg, command = lambda:self.changeScreen("storeScreen"))
        store.image = img
        store.grid(row=5, column=1, sticky=NSEW,  ipadx = 20, ipady = 13)

        leave = Button(self.master, text = "Quit", compound = "center", image = img, fg = "white", borderwidth=0, activebackground=Battle.bg, highlightthickness=0, font=("Arial", 20), background = Battle.bg, command = lambda:quit(0))
        leave.image = img
        leave.grid(row=6, column=1, sticky=NSEW, ipadx = 20, ipady = 13)

        # adds the widgets to the list of widgets that is used when the game changed screens
        Battle.widgets = [leftSpace, topSpace, midSpace, botSpace, rightSpace, play, options, store, leave, money, title]
        Battle.persistWidgets = []


##################################################################################################
#############################################  STORE  ############################################
##################################################################################################

    # this funciton is called whenever the player goes to the store screen       
    def storeScreen(self):

        # a label that displays the the current amount of money that the player has to spend on things in the store
        img = PhotoImage(file = "Pictures/coin.gif")
        money = Label(self.master, compound = "left",image = img, justify = "left", text = " " + str(Battle.ownedMoney), font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        money.image = img
        money.grid(row=0, column = 5, sticky=NSEW, rowspan = 1, ipady = 32, ipadx = 22)

        # a label that titles the column as the bacgrounds available to purchase and how much they cost
        textB = Label(self.master, justify = "center", text = "New Backgrounds\n(5000)", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        textB.grid(row=0, column = 1, sticky=NSEW, rowspan = 1)

        # a label that titles the column as the card backs available to purchase and how much they cost
        textC = Label(self.master, justify = "center", text = "New Decks\n(10000)", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        textC.grid(row=0, column = 3, sticky=NSEW, rowspan = 1)

        # a label that is created for padding
        space1 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = "black")
        space1.grid(row=0, column = 0, sticky=NSEW, rowspan = 13, ipadx = 1)

        # a label that is created for padding
        space2 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = "black")
        space2.grid(row=0, column = 2, sticky=NSEW, rowspan = 13, ipadx = 1)

        # a label that is created for padding
        space3 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = "black")
        space3.grid(row=0, column = 4, sticky=NSEW, rowspan = 13, ipadx = 1)

        # a label that is created for padding
        space4 = Label(self.master, justify = "center", text = "", borderwidth=0, font = ("Arial", 1), highlightthickness=0, background = "black")
        space4.grid(row=1, column = 0, sticky=NSEW, columnspan = 13)

        # a label that is created for padding
        space5 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = "black")
        space5.grid(row=0, column = 6, sticky=NSEW, rowspan = 13, ipadx = 1)

        # a label that is created for padding
        space6 = Label(self.master, justify = "center", text = "", borderwidth=0, font = ("Arial", 1), highlightthickness=0, background = "black")
        space6.grid(row=11, column = 0, sticky=NSEW, columnspan = 6)
        
        # a button that is used to purchase a grey background
        grey = Button(self.master, bg = "slategrey", text = "Grey", font=("Arial", 20), borderwidth=0, highlightthickness=0, fg="black",\
                         command = lambda:self.purchase("bg", "slategrey"), activebackground="slategrey")
        
        # a button that is used to purchase a brown background
        brown = Button(self.master, bg = "sienna4", text = "Brown", font=("Arial", 20), borderwidth=0, highlightthickness=0, fg="black",\
                         command = lambda:self.purchase("bg", "sienna4"), activebackground="sienna4")

        # a button that is used to purchase a blue background
        blue = Button(self.master, bg = "dodgerblue4", text = "Blue", font=("Arial", 20), borderwidth=0, highlightthickness=0, fg="black",\
                         command = lambda:self.purchase("bg", "dodgerblue4"), activebackground="dodgerblue4")
                
        # a button that is used to purchase a red background
        red = Button(self.master, bg = "red4", text = "Red", font=("Arial", 20), borderwidth=0, highlightthickness=0, fg="black",\
                         command = lambda:self.purchase("bg", "red4"), activebackground="red4")
        
        # a button that is used to purchase a purple background
        purple = Button(self.master, bg = "purple4", text = "Purple", font=("Arial", 20), borderwidth=0, highlightthickness=0, fg="black",\
                         command = lambda:self.purchase("bg", "purple4"), activebackground="purple4")

        # a button that is used to purchase a red cardback
        img = PhotoImage(file = "Pictures/redcard_.gif")
        redCard = Button(self.master, image = img, bg = Battle.bg, borderwidth=0, highlightthickness=0, fg="black",\
                         command = lambda:self.purchase("card", "redcard.gif"), activebackground=Battle.bg)
        redCard.image = img

        # a button that is used to purchase a black cardback
        img = PhotoImage(file = "Pictures/blackcard_.gif")
        blackCard = Button(self.master, image = img, bg = Battle.bg, borderwidth=0, highlightthickness=0, fg="black",\
                         command = lambda:self.purchase("card", "blackcard.gif"), activebackground=Battle.bg)
        blackCard.image = img


        # dictionaries that tie the colors to the tkinter color names
        bgs = {"slategrey": grey, "sienna4": brown, "dodgerblue4": blue, "red4": red, "purple4": purple}
        # likewise with the cards and the images
        cbs = {"redcard.gif": redCard, "blackcard.gif": blackCard}

        # yeah Carter is gonna have to comment this bit cause I have no clue
        b = 2
        c = 2
        for item in bgs:
            if item not in Battle.unlocks:
                bgs[item].grid(row = b, column = 1, sticky = NSEW)
                b += 1
        for item in cbs:
            if item not in Battle.unlocks:
                cbs[item].grid(row = c, column = 3, sticky = NSEW, rowspan = 2, ipady = 5)
                c += 2

        rs_1 = 11 - b
        rs_2 =  11 - c

        # a button that sends the player back to the main screen
        img = PhotoImage(file = "Pictures/buttonWide.gif")
        leave = Button(self.master, text = "Main Screen", compound = "center", image = img, fg = "white", font=("Arial", 20), activebackground=Battle.bg, borderwidth=0, bg = Battle.bg, highlightthickness=0, command = lambda:self.changeScreen("mainScreen"))
        leave.image = img
        leave.grid(row= 12, column=1, sticky=NSEW)

        # a button that sends the player to the battle screen and starts the game
        img = PhotoImage(file = "Pictures/button.gif")
        play = Button(self.master, text = "Play", compound = "center", image = img, fg = "white", font=("Arial", 20), activebackground=Battle.bg, borderwidth=0, bg = Battle.bg, highlightthickness=0, command = lambda:self.changeScreen("gameScreen"))
        play.image = img
        play.grid(row= 12, column=5, sticky=NSEW)

        # a button that sends the player to the options screen
        options = Button(self.master, text = "Options", compound = "center", image = img, fg = "white", font=("Arial", 20), activebackground=Battle.bg, borderwidth=0, bg = Battle.bg, highlightthickness=0, command = lambda:self.changeScreen("optionsScreen"))
        options.image = img
        options.grid(row= 12, column=3, sticky=NSEW)

        # a label that is created for padding
        empty4 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, bg = Battle.bg)
        empty4.grid(row=11, column = 7, sticky=NSEW, columnspan = 2, rowspan = 2)

        # a label that is created for padding
        empty1 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = Battle.bg)
        empty1.grid(row = b, column = 1, sticky=NSEW, rowspan = rs_1)

        # a label that is created for padding
        empty2 = Label(self.master, justify = "center", text = "", borderwidth=0, highlightthickness=0, background = Battle.bg)
        empty2.grid(row = c, column = 3, sticky=NSEW, rowspan = rs_2)

        # a label that displays the suits used to fill empty space
        img = PhotoImage(file = "Pictures/suits.gif")
        empty3 = Label(self.master, image = img,borderwidth=0, highlightthickness=0, background = Battle.bg)
        empty3.image = img
        empty3.grid(row=2, column = 5, sticky=NSEW, rowspan = 9, ipadx = 10)

        # a label to show where the preview section of the screen is
        previewText = Label(self.master, justify = "center", text = "Preview", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        previewText.grid(row=0, column = 7, columnspan = 2, sticky=NSEW)
        
        # a label that displays the preview of the card back
        img = PhotoImage(file = Card.cardBack)
        previewCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
        previewCard.image = img
        previewCard.grid(row=2, column=8, sticky=NSEW, rowspan = 5, ipadx = 38, ipady = 50)

        image = Card.cardBack.split(".")
        image = image[0] + "_." + image[1]    
        img = PhotoImage(file = image)

        # a label that previews the front of the card
        previewCard_ = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
        previewCard_.image = img
        previewCard_.grid(row=2, column=7, sticky=NSEW, rowspan = 5, ipadx = 54, ipady = 20)

        # a label that displays the super bet up to allow the player to see how it contrasts with the backgrounds
        img = PhotoImage(file = "Pictures/superBetUp.gif")
        superBetUp = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, activebackground=Battle.bg)
        superBetUp.image = img
        superBetUp.grid(row=7, column=7, sticky = NSEW, ipady = 19)

        # likewise with the super bet down
        img = PhotoImage(file = "Pictures/superBetDown.gif")
        superBetDown = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, activebackground=Battle.bg)
        superBetDown.image = img
        superBetDown.grid(row = 8, column=7, sticky = NSEW, ipady = 19)

        # a label that displays text to allow the player to see how it contrasts with the backgrounds
        previewtextText = Label(self.master, justify = "center", text = "Ace of Spades\nVS\n10 of Hearts", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        previewtextText.grid(row=7, column = 8, rowspan = 2, sticky=NSEW, ipadx = 10)

        # adds these to widgets that will be used when changing screens
        Battle.widgets = [previewCard, previewCard_, superBetDown, superBetUp, empty4, previewtextText, grey, brown, blue, red, purple, redCard, leave, money, textB, textC, space1, space2, space3, space4, space5, space6, empty1, empty2, blackCard, empty3, play, options, previewText]

        # calls functions when the mouse enters and leaves the buttons that include customization
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


##################################################################################################
############################################# OPTIONS ############################################
##################################################################################################

    def optionsScreen(self):
        #backgrounds
                
        grey = Button(self.master, bg = "slategrey", text = "Grey", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground="slategrey", fg="black",\
                         command = lambda:self.select("bg", "slategrey", "options"))
        

        brown = Button(self.master, bg = "sienna4", text = "Brown", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground="sienna4", fg="black",\
                         command = lambda:self.select("bg", "sienna4", "options"))


        blue = Button(self.master, bg = "dodgerblue4", text = "Blue", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground="dodgerblue4", fg="black",\
                         command = lambda:self.select("bg", "dodgerblue4", "options"))
        

        green = Button(self.master, bg = "darkolivegreen", text = "Green", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground="darkolivegreen", fg="black",\
                         command = lambda:self.select("bg", "darkolivegreen", "options"))
        

        red = Button(self.master, bg = "red4", text = "Red", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground="red4", fg="black",\
                         command = lambda:self.select("bg", "red4", "options"))
        

        purple = Button(self.master, bg = "purple4", text = "Purple", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground="purple4", fg="black", \
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
        textB.grid(row=0, column = 1, sticky=NSEW, rowspan = 1)

        textC = Label(self.master, justify = "center", text = "Decks", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        textC.grid(row=0, column = 3, sticky=NSEW, rowspan = 1)

        bgs = {"slategrey": grey, "sienna4": brown, "dodgerblue4": blue, "darkolivegreen": green, "red4": red, "purple4": purple}
        cbs = {"bluecard.gif": blueCard, "redcard.gif": redCard, "blackcard.gif": blackCard}

        img = PhotoImage(file = "Pictures/coin.gif")
        money = Label(self.master, compound = "left",image = img, justify = "left", text = " " + str(Battle.ownedMoney), font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        money.image = img
        money.grid(row=0, column = 5, sticky=NSEW, ipady = 32, ipadx = 2)

        b = 2
        c = 2

        for item in Battle.unlocks:
            if item in bgs:
                bgs[item].grid(row = b, column = 1, sticky = NSEW)
                b += 1
            if item in cbs:
                cbs[item].grid(row = c, column = 3, rowspan = 2, sticky = NSEW, ipady = 5)
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
        empty3.grid(row=2, column = 5, sticky=NSEW, rowspan = 9)
        

        previewText = Label(self.master, justify = "center", text = "Preview", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        previewText.grid(row=0, column = 7, columnspan = 2, sticky=NSEW)
        
        img = PhotoImage(file = Card.cardBack)
        previewCard = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
        previewCard.image = img
        previewCard.grid(row=2, column=8, sticky=NSEW, rowspan = 5, ipadx = 38, ipady = 50)

        image = Card.cardBack.split(".")
        image = image[0] + "_." + image[1]    
        img = PhotoImage(file = image)
        previewCard_ = Label(self.master, bg = Battle.bg, image = img, borderwidth=0)
        previewCard_.image = img
        previewCard_.grid(row=2, column=7, sticky=NSEW, rowspan = 5, ipadx = 54, ipady = 20)

        img = PhotoImage(file = "Pictures/superBetUp.gif")
        superBetUp = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, activebackground=Battle.bg)
        superBetUp.image = img
        superBetUp.grid(row=7, column=7, sticky = NSEW, ipady = 19)

        img = PhotoImage(file = "Pictures/superBetDown.gif")
        superBetDown = Label(self.master, bg = Battle.bg, image = img, borderwidth=0, activebackground=Battle.bg)
        superBetDown.image = img
        superBetDown.grid(row = 8, column=7, sticky = NSEW, ipady = 19)

        previewtextText = Label(self.master, justify = "center", text = "Ace of Spades\nVS\n10 of Hearts", font=("Arial", 20), borderwidth=0, highlightthickness=0, background = Battle.bg)
        previewtextText.grid(row=7, column = 8, rowspan = 2, sticky=NSEW, ipadx = 10)

        img = PhotoImage(file = "Pictures/buttonWide.gif")
        leave = Button(self.master, text = "Main Screen", fg = "white", compound = "center", image = img, font=("Arial", 20), activebackground=Battle.bg, borderwidth=0, bg = Battle.bg, highlightthickness=0, command = lambda:self.changeScreen("mainScreen"))
        leave.image = img
        leave.grid(row= 12, column=1, sticky=NSEW)

        img = PhotoImage(file = "Pictures/button.gif")
        play = Button(self.master, text = "Play", fg = "white", compound = "center", image = img, font=("Arial", 20), activebackground=Battle.bg, borderwidth=0, bg = Battle.bg, highlightthickness=0, command = lambda:self.changeScreen("gameScreen"))
        play.image = img
        play.grid(row= 12, column=5, sticky=NSEW)

        img = PhotoImage(file = "Pictures/button.gif")
        store = Button(self.master, text = "Store", fg = "white", compound = "center", image = img, font=("Arial", 20), activebackground=Battle.bg, borderwidth=0, bg = Battle.bg, highlightthickness=0, command = lambda:self.changeScreen("storeScreen"))
        store.image = img
        store.grid(row= 12, column=3, sticky=NSEW)

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

        
#################################################################################################
########################################### OTHER CODE ##########################################
#################################################################################################

        
    # a function that is called when the mouse enters a button that is used to purchase customizations
    def on_enter_color(self, event, color):
        
        # changes the backgrounds of the preview area to the customization the mouse is on
        for i in range(6):
            Battle.widgets[i].configure(bg = color)
        
    # a function that is used when the mouse leaves a button that is used to purchase customizations
    def on_leave_color(self, enter):
        
        # changes the backgrounds of the preview area to the customization that is selected in options
        for i in range(6):
            Battle.widgets[i].configure(bg = Battle.bg)


    def on_enter_card(self, event, cardBack):
        # changes the cards of the preview area to the customization the mouse is on
        img = PhotoImage(file = cardBack)
        Battle.widgets[0].configure(image = img)
        Battle.widgets[0].image = img

        image = cardBack.split(".")
        image = image[0] + "_." + image[1]    
        img = PhotoImage(file = image)
        Battle.widgets[1].configure(image = img)
        Battle.widgets[1].image = img
               
    def on_leave_card(self, enter):
        # changes the cards of the preview area to the customization that is selected in options
        img = PhotoImage(file = Card.cardBack)
        Battle.widgets[0].configure(image = img)
        Battle.widgets[0].image = img

        image = Card.cardBack.split(".")
        image = image[0] + "_." + image[1]    
        img = PhotoImage(file = image)
        Battle.widgets[1].configure(image = img)
        Battle.widgets[1].image = img


    # a function that is used when purchasing an item
    def purchase(self, item, value):

        # checks if the item purchased is a card and if so charges 5000
        if (item == "card"):
            price = 10000
                
        # checks if the item purchased is a background and if so charges 1500
        if (item == "bg"):
            price = 5000

        # if the player has enough money to purchase it
        if(Battle.ownedMoney >= price):
            # creates a popup window to allow the player to confirm if the player would like to purchase the item
            purchase = mb.askyesno(title = "Purchase Item", message = "Would you like to purchase this item?")
            # if so it deducts the price of the item and unlocks the item
            if (purchase):
                Battle.ownedMoney -= price
                Battle.unlocks.append(value)
                self.select(item, value, "store")
                mb.showinfo("Purchase Item", "Item Purchased!")

        # if the player does not have enough money    
        else:
            # shows a popup explaining they do not have enough money
            mb.showinfo("Purchase Item", "Sorry! You don't have enough money")
            

    #function that removes all widgets from the previous screen
    #this is done to reduce the number of widgets loaded at any given time and to fix the persistant sizing of widgets
    def changeScreen(self, newScreen):

        #removes all widgets that are never updated from the previous screen
        while (len(Battle.persistWidgets) > 0):
            Battle.persistWidgets[0].destroy()
            del Battle.persistWidgets[0]

        #removes the widgets that are updated throughout the use of the previous screen
        while (len(Battle.widgets) > 0):
            Battle.widgets[0].destroy()
            del Battle.widgets[0]


        #creates the new screen         
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


    #used in the options and purchase screen to set the new card / background and saves it. updates the screen
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

    #calculates the win / loss ratio after each round
    def stats(self, wins, loss):
        if (loss == 0):
            winLoss = wins / 1.0
        else:
            winLoss = round((float(wins)/float(loss)), 2)

        return winLoss

        

    
######################## MAIN CODE ############################
#window size
WIDTH = 1072
HEIGHT = 712

#initialize
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("War!")
g = Battle(window)

#starts on main screen
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








