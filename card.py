#########################################################################
# This file holds the methods for the cards used in the battle game
#########################################################################

from random import randint

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

# shuffle the cards
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

# shuffle the cards
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
