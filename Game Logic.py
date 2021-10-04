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
        for suit in self.suits:
            for value in self.values:
                card = Card(suit,value)
                self.cards.append(card)
        shuffle(self.cards)

class Player:
    def __init__(self):
        self.hand = []
        self.attack = None
        self.defend = None
        self.king = False
        self.durak = False
        self.wins = 0

class Game:
    def __init__(self,players):
        self.players = players
        self.deck = Deck()
        self.deal_hands()
        self.assign_positions(0)

    def assign_positions(self,starter):
        print('hi')

    def deal_hands(self):
        n_players = len(self.players)
        hands = [self.deck.cards[i::n_players] for i in range(0,n_players)]
        for i in range(n_players):
            pname = 'Player' + str(i)
            self.players[pname].hand = hands[i]

class Session:
    def __init__(self,n_players):
        self.games = []
        self.players = self.make_players(n_players)
        self.game = Game(self.players)

    def make_players(self,n_players):
        players = {}
        for i in range(n_players):
            pname = 'Player' + str(i)
            players[pname] = Player()
        return players

game = Session(4)
print(game.game)
