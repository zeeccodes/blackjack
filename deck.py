import card

class Deck:
    def __init__(self):
        value = []
        suits = ['Heart','Diamonds','Clover', 'Spades']

        deck = [card(value, suit) for value in range(1, 14) for suit in suits]
