from random import shuffle
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K","Q"]
        self.cards = [Card(s, v)for s in suits for v in values]
        print(type(self.cards[0]))
        print(self.cards)

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of {}".format(len(self.cards))

    def _deal(self, num):
        counts = len(self.cards)
        actual = min([counts, num])
        if counts == 0:
            raise ValueError("All cards has been delt")

        rm_cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return rm_cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Cards less than 52")
        shuffle(self.cards)

#c = Card("Hearts", "2")
#print(c)
d = Deck()
print(d)
d.shuffle()
print(d.cards)
print(d.deal_card())
print(d.deal_hand(50))
print(d)