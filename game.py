
from player import Player
from deck import Deck
import sys

"""
    Look up the rules for blackjack. 
"""

class Game:

    def __init__(self):
        
        deckGame = Deck()
        print("---The game has started---")
        player_1 = Player("Cesar", 100)
        dealer = Player("Dealer", 500)
        end =0

        while(end):
            print("1.Deal")
            print("2.Exit")
            end = input("What do you want to do?")
            

Game()
