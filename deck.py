from card import Card
from random import shuffle

class Deck:

    def __init__(self):
        self.cards = []

    def createDeck(self):
        suits = ["H", "D", "C", "S"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K"]

        for suit in suits:
            for value, rank in enumerate(ranks):
                self.cards.append(Card(suit, rank, value))

    def shuffleDeck(self):
        shuffle(self.cards)

    def __str__(self):
        return ", ".join([str(card) for card in self.cards])
