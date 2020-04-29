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
import save
import betSys
import card


######################
######## Main ########
######################
    
class Battle(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        

    def main(self):
        Battle.money, Battle.difficulty, Battle.bg, card.Card.cardBack = save.retrieve()
        #self.mainScreen()

        self.createCards()
        self.gameScreen()
        pass
    
    def mainScreen(self):
        pass
        
    def gameScreen(self, winner = None):
        #game screen
        if (Battle.going == None):
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

            saveButton = Button(self.master, bg = Battle.bg, text = "Save", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
                                command = lambda:save.save(Battle.money, Battle.difficulty, Battle.bg, card.Card.cardBack))
            saveButton.grid(row=9, column=0, sticky = NSEW, rowspan = 4)

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

        battleButton = Label(self.master, bg = Battle.bg, text = "", borderwidth=0, highlightthickness=0, activebackground=Battle.bg, padx = 50)
        battleButton.grid(row=6, column = 2, sticky = NSEW, columnspan = 2)

        img = PhotoImage(file = card.Card.cardBack)
        oppDeck = Label(self.master, bg = Battle.bg, image = img, compound = "center", font=("Arial", 50), text = (len(Battle.opponent) + len(Battle.oppQ)-i),activebackground=Battle.bg)
        oppDeck.image = img
        oppDeck.grid(row=0, column=3, sticky=N+S+E+W, rowspan = 6, ipadx = 20, ipady = 20)

        img = PhotoImage(file = card.Card.cardBack)
        playerDeck = Button(self.master, bg = Battle.bg, image = img, compound = "center", font=("Arial", 50), text = (len(Battle.me) + len(Battle.meQ)-i),borderwidth=0,\
                            highlightthickness=0, activebackground=Battle.bg, command = lambda: self.battle())
        playerDeck.image = img
        playerDeck.grid(row=7, column=3, rowspan = 6, sticky = NSEW, ipadx = 20, ipady = 20)

############## customization buttons ########################       
##        custom1 = Button(self.master, bg = Battle.bg, text = "Grey", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
##                         command = lambda:self.store("grey"))
##        custom1.grid(row=0, column=4, sticky = NSEW, rowspan = 2)
##
##        custom2 = Button(self.master, bg = Battle.bg, text = "Brown", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
##                         command = lambda:self.store("brown"))
##        custom2.grid(row=2, column=4, sticky = NSEW, rowspan = 2)
##
##        custom3 = Button(self.master, bg = Battle.bg, text = "Blue", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
##                         command = lambda:self.store("blue"))
##        custom3.grid(row=4, column=4, sticky = NSEW, rowspan = 2)
##
##        custom4 = Button(self.master, bg = Battle.bg, text = "Green", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
##                         command = lambda:self.store("green"))
##        custom4.grid(row=6, column=4, sticky = NSEW, rowspan = 2)
##
##        custom5 = Button(self.master, bg = Battle.bg, text = "Red", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
##                         command = lambda:self.store("red"))
##        custom5.grid(row=8, column=4, sticky = NSEW, rowspan = 2)
##
##        custom6 = Button(self.master, bg = Battle.bg, text = "Purple", font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, fg="black", padx = 50,\
##                         command = lambda:self.store("purple"))
##        custom6.grid(row=10, column=4, sticky = NSEW, rowspan = 3)

        

        if (winner != "tie"):
            pool = Label(self.master, bg = Battle.bg, font=("Arial", 20), text = "")
            pool.grid(row=0, column=1, sticky=N+S+E+W, rowspan = 13)

    def battleScreen(self, myMega, clicks):
        image = card.Card.cardBack.split(".")
        image = image[0] + "_." + image[1]    
        img = PhotoImage(file = image)
        pool = Label(self.master, bg = Battle.bg, image = img, compound = "center", font=("Arial", 20), text = len(Battle.megabattle), activebackground=Battle.bg)
        pool.image = img
        pool.grid(row=0, column=1, sticky=N+S+E+W, rowspan = 13)

        oppCard = Label(self.master, bg = Battle.bg, text = "", borderwidth=0)
        oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6, ipadx = 20, ipady = 20)
        
        playerCard = Label(self.master, bg = Battle.bg, text = "", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        playerCard.grid(row=7, column=2, sticky=NSEW, rowspan = 6, ipadx = 20, ipady = 20)

        img = PhotoImage(file = card.Card.cardBack)
        playerDeck = Button(self.master, bg = Battle.bg, image = img, compound = "center", font=("Arial", 50), text = (len(Battle.me) + len(Battle.meQ)),borderwidth=0, highlightthickness=0, activebackground=Battle.bg, command = lambda: self.megabattle2(myMega, clicks))
        playerDeck.image = img
        playerDeck.grid(row=7, column=3, rowspan = 6, sticky = NSEW, ipadx = 20, ipady = 20)

        battleButton = Label(self.master, bg = Battle.bg, text = " ", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        battleButton.grid(row=6, column = 2, sticky = NSEW, columnspan = 2)

            
    def store(self, value):
        #option to purchase in-game items, decks, backgrounds
        if (value == "grey"):
            Battle.bg = "slategrey"

        if (value == "brown"):
            Battle.bg = "sienna4"

        if (value == "blue"):
            Battle.bg = "dodgerblue4"

        if (value == "green"):
            Battle.bg = "darkolivegreen"

        if (value == "red"):
            Battle.bg = "red4"

        if (value == "purple"):
            Battle.bg = "purple4"

    def options(self):
        pass

    def bet(self, value, money, currentBet):
        #bet from your pool of money, calculates the money you get after each hand
        Battle.currentBet, Battle.money = betSys.bet(value, money, currentBet)

        # overwrites the current label in the GUI to display the players bet
        currentBet = Label(self.master, bg = Battle.bg, text = "+" + str(Battle.currentBet), borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        currentBet.grid(row=6, column=0, sticky = NSEW)

        # overwrites the current label in the GUI to display the players currency
        money = Label(self.master, bg = Battle.bg, text = "Money:\n" + str(Battle.money), font=("Arial", 20), borderwidth=0, highlightthickness=0, activebackground=Battle.bg, padx = 50)
        money.grid(row=0, column=0, sticky = NSEW, rowspan = 4)

        

    def endGame(self):
        Battle.going = False
        Winner = ""
        if (len(Battle.me) > len(Battle.opponent)):
            Winner = "me"
        if (len(Battle.me) < len(Battle.opponent)):
            Winner = "opponent"
        print "________done________"
        print Winner
        
    
        
    # a battle function that take in itself and an opposing card and compares to determine the winner
    def battle(self, winner = None):                
        myCard = Battle.me[0]
        oppCard = Battle.opponent[0]
        self.gameScreen(winner)
        
        if (myCard.rank < oppCard.rank):
            winner = "opponent"
            Battle.oppQ.append(myCard)
            Battle.oppQ.append(oppCard)
            Battle.currentbet, Battle.money = betSys.bet(winner, Battle.money, Battle.currentBet)
            
        if (myCard.rank > oppCard.rank):
            winner = "me"
            Battle.meQ.append(myCard)
            Battle.meQ.append(oppCard)
            Battle.currentBet, Battle.money = betSys.bet(winner, Battle.money, Battle.currentBet)
            
        if (myCard.rank == oppCard.rank):
            battleButton = Button(self.master, bg = Battle.bg, text = "BATTLE", borderwidth=0, highlightthickness=0, activebackground=Battle.bg, command = lambda: self.megaBattle())
            Button.grid(row=6, column = 2, sticky = NSEW, columnspan = 2)
            
        else:
            del Battle.me[0]
            del Battle.opponent[0]
            print winner        
            print "\t" + str(myCard),
            print "\t" + str(oppCard)

        if(len(Battle.me) == 0):
            if (len(Battle.meQ) == 0):
                self.endGame()
            else:
                Battle.me = card.shuffle(self, Battle.me, Battle.meQ)

        if(len(Battle.opponent) == 0):
            if (len(Battle.oppQ) == 0):
                self.endGame()
            else:
                Battle.opponent = card.shuffle(self, Battle.opponent, Battle.oppQ)

                
    def megaBattle(self):
        megabattle = []
        Battle.megabattle.append(Battle.me[0])
        Battle.megabattle.append(Battle.opponent[0])
        del Battle.me[0]
        del Battle.opponent[0]


        if (len(Battle.me) < 4):
            Battle.me = card.shuffle(self, Battle.me, Battle.meQ)
            print "me shuffled"
        if (len(Battle.opponent) < 4):
            Battle.opponent = card.shuffle(self, Battle.opponent, Battle.oppQ)
            print "opp shuffled"
    
    #if they still dont have enough, they battle with however many they have
        if (len(Battle.me) < 4):
            mymega = len(Battle.me) -2
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
        else:
            clicks += 1
            if (len(Battle.opponent) < 4):
                for i in range(len(Battle.opponent) - 2):
                    Battle.megabattle.append(Battle.opponent[0])
                    del Battle.opponent[0]
            else:
                for i in range(3):
                    Battle.megabattle.append(Battle.opponent[0])
                    del Battle.opponent[0]

            self.battleScreen(myMega, clicks)
            
        if (clicks == myMega + 1):
            self.battleScreen(myMega, clicks)
            
            myCard = Battle.me[0]
            oppCard = Battle.opponent[0]
            Battle.megabattle.append(myCard)
            Battle.megabattle.append(oppCard)
                          
            
            window.update()
            print "done"
                

            if (myCard.rank < oppCard.rank):
                winner = "opponent"
                for item in Battle.megabattle:
                    Battle.oppQ.append(item)
                Battle.currentBet, Battle.money = betSys.bet(winner, Battle.money, Battle.currentBet)
            if (myCard.rank > oppCard.rank):
                winner = "me"
                for item in Battle.megabattle:
                    Battle.meQ.append(item)
                Battle.currentBet, Battle.money = betSys.bet(winner, Battle.money, Battle.currentBet)


            if (myCard.rank == oppCard.rank):
                Battle.megabattle.remove(myCard)
                Battle.megabattle.remove(oppCard)
                winner = "tie"
                self.battle(winner)
                
            else:
                self.gameScreen()
                del Battle.me[0]
                del Battle.opponent[0]
                Battle.megabattle = []

            print winner
            print "\t" + str(myCard)
            print "\t" + str(oppCard)
            
            

    def createCards(self):
        s2 = card.Card("Spades", 2, "s2.gif")
        c2 = card.Card("Clubs", 2, "c2.gif")
        d2 = card.Card("Diamonds", 2,"d2.gif")
        h2 = card.Card("Hearts", 2, "h2.gif")
        s3 = card.Card("Spades", 3, "s3.gif")
        c3 = card.Card("Clubs", 3, "c3.gif")
        d3 = card.Card("Diamonds", 3,"d3.gif")
        h3 = card.Card("Hearts", 3, "h3.gif")
        s4 = card.Card("Spades", 4, "s4.gif")
        c4 = card.Card("Clubs", 4, "c4.gif")
        d4 = card.Card("Diamonds", 4,"d4.gif")
        h4 = card.Card("Hearts", 4, "h4.gif")
        s5 = card.Card("Spades", 5, "s5.gif")
        c5 = card.Card("Clubs", 5, "c5.gif")
        d5 = card.Card("Diamonds", 5,"d5.gif")
        h5 = card.Card("Hearts", 5, "h5.gif")
        s6 = card.Card("Spades", 6, "s6.gif")
        c6 = card.Card("Clubs", 6, "c6.gif")
        d6 = card.Card("Diamonds", 6,"d6.gif")
        h6 = card.Card("Hearts", 6, "h6.gif")
        s7 = card.Card("Spades", 7, "s2.gif")
        c7 = card.Card("Clubs", 7, "c7.gif")
        d7 = card.Card("Diamonds", 7,"d7.gif")
        h7 = card.Card("Hearts", 7, "h7.gif")
        s8 = card.Card("Spades", 8, "s8.gif")
        c8 = card.Card("Clubs", 8, "c8.gif")
        d8 = card.Card("Diamonds", 8,"d8.gif")
        h8 = card.Card("Hearts", 8, "h8.gif")
        s9 = card.Card("Spades", 9, "s9.gif")
        c9 = card.Card("Clubs", 9, "c9.gif")
        d9 = card.Card("Diamonds", 9,"d9.gif")
        h9 = card.Card("Hearts", 9, "h9.gif")
        s10 = card.Card("Spades", 10, "s10.gif")
        c10 = card.Card("Clubs", 10, "c10.gif")
        d10 = card.Card("Diamonds", 10,"d10.gif")
        h10 = card.Card("Hearts", 10, "h10.gif")
        sJ = card.Card("Spades", 11, "sJ.gif")
        cJ = card.Card("Clubs", 11, "cJ.gif")
        dJ = card.Card("Diamonds", 11,"dJ.gif")
        hJ = card.Card("Hearts", 11, "hJ.gif")
        sQ = card.Card("Spades", 12, "sQ.gif")
        cQ = card.Card("Clubs", 12, "cQ.gif")
        dQ = card.Card("Diamonds", 12,"dQ.gif")
        hQ = card.Card("Hearts", 12, "hQ.gif")
        sK = card.Card("Spades", 13, "sK.gif")
        cK = card.Card("Clubs", 13, "cK.gif")
        dK = card.Card("Diamonds", 13,"dK.gif")
        hK = card.Card("Hearts", 13, "hK.gif")
        sA = card.Card("Spades", 14, "sA.gif")
        cA = card.Card("Clubs", 14, "cA.gif")
        dA = card.Card("Diamonds", 14,"dA.gif")
        hA = card.Card("Hearts", 14, "hA.gif")
        
        deck = [s2, c2, d2, h2, s3, c3, d3, h3, s4, c4, d4, h4, s5, c5, d5, h5, s6, c6, d6, h6, s7, c7, d7, h7, s8, c8, d8, h8, s9, c9, d9, h9, s10, c10, d10, h10, sJ, cJ, dJ, hJ, sQ, cQ, dQ, hQ, sK, cK, dK, hK, sA, cA, dA, hA]
        Battle.me, Battle.opponent = card.shuffleStart(self, deck)

        Battle.meQ = []
        Battle.oppQ = []
        
        Battle.going = None

        playerCard = Label(self.master, bg = Battle.bg, text = "\t\t\t\t\t\t", borderwidth=0, highlightthickness=0, activebackground=Battle.bg)
        playerCard.grid(row=7, column=2, sticky=NSEW, rowspan = 6, ipadx = 20, ipady = 20)
        
        oppCard = Label(self.master, bg = Battle.bg, text = "\t\t\t\t\t\t", borderwidth=0)
        oppCard.grid(row=0, column=2, sticky=NSEW, rowspan = 6, ipadx = 20, ipady = 20)       


        Battle.megabattle = []
    
#########################################################
WIDTH = 1080
HEIGHT = 687
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








