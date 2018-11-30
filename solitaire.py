import pygame
import sys
import time
from deck import Deck
from pile import Pile
from card import Card
from board1 import Board
from socket import *
import pickle

pygame.init()


class Solitaire:
    # print("Enter in IP address of server: ")
    # serverName = input()
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

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

    player_num = clientSocket.recv(1024).decode('utf-8')
    # deck = pickle.loads(clientSocket.recv(10000))
    deck = Deck()

    cards_highlighted = False

    my_score = 0
    opponent_score = 0
    elapsed_time = 0
    status = "continue"

    def __init__(self):
        return

    def deal(self):
        self.col1.add(self.deck.remove_card())
        self.col1.get_cards().__getitem__(len(self.col1.get_cards()) - 1).change_flipped()

        count = 0
        while count < 2:
            self.col2.add(self.deck.remove_card())
            count = count + 1
        self.col2.get_cards().__getitem__(len(self.col2.get_cards()) - 1).change_flipped()

        count = 0
        while count < 3:
            self.col3.add(self.deck.remove_card())
            count = count + 1
        self.col3.get_cards().__getitem__(len(self.col3.get_cards()) - 1).change_flipped()

        count = 0
        while count < 4:
            self.col4.add(self.deck.remove_card())
            count = count + 1
        self.col4.get_cards().__getitem__(len(self.col4.get_cards()) - 1).change_flipped()

        count = 0
        while count < 5:
            self.col5.add(self.deck.remove_card())
            count = count + 1
        self.col5.get_cards().__getitem__(len(self.col5.get_cards()) - 1).change_flipped()

        count = 0
        while count < 6:
            self.col6.add(self.deck.remove_card())
            count = count + 1
        self.col6.get_cards().__getitem__(len(self.col6.get_cards()) - 1).change_flipped()

        count = 0
        while count < 7:
            self.col7.add(self.deck.remove_card())
            count = count + 1
        self.col7.get_cards().__getitem__(len(self.col7.get_cards()) - 1).change_flipped()

    def draw_deck(self, card_to_add_back):
        self.deck.add_back(card_to_add_back)
        return self.deck.remove_card()

    def highlight_cards(self, cards_to_highlight):
        highlighted_cards = []
        stack_number = cards_to_highlight.__getitem__(0)
        first_highlighted = cards_to_highlight.__getitem__(1)
        count = 0

        if stack_number == 1:
            if first_highlighted >= len(self.col1.get_cards()):
                first_highlighted = len(self.col1.get_cards()) - 1
            while count < len(self.col1.get_cards()):
                if count >= first_highlighted:
                    self.col1.cards.__getitem__(count).change_highlighted()
                    highlighted_cards.append(self.col1.get_cards().__getitem__(count))
                    self.cards_highlighted = True
                count = count + 1
        elif stack_number == 2:
            if first_highlighted >= len(self.col2.get_cards()):
                first_highlighted = len(self.col2.get_cards()) - 1
            while count < len(self.col2.get_cards()):
                if count >= first_highlighted:
                    self.col2.cards.__getitem__(count).change_highlighted()
                    highlighted_cards.append(self.col2.get_cards().__getitem__(count))
                    self.cards_highlighted = True
                count = count + 1
        elif stack_number == 3:
            if first_highlighted >= len(self.col3.get_cards()):
                first_highlighted = len(self.col3.get_cards()) - 1
            while count < len(self.col3.get_cards()):
                if count >= first_highlighted:
                    self.col3.cards.__getitem__(count).change_highlighted()
                    highlighted_cards.append(self.col3.get_cards().__getitem__(count))
                    self.cards_highlighted = True
                count = count + 1
        elif stack_number == 4:
            if first_highlighted >= len(self.col4.get_cards()):
                first_highlighted = len(self.col4.get_cards()) - 1
            while count < len(self.col4.get_cards()):
                if count >= first_highlighted:
                    self.col4.cards.__getitem__(count).change_highlighted()
                    highlighted_cards.append(self.col4.get_cards().__getitem__(count))
                    self.cards_highlighted = True
                count = count + 1
        elif stack_number == 5:
            if first_highlighted >= len(self.col5.get_cards()):
                first_highlighted = len(self.col5.get_cards()) - 1
            while count < len(self.col5.get_cards()):
                if count >= first_highlighted:
                    self.col5.cards.__getitem__(count).change_highlighted()
                    highlighted_cards.append(self.col5.get_cards().__getitem__(count))
                    self.cards_highlighted = True
                count = count + 1
        elif stack_number == 6:
            if first_highlighted >= len(self.col6.get_cards()):
                first_highlighted = len(self.col6.get_cards()) - 1
            while count < len(self.col6.get_cards()):
                if count >= first_highlighted:
                    self.col6.cards.__getitem__(count).change_highlighted()
                    highlighted_cards.append(self.col6.get_cards().__getitem__(count))
                    self.cards_highlighted = True
                count = count + 1
        elif stack_number == 7:
            if first_highlighted >= len(self.col7.get_cards()):
                first_highlighted = len(self.col7.get_cards()) - 1
            while count < len(self.col7.get_cards()):
                if count >= first_highlighted:
                    self.col7.cards.__getitem__(count).change_highlighted()
                    highlighted_cards.append(self.col7.get_cards().__getitem__(count))
                    self.cards_highlighted = True
                count = count + 1
        return highlighted_cards

    def dehighlight_cards(self, cards_to_dehighlight):
        count = 0
        while count < len(cards_to_dehighlight):
            cards_to_dehighlight.__getitem__(count).change_highlighted()
            count = count + 1
        return

    def remove_cards(self, cards_pos, num_of_cards_to_remove):
        stack_number = cards_pos.__getitem__(0)
        count = 0
        if stack_number == 1:
            while count < num_of_cards_to_remove:
                self.col1.remove(len(self.col1.get_cards()) - 1)
                count = count + 1
        elif stack_number == 2:
            while count < num_of_cards_to_remove:
                self.col2.remove(len(self.col2.get_cards()) - 1)
                count = count + 1
        elif stack_number == 3:
            while count < num_of_cards_to_remove:
                self.col3.remove(len(self.col3.get_cards()) - 1)
                count = count + 1
        elif stack_number == 4:
            while count < num_of_cards_to_remove:
                self.col4.remove(len(self.col4.get_cards()) - 1)
                count = count + 1
        elif stack_number == 5:
            while count < num_of_cards_to_remove:
                self.col5.remove(len(self.col5.get_cards()) - 1)
                count = count + 1
        elif stack_number == 6:
            while count < num_of_cards_to_remove:
                self.col6.remove(len(self.col6.get_cards()) - 1)
                count = count + 1
        elif stack_number == 7:
            while count < num_of_cards_to_remove:
                self.col7.remove(len(self.col7.get_cards()) - 1)
                count = count + 1

    def flip_cards(self):
        if not self.col1.is_empty():
            self.col1.get_cards().__getitem__(len(self.col1.get_cards()) - 1).change_flipped()
        if not self.col2.is_empty():
            self.col2.get_cards().__getitem__(len(self.col2.get_cards()) - 1).change_flipped()
        if not self.col3.is_empty():
            self.col3.get_cards().__getitem__(len(self.col3.get_cards()) - 1).change_flipped()
        if not self.col4.is_empty():
            self.col4.get_cards().__getitem__(len(self.col4.get_cards()) - 1).change_flipped()
        if not self.col5.is_empty():
            self.col5.get_cards().__getitem__(len(self.col5.get_cards()) - 1).change_flipped()
        if not self.col6.is_empty():
            self.col6.get_cards().__getitem__(len(self.col6.get_cards()) - 1).change_flipped()
        if not self.col7.is_empty():
            self.col7.get_cards().__getitem__(len(self.col7.get_cards()) - 1).change_flipped()

    def start(self):
        self.deal()
        board = Board()
        screen_num = 1
        cards_to_highlight = [-1, -1]
        # print(self.player_num)
        while self.status == "continue":
            if screen_num == -1:
                self.clientSocket.send("-1".encode())
                self.status == "quit"

            if screen_num == 0:
                sys.exit(0)

            if screen_num == 1:
                time.sleep(.1)
                screen_num = board.start()

            if screen_num == 2:
                time.sleep(.1)
                screen_num = board.instruction_screen()

            if screen_num == 3:
                time.sleep(.1)
                screen_num = board.waiting_screen(self.clientSocket, self.player_num)

            if screen_num == 4:
                time.sleep(.1)
                screen_num = board.game_screen(self.deck, self.col1, self.col2, self.col3, self.col4, self.col5,
                                               self.col6, self.col7, self.suit_stack_1, self.suit_stack_2,
                                               self.suit_stack_3, self.suit_stack_4, self.my_score, self.opponent_score,
                                               self.elapsed_time, self.player_num)
            if cards_to_highlight.__getitem__(0) == -1:
                cards_to_highlight = Board.get_card_hover()
                highlighted_cards = Solitaire.highlight_cards(self, cards_to_highlight)
                self.clientSocket.send("0".encode())
            elif not cards_to_highlight.__getitem__(0) == -1:
                if self.cards_highlighted:
                    card_coordinates = Board.get_card_hover()
                    if card_coordinates.__getitem__(0) > 0 and card_coordinates.__getitem__(0) < 8:
                        cards_to_move_to = card_coordinates.__getitem__(0)

                        if Pile.can_be_moved(highlighted_cards):
                            if cards_to_move_to == 1:
                                if Pile.can_be_placed(self.col1, highlighted_cards):
                                    self.col1.add_to_stack(highlighted_cards)
                                    self.remove_cards(cards_to_highlight, len(highlighted_cards))
                                    cards_to_highlight = [-1, -1]
                                    self.clientSocket.send("5".encode())
                                else:
                                    cards_to_highlight = [-1, -1]
                                    self.dehighlight_cards(highlighted_cards)
                                    self.clientSocket.send("0".encode())
                            elif cards_to_move_to == 2:
                                if Pile.can_be_placed(self.col2, highlighted_cards):
                                    self.col2.add_to_stack(highlighted_cards)
                                    self.remove_cards(cards_to_highlight, len(highlighted_cards))
                                    cards_to_highlight = [-1, -1]
                                    self.clientSocket.send("5".encode())
                                else:
                                    cards_to_highlight = [-1, -1]
                                    self.dehighlight_cards(highlighted_cards)
                                    self.clientSocket.send("0".encode())
                            elif cards_to_move_to == 3:
                                if Pile.can_be_placed(self.col3, highlighted_cards):
                                    self.col3.add_to_stack(highlighted_cards)
                                    self.remove_cards(cards_to_highlight, len(highlighted_cards))
                                    cards_to_highlight = [-1, -1]
                                    self.clientSocket.send("5".encode())
                                else:
                                    cards_to_highlight = [-1, -1]
                                    self.dehighlight_cards(highlighted_cards)
                                    self.clientSocket.send("0".encode())
                            elif cards_to_move_to == 4:
                                if Pile.can_be_placed(self.col4, highlighted_cards):
                                    self.col4.add_to_stack(highlighted_cards)
                                    self.remove_cards(cards_to_highlight, len(highlighted_cards))
                                    cards_to_highlight = [-1, -1]
                                    self.clientSocket.send("5".encode())
                                else:
                                    cards_to_highlight = [-1, -1]
                                    self.dehighlight_cards(highlighted_cards)
                                    self.clientSocket.send("0".encode())
                            elif cards_to_move_to == 5:
                                if Pile.can_be_placed(self.col5, highlighted_cards):
                                    self.col5.add_to_stack(highlighted_cards)
                                    self.remove_cards(cards_to_highlight, len(highlighted_cards))
                                    cards_to_highlight = [-1, -1]
                                    self.clientSocket.send("5".encode())
                                else:
                                    cards_to_highlight = [-1, -1]
                                    self.dehighlight_cards(highlighted_cards)
                                    self.clientSocket.send("0".encode())
                            elif cards_to_move_to == 6:
                                if Pile.can_be_placed(self.col6, highlighted_cards):
                                    self.col6.add_to_stack(highlighted_cards)
                                    self.remove_cards(cards_to_highlight, len(highlighted_cards))
                                    cards_to_highlight = [-1, -1]
                                    self.clientSocket.send("5".encode())
                                else:
                                    cards_to_highlight = [-1, -1]
                                    self.dehighlight_cards(highlighted_cards)
                                    self.clientSocket.send("0".encode())
                            elif cards_to_move_to == 7:
                                if Pile.can_be_placed(self.col7, highlighted_cards):
                                    self.col7.add_to_stack(highlighted_cards)
                                    self.remove_cards(cards_to_highlight, len(highlighted_cards))
                                    cards_to_highlight = [-1, -1]
                                    self.clientSocket.send("5".encode())
                                else:
                                    cards_to_highlight = [-1, -1]
                                    self.dehighlight_cards(highlighted_cards)
                                    self.clientSocket.send("0".encode())
                        else:
                            self.clientSocket.send("0".encode())
                    else:
                        self.clientSocket.send("0".encode())

            self.flip_cards()

            if self.player_num == "1":
                # print("made it to recieving")
                self.clientSocket.send("ready".encode())
                self.my_score = self.clientSocket.recv(1024).decode('utf-8')
                self.clientSocket.send("ready".encode())
                self.opponent_score = self.clientSocket.recv(1024).decode('utf-8')
                self.clientSocket.send("ready".encode())
                self.elapsed_time = self.clientSocket.recv(1024).decode('utf-8')
                self.clientSocket.send("ready".encode())
                self.status = self.clientSocket.recv(1024).decode('utf-8')
                # print(self.my_score)
                # print(self.opponent_score)
                # print(self.elapsed_time)
                # print(self.status)
            elif self.player_num == "2":
                self.clientSocket.send("ready".encode())
                self.opponent_score = self.clientSocket.recv(1024).decode('utf-8')
                self.clientSocket.send("ready".encode())
                self.my_score = self.clientSocket.recv(1024).decode('utf-8')
                self.clientSocket.send("ready".encode())
                self.elapsed_time = self.clientSocket.recv(1024).decode('utf-8')
                self.clientSocket.send("ready".encode())
                self.status = self.clientSocket.recv(1024).decode('utf-8')
                # print(self.my_score)
                # print(self.opponent_score)
                # print(self.elapsed_time)
                # print(self.status)

        winner = self.clientSocket.recv(1024).decode()
        Board.winning_screen(winner)
