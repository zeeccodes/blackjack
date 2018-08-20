from card import Card
import random

class Deck:
    
    def __init__(self):
        self.suits = ['diamonds', 'clubs', 'hearts', 'spades']
        self.cards = ['Ace','2','3','4','5','6','7','8','9','10', 'Jack', 'Queen', 'King']
        self.generatedDeck = [Card(suit, face) for suit in self.suits for face in self.cards]
        random.shuffle(self.generatedDeck)
    
    def deal(self):
        return str(self.generatedDeck.pop())

    def __str__(self):
        output = ''
        for card in self.generatedDeck:
            output += str(card)
        return output
    

    


     

