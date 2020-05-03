###############################################################################
# This file holds the functions that deal with the betting system for the game
###############################################################################

def bet(value, money, currentBet):
    #bet from your pool of money, calculates the money you get after each hand
    bet = currentBet
    
    if (value == "up"):
            bet += 10
                
    elif (value == "supUp"):
            bet += 50
           
    elif (value == "down"):
            bet -= 10

    elif (value == "supDown"):
            bet -= 50

    if (bet >= money):
            bet -= (bet-money)

    if (bet < 0):
            bet -= bet

    if (currentBet > money):
        currentBet = money
                
    if (value == "me"):
        money += currentBet
        if (currentBet == 0):
            money += 10

    elif (value == "opponent"):
        money -= currentBet

    return bet, money
