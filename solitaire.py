import pygame
import sys
from deck import Deck
from pile import Pile
from board1 import Board

pygame.init()


class Solitaire:

    col1 = Pile()
    col2 = Pile()
    col3 = Pile()
    col4 = Pile()
    col5 = Pile()
    col6 = Pile()
    col7 = Pile()

    suit_stack_1 = Pile()
    suit_stack_2 = Pile()
    suit_stack_3 = Pile()
    suit_stack_4 = Pile()

    deck = Deck()

    def __init__(self):
        return

    def deal(self):
        self.col1.add(self.deck.remove_card())

        count = 0
        while count < 2:
            self.col2.add(self.deck.remove_card())
            count = count + 1

        count = 0
        while count < 3:
            self.col3.add(self.deck.remove_card())
            count = count + 1

        count = 0
        while count < 4:
            self.col4.add(self.deck.remove_card())
            count = count + 1

        count = 0
        while count < 5:
            self.col5.add(self.deck.remove_card())
            count = count + 1

        count = 0
        while count < 6:
            self.col6.add(self.deck.remove_card())
            count = count + 1

        count = 0
        while count < 7:
            self.col7.add(self.deck.remove_card())
            count = count + 1

    def draw_deck(self, card_to_add_back):
        self.deck.add_back(card_to_add_back)
        return self.deck.remove_card()

    def start(self):
        self.deal(self)
        board = Board()
        carryon = True
        screen_num = 1
        while carryon:
            if screen_num == 0:
                sys.exit(0)

            if screen_num == 1:
                screen_num = board.start()

            if screen_num == 2:
                screen_num = board.instruction_screen()

            if screen_num == 3:
                screen_num = board.waiting_screen()

            if screen_num == 4:
                screen_num = board.game_screen(self.deck, self.col1, self.col2, self.col3, self.col4, self.col5,
                                               self.col6, self.col7, self.suit_stack_1, self.suit_stack_2,
                                               self.suit_stack_3, self.suit_stack_4)
