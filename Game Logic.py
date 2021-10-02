from random import shuffle

class Card:

    def __init__(self,s,v):
        self.suit = s
        self.value = v

class Deck:

    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    values = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(suit,value)
        shuffle(self.cards)

