from card import Card


class Deck:

    def __init__(self):
        self.cards = []
        while len(self.cards) < 52:
            card = Card()
            if card not in self.cards:
                self.cards.append(card)

    def remove_card(self):
        self.cards.pop(0)

    def add_back(self, card):
        self.cards.append(card)
