
class Card:

    def __init__(self, suit, faceValue):
        self.suit = suit
        self.faceValue = faceValue

    @property
    def getSuit(self):
        return self.suit

    def getfaceValue(self):
        return self.faceValue

    def __repr__(self):
        return self.faceValue + ' of ' + self.suit + '\n'