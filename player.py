from deck import Deck

"""
    I have to define the chip count. Should we padd money in and
    return chips or just pass in chips. 
    TODO: Fix chip/money conversion

"""

class Player:
    chips = 0
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.cards = []
    
    def __str__(self):
        print()

    @property
    def getChips(self):
        return self.chips
    
    @property
    def getName(self):
        return self.name
    
    def getCards(self):
        return self.cards
    
    def addCard(self, card):
        self.cards.append(card)

    def resetHand(self):
        self.cards = []