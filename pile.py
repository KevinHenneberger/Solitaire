class Pile:

    def __init__(self, label, cards):
        self.label = label
        self.cards = cards

    def isEmpty(self):
        return len(self.cards) == 0

    def isValidMove(self, fromPile, numOfCards):

        # all cards that are moved have to be flipped over except cards that are moved from the hand pile into the waste pile  
        if (fromPile.label != "h" and self.label != "w"):
            for card in fromPile.cards[-numOfCards:]:
                if (not card.isFlipped):
                    return False

        # prevents index errors by preventing moving cards from piles that are empty
        if (not fromPile.isEmpty()):

            # inserting card into tableau pile
            if (self.label == "t"):
                # prevents index errors by allowing only the number of cards in the pile to be moved
                if (len(fromPile.cards) >= numOfCards):
                    # if tableau pile is empty
                    if (self.isEmpty()):
                        # card needs to be a king
                        if (fromPile.cards[-numOfCards].rank == "K"):
                            return True
                    else:
                        # card needs to be from opposite suit and rank has to be one lower
                        if (self.cards[-1].value == fromPile.cards[-numOfCards].value + 1 and (((self.cards[-1].suit == "H" or self.cards[-1].suit == "D") and (fromPile.cards[-numOfCards].suit == "C" or fromPile.cards[-numOfCards].suit == "S")) or ((self.cards[-1].suit == "C" or self.cards[-1].suit == "S") and (fromPile.cards[-numOfCards].suit == "H" or fromPile.cards[-numOfCards].suit == "D")))):
                            return True
            
            # inserting card into foundation pile
            elif (self.label == "f"):
                # if foundation pile is empty
                if (self.isEmpty()):
                    # card needs to be an ace
                    if (fromPile.cards[-1].rank == "A"):
                        return True
                else:
                    # card needs to be from same suit and rank has to be one higher
                    if (self.cards[-1].value == fromPile.cards[-1].value - 1 and self.cards[-1].suit == fromPile.cards[-1].suit): 
                        return True
            
            # inserting card into waste pile
            elif (self.label == "w"):
                # card needs to be from hand pile
                if (fromPile.label == "h"):
                    return True
            
            # inserting card into hand pile
            elif (self.label == "h"):
                # card needs to be from waste pile
                if (fromPile.label == "w"):
                    # if hand pile is empty and the waste is not empty
                    if (self.isEmpty() and not fromPile.isEmpty()):
                        # insert cards from waste pile into hand pile
                        for card in fromPile.cards:
                            card.unflip()

                        self.cards = fromPile.cards[::-1]
                        fromPile.cards = []

                        return True

        return False

    def insertCardFrom(self, fromPile, numOfCards):
        # insert card from other pile
        self.cards.extend(fromPile.cards[-numOfCards:])
        del fromPile.cards[-numOfCards:]

    def __str__(self):
        return ", ".join([str(card) for card in self.cards])
