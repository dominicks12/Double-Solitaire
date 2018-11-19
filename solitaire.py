import pygame
import sys
from deck import Deck
from board1 import Board

pygame.init()


class Solitaire:

    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []

    suit_row1 = []
    suit_row2 = []
    suit_row3 = []
    suit_row4 = []

    deck = Deck()

    def __init__(self):
        return

    def deal(self):
        self.row1.append(self.deck.remove_card())

        count = 0
        while count < 2:
            self.row2.append(self.deck.remove_card())
            count = count + 1

        count = 0
        while count < 3:
            self.row3.append(self.deck.remove_card())
            count = count + 1

        count = 0
        while count < 4:
            self.row4.append(self.deck.remove_card())
            count = count + 1

        count = 0
        while count < 5:
            self.row5.append(self.deck.remove_card())
            count = count + 1

        count = 0
        while count < 6:
            self.row6.append(self.deck.remove_card())
            count = count + 1

        count = 0
        while count < 7:
            self.row7.append(self.deck.remove_card())
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
                screen_num = board.game_screen()
