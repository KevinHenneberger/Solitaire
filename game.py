from deck import Deck
from pile import Pile

class Game:

    def __init__(self):
        # create and shuffle deck
        self.gameDeck = Deck()
        self.gameDeck.createDeck()
        self.gameDeck.shuffleDeck()

        # initialize piles
        self.handPile = Pile("h", self.gameDeck.cards[:])
        self.wastePile = Pile("w", []) 
        self.foundationsPiles = [
            Pile("f", []),
            Pile("f", []),
            Pile("f", []),
            Pile("f", []) 
        ]
        self.tableauPiles = [
            Pile("t", []),
            Pile("t", []),
            Pile("t", []),
            Pile("t", []),
            Pile("t", []),
            Pile("t", []),
            Pile("t", [])
        ]

    def setup(self):
        # insert cards from hand pile into tableau piles
        for n, tableauPile in enumerate(self.tableauPiles):
            tableauPile.insertCardFrom(self.handPile, n + 1)

    def displayCards(self):
        print("=" * 150)

        print("[h]  || " + str(self.handPile))
        print("-" * 150)

        print("[w]  || " + str(self.wastePile))
        print("-" * 150)

        for i, foundationsPile in enumerate(self.foundationsPiles):
            print("[f" + str(i + 1) + "] || ", end="")
            print(foundationsPile)
        print("-" * 150)

        for i, tableauPile in enumerate(self.tableauPiles):
            print("[t" + str(i + 1) + "] || ", end="")
            print(tableauPile)
        print("-" * 150)

    def runLoop(self):
        self.setup()

        keyMap = {
            "h": self.handPile,
            "w": self.wastePile,
            "f1": self.foundationsPiles[0],
            "f2": self.foundationsPiles[1],
            "f3": self.foundationsPiles[2],
            "f4": self.foundationsPiles[3],
            "t1": self.tableauPiles[0],
            "t2": self.tableauPiles[1],
            "t3": self.tableauPiles[2],
            "t4": self.tableauPiles[3],
            "t5": self.tableauPiles[4],
            "t6": self.tableauPiles[5],
            "t7": self.tableauPiles[6]
        }

        while (True):
            # if hand pile is empty and the waste is not empty
            if (self.handPile.isEmpty() and not self.wastePile.isEmpty()):
                # insert cards from waste pile into hand pile
                for card in self.wastePile.cards:
                    card.unflip()

                self.handPile.cards = self.wastePile.cards[::-1]
                self.wastePile.cards = []

            # flip top card in hand pile
            if (not self.handPile.isEmpty()):
                self.handPile.cards[-1].flip()

            # flip top card in tableau piles
            for tableauPile in self.tableauPiles:
                if (not tableauPile.isEmpty()):
                    tableauPile.cards[-1].flip()

            self.displayCards()

            # prompt user for input 
            while True:
                action = input("[continue (c) or quit (q)] || ")
                if (action == "c" or action == "q"):
                    break

            if (action == "c"):
                # prompt user for input 
                while True:
                    try: 
                        fromPile = keyMap[input("[move from]  || ")]
                        break
                    except:
                        continue

                while True:
                    try: 
                        numOfCards = int(input("[# of cards] || "))
                        break
                    except:
                        continue

                while True:
                    try: 
                        toPile = keyMap[input("[move to]    || ")]
                        break
                    except:
                        continue

                # commit move 
                if (toPile.isValidMove(fromPile)):
                    toPile.insertCardFrom(fromPile, numOfCards)
                    print("--- move executed ---")
                else:
                    print("--- move failed ---")

                # if game is won
                if (len(self.foundationsPiles[0].cards) == 13 and len(self.foundationsPiles[1].cards) == 13 and len(self.foundationsPiles[2].cards) == 13 and len(self.foundationsPiles[3].cards) == 13):
                    print("--- congratulations, you won! ---")
                    break

            elif (action == "q"):
                print("--- exited ---")  
                break
