class Card:

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.isFlipped = False

    def flip(self):
        self.isFlipped = True

    def unflip(self):
        self.isFlipped = False

    def __str__(self):
        if (self.isFlipped):
            return self.suit + "|" + self.rank
        else:
            return "###"
