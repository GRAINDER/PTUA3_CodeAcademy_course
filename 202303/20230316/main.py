# Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:

# The Deck class should have a deal method to deal a single card from the deckAfter a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
from typing import Union
import random


class Card:
    def __init__(self, suit: int, value: str) -> Union[int, str]:
        self.suit = suit
        self.value = value

    def show(self) -> Union[int, str]:
        print(self.suit, self.value)


card = Card("Card", 6)
card.show()


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.build_deck()

    def build_deck(self) -> None:
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self) -> int:
        for c in self.cards:
            return c.show()

    def shuffle(self):
        for i in range(len(self.cards)):
            r = random.randint(0, i)


    def drawCard(self):
        return self.cards.pop()


deck = Deck()

deck.shuffle()

card = deck.drawCard()

card.show()
