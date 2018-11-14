from card import Card


# CHECK LOGIC HERE: How are these methods being used??
class Pile:

    # Creates an empty pile of cards
    def __init__(self):
        self.cards = []

    # Adds a list of cards to the pile
    def add(self, cards_to_add):
        if Pile.can_be_placed(self, cards_to_add):
            for card in cards_to_add:
                self.cards.append(card)

    # Removes a list of cards from the pile
    def remove(self, pos):
        if Pile.can_be_moved(self[pos:]):
            stack_to_remove = self.cards[pos:]
            self.cards = self.cards[:pos]
            return stack_to_remove

    # Checks if the pile is empty
    def is_empty(self):
        if len(self.cards) == 0:
            return True
        else:
            return False

    # Checks if the selected list of cards can be moved
    @staticmethod
    def can_be_moved(stack_of_cards):
        count = len(stack_of_cards)
        can_move = True
        card_pos = 0

        #Checks that stack_of_cards is in consecutive descending order
        while count > 0:
            curr_card = stack_of_cards[card_pos]
            next_card = stack_of_cards[card_pos + 1]
            if curr_card.get_rank_value() - 1 != next_card.get_rank_value():
                can_move = False
            count = count - 1
            card_pos = card_pos + 1

        count = len(stack_of_cards)
        card_pos = 0

        #Checks that stack_or_cards is in alternating color order
        while count > 0:
            curr_card = stack_of_cards[card_pos]
            next_card = stack_of_cards[card_pos + 1]
            if curr_card.get_suit_color == next_card.get_suit_color:
                can_move = False
            count = count - 1
            card_pos = card_pos + 1

        return can_move

    # Checks if the selected list of cards can be placed on the chosen pile
    @staticmethod
    def can_be_placed(pile_to_place_on, stack_of_cards):
        if pile_to_place_on.is_empty():
            return True
        card1 = stack_of_cards[0]  # Bottom of pile being placed on
        card2 = pile_to_place_on.cards[len(pile_to_place_on.get_cards()) - 1]  # Top of pile being placed

        if (card1.get_rank_value() + 1) == card2.get_rank_value():
            if card1.get_suit_color() != card2.get_suit_color():
                return True
        else:
            return False

    def get_cards(self):
        return self.cards
