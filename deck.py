from card import Card


class Deck:

    cards = []

    def __init__(self):
        while len(self.cards) < 52:
            card = Card()
            if not self.contains(card):
                self.cards.append(card)
        return

    # ADD IN CONTAINS METHOD, NOT IN IS COMPARING OBJECT REFERENCES
    def remove_card(self):
        return self.cards.pop(0)

    def add_back(self, card):
        self.cards.append(card)
        return

    def contains(self, card):
        count = 0
        if len(self.cards) == 0:
            return False
        while count < len(self.cards):
            if self.cards.__getitem__(count).get_rank_value() == card.get_rank_value():
                if self.cards.__getitem__(count).get_suit_name() == card.get_suit_name():
                    return True
            count = count + 1
        return False
