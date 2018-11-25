from card import Card


class Deck:

    cards = []

    def __init__(self):
        while len(self.cards) < 52:
            card = Card()
            if card not in self.cards:
                self.cards.append(card)
        return

    # ADD IN CONTAINS METHOD, NOT IN IS COMPARING OBJECT REFERENCES
    def remove_card(self):
        return self.cards.pop(0)

    def add_back(self, card):
        self.cards.append(card)
        return
