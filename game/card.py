from Rank import Rank
from Rank import Suit
import random

# ADD A TO STRING METHOD
class Card:

    def __init__(self):
        num1 = random.randint(0,13)
        num2 = random.randint(1,4)
        ranks = {
            0: Rank.ACE,
            1: Rank.ONE,
            2: Rank.TWO,
            3: Rank.THREE,
            4: Rank.FOUR,
            5: Rank.FIVE,
            6: Rank.SIX,
            7: Rank.SEVEN,
            8: Rank.EIGHT,
            9: Rank.NINE,
            10: Rank.TEN,
            11: Rank.JACK,
            12: Rank.QUEEN,
            13: Rank.KING
        }

        suits = {
            1: Suit.DIAMONDS,
            2: Suit.HEARTS,
            3: Suit.CLUBS,
            4: Suit.SPADES
        }

        self.rank = ranks.get(num1, "Could not assign a rank.")
        self.suit = suits.get(num2, "Could not assign a suit.")

    def get_rank_name(self):
        return self.rank.value[0]

    def get_rank_value(self):
        return self.rank.value[1]

    def get_suit_name(self):
        return self.suit.value[0]

    def get_suit_color(self):
        return self.suit.value[1]

    @staticmethod
    def compare_rank(card1, card2):
        """
            Compares the face values of two cards
        :param card1: a Card object
        :param card2: a Card object
        :return: 1 if card1 has a greater face value
                 0 if card1 and card2 have the same face value
                 -1 if card2 has a greater face value
        """
        if card1.get_rank < card2.get_rank:
            return -1
        elif card1.get_rank > card2.get_rank:
            return 1
        else:
            return 0

    @staticmethod
    def equals(card1, card2):
        if card1.get_rank.value[1] == card2.get_rank.value[1]:
            if card1.get_suit.value[0] == card2.get_suit.value[0]:
                return True
        return False
