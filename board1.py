import pygame
import time
import sys
from card import Card
from pile import Pile
pygame.init()


class TextRectException:
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return self.message


class Board:

    def __init__(self):
        return

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BACKGROUND = (26, 155, 43)

    # Open a window
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Double Solitaire")

    clock = pygame.time.Clock()

    @staticmethod
    def start():
        # Text Surface
        basic_font = pygame.font.SysFont(None, 100)
        text = basic_font.render("Double Solitaire", True, Board.BLACK, Board.BACKGROUND)
        text_rect = text.get_rect()
        text_rect.centerx = Board.screen.get_rect().centerx
        text_rect.centery = 150

        # Buttons
        start_button = pygame.Rect((pygame.display.get_surface().get_width() / 2)-75, 250, 150, 25)
        instruct_button = pygame.Rect((pygame.display.get_surface().get_width() / 2)-75, 290, 150, 25)
        exit_button = pygame.Rect((pygame.display.get_surface().get_width() / 2)-75, 330, 150, 25)

        # startText Button
        basic_font_small = pygame.font.SysFont(None, 24)
        start_text = basic_font_small.render("Start", True, Board.BLACK, (275, 250))
        start_text_rect = start_text.get_rect()
        start_text_rect.centerx = start_button.centerx
        start_text_rect.centery = start_button.centery

        # instructText Button
        instruct_text = basic_font_small.render("Instructions", True, Board.BLACK, (275, 290))
        instruct_text_rect = instruct_text.get_rect()
        instruct_text_rect.centerx = instruct_button.centerx
        instruct_text_rect.centery = instruct_button.centery

        # exitText Button
        exit_text = basic_font_small.render("Exit", True, Board.BLACK, (275, 330))
        exit_text_rect = exit_text.get_rect()
        exit_text_rect.centerx = exit_button.centerx
        exit_text_rect.centery = exit_button.centery

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if start_button.collidepoint(mouse_pos):
                    time.sleep(.200)
                    return 3

                if instruct_button.collidepoint(mouse_pos):
                    time.sleep(.200)
                    return 2

                if exit_button.collidepoint(mouse_pos):
                    return 0

        Board.screen.fill(Board.BACKGROUND)
        Board.screen.blit(text, text_rect)

        pygame.draw.rect(Board.screen, Board.WHITE, start_button)
        pygame.draw.rect(Board.screen, Board.WHITE, instruct_button)
        pygame.draw.rect(Board.screen, Board.WHITE, exit_button)

        Board.screen.blit(start_text, start_text_rect)
        Board.screen.blit(instruct_text, instruct_text_rect)
        Board.screen.blit(exit_text, exit_text_rect)

        pygame.display.update()
        pygame.display.flip()

        Board.clock.tick(60)
        return 1

    @staticmethod
    def instruction_screen():
        #Back Button
        back_button = pygame.Rect(25, 25, 150, 25)

        #Background box
        black_rect = pygame.Rect(125, 25, 450, 450)

        #Text
        my_string = "Race against your opponent to see who can solve the " \
                    "game of solitaire first. Each player is distributed " \
                    "an identical solitaires layout, the player with the " \
                    "fastest solitaire time or with the most amount of cards " \
                    "stacked wins.\n\n" \
                    "HOW TO PLAY: Use the mouse or touchpad to drag cards " \
                    "into desired position"
        basic_font = pygame.font.SysFont(None, 40)
        small_font = pygame.font.SysFont(None, 24)
        black_rect = pygame.Rect(150, 150, 450, 450)
        back_text = small_font.render("Back", True, Board.BLACK, Board.WHITE)
        back_text_rect = back_text.get_rect()
        back_text_rect.centerx = back_button.centerx
        back_text_rect.centery = back_button.centery
        rendered_text = Board.render_textrect(my_string, basic_font, black_rect, Board.BLACK, Board.BACKGROUND, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if back_button.collidepoint(mouse_pos):
                    time.sleep(.200)
                    return 1

        Board.screen.fill(Board.BACKGROUND)

        pygame.draw.rect(Board.screen, Board.BACKGROUND, black_rect)
        pygame.draw.rect(Board.screen, Board.WHITE, back_button)

        Board.screen.blit(back_text, back_text_rect)
        Board.screen.blit(rendered_text, black_rect.topleft)

        pygame.display.update()
        pygame.display.flip()

        Board.clock.tick(60)

        return 2

    @staticmethod
    def waiting_screen():
        # Text Surface
        basic_font = pygame.font.SysFont(None, 48)
        text = basic_font.render("waiting for other player", True, Board.BLACK, Board.BACKGROUND)
        text_rect = text.get_rect()
        text_rect.centerx = Board.screen.get_rect().centerx
        text_rect.centery = 150

        #Button
        back_button = pygame.Rect((pygame.display.get_surface().get_width() / 2)-75, 250, 150, 25)

        # startText Button
        basic_font_small = pygame.font.SysFont(None, 24)
        back_text = basic_font_small.render("Back", True, Board.BLACK, (275, 250))
        back_text_rect = back_text.get_rect()
        back_text_rect.centerx = back_button.centerx
        back_text_rect.centery = back_button.centery

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if back_button.collidepoint(mouse_pos):
                    time.sleep(.200)
                    return 4

        Board.screen.fill(Board.BACKGROUND)
        Board.screen.blit(text, text_rect)

        pygame.draw.rect(Board.screen, Board.WHITE, back_button)
        Board.screen.blit(back_text, back_text_rect)

        pygame.display.update()
        pygame.display.flip()

        Board.clock.tick(60)
        return 3

    @staticmethod
    def game_screen(deck, pile1, pile2, pile3, pile4, pile5, pile6, pile7, suit_stack1, suit_stack2, suit_stack3, suit_stack4):
        size = (800, 600)
        display_surface = pygame.Surface(size)

        # Back Button
        quit_button = pygame.Rect(25, 25, 50, 20)

        # startText Button
        basic_font_small = pygame.font.SysFont(None, 24)
        quit_text = basic_font_small.render("Quit", True, Board.BLACK, (275, 250))
        quit_text_rect = quit_text.get_rect()
        quit_text_rect.centerx = quit_button.centerx
        quit_text_rect.centery = quit_button.centery

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if quit_button.collidepoint(mouse_pos):
                    time.sleep(.200)
                    return 1

        Board.screen.fill(Board.BACKGROUND)
        display_surface.fill(Board.BACKGROUND)

        Board.display_stack(deck, 0, display_surface)
        Board.display_stack(pile1, 1, display_surface)
        Board.display_stack(pile2, 2, display_surface)
        Board.display_stack(pile3, 3, display_surface)
        Board.display_stack(pile4, 4, display_surface)
        Board.display_stack(pile5, 5, display_surface)
        Board.display_stack(pile6, 6, display_surface)
        Board.display_stack(pile7, 7, display_surface)
        Board.display_stack(suit_stack1, 8, display_surface)
        Board.display_stack(suit_stack2, 9, display_surface)
        Board.display_stack(suit_stack3, 10, display_surface)
        Board.display_stack(suit_stack4, 11, display_surface)
        Board.screen.blit(display_surface, (0, 0))

        pygame.draw.rect(Board.screen, Board.WHITE, quit_button)
        Board.screen.blit(quit_text, quit_text_rect)
        pygame.display.update()
        pygame.display.flip()

        Board.clock.tick(60)
        return 4

    @staticmethod
    def render_textrect(string, font, rect, text_color, background_color, justification=0):
        final_lines = []

        requested_lines = string.splitlines()

        # Create a series of lines that will fit on the provided
        # rectangle.

        for requested_line in requested_lines:
            if font.size(requested_line)[0] > rect.width:
                words = requested_line.split(' ')
                # if any of our words are too long to fit, return.
                for word in words:
                    if font.size(word)[0] >= rect.width:
                        raise TextRectException("The word " + word + " is too long to fit in the rect passed.")
                # Start a new line
                accumulated_line = ""
                for word in words:
                    test_line = accumulated_line + word + " "
                    # Build the line while the words fit.
                    if font.size(test_line)[0] < rect.width:
                        accumulated_line = test_line
                    else:
                        final_lines.append(accumulated_line)
                        accumulated_line = word + " "
                final_lines.append(accumulated_line)
            else:
                final_lines.append(requested_line)

                # Let's try to write the text out on the surface.

        surface = pygame.Surface(rect.size)
        surface.fill(background_color)

        accumulated_height = 0
        for line in final_lines:
            # if accumulated_height + font.size(line)[1] >= rect.height:
            # raise TextRectException("Once word-wrapped, the text string was too tall to fit in the rect.")
            if line != "":
                tempsurface = font.render(line, 1, text_color)
                if justification == 0:
                    surface.blit(tempsurface, (0, accumulated_height))
                elif justification == 1:
                    surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
                elif justification == 2:
                    surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
                else:
                    raise TextRectException("Invalid justification argument: " + str(justification))
            accumulated_height += font.size(line)[1]

        return surface

    @staticmethod
    def display_card(card, x_pos, y_pos, surf):
        card_suit = card.get_suit_name()
        card_value = card.get_rank_value()

        if card_value == 0:
            card_value = "ace"
        if card_value == 11:
            card_value = "jack"
        if card_value == 12:
            card_value = "queen"
        if card_value == 13:
            card_value = "king"

        card_name = "PNG-cards-1.3\\" + str(card_value) + "_of_" + str(card_suit) + ".png"
        card_image = pygame.image.load(card_name)
        card_image = pygame.transform.scale(card_image, (80, 105))

        surf.blit(card_image, (x_pos, y_pos))
        return card_image

    @staticmethod
    def display_card_back(x_pos, y_pos, surf):
        card_name = "PNG-cards-1.3\\card_back.png"
        card_image = pygame.image.load(card_name)
        card_image = pygame.transform.scale(card_image, (80, 105))

        surf.blit(card_image, (x_pos, y_pos))
        return

    @staticmethod
    def display_empty_suit_stack(x_pos, y_pos, surf):
        outer_rect = (x_pos, y_pos, 80, 105)
        inner_rect = (x_pos + 5, y_pos + 5, 70, 95)
        pygame.draw.rect(surf, Board.WHITE, outer_rect)
        pygame.draw.rect(surf, Board.BACKGROUND, inner_rect)

        return

    @staticmethod
    def display_stack(card_stack, num_stack, surf):
        if num_stack == 0:
            x_pos = 20
            y_pos = 50
            Board.display_card_back(x_pos, y_pos, surf)
        if num_stack > 7 & num_stack < 12:
            cards = card_stack.get_cards()
            x_pos = ((num_stack - 7) * 110)+200
            y_pos = 50
            if not(card_stack.is_empty()):
                Board.display_card(cards.__getitem__(len(cards) - 1), x_pos, y_pos, surf)
            else:
                Board.display_empty_suit_stack(x_pos, y_pos, surf)
        if num_stack > 0 & num_stack < 8:
            cards = card_stack.get_cards()
            x_pos = ((num_stack - 1) * 110) + 25
            y_pos = pygame.display.get_surface().get_height() * (1/3) - 20
            count = 0
            while count <= len(cards) - 1:
                y_pos = y_pos + 25
                if cards.__getitem__(count).get_flipped():
                    Board.display_card(cards.__getitem__(count), x_pos, y_pos, surf)
                else:
                    Board.display_card_back(x_pos, y_pos, surf)
                count = count + 1
        return

    @staticmethod
    def move_card(card, surf):
        cont = True
        dragging = False

        while cont:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cont = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    dragging = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    dragging = False

                elif event.type == pygame.MOUSEMOTION:
                    if dragging:
                        mouse_pos = event.pos
                        surf.blit(card, mouse_pos)
            Board.screen.blit(surf, (0, 0))
            pygame.display.update()
            #pygame.display.flip()
        return

    @staticmethod
    def get_card_hover(mouse_pos):
        x_pos = mouse_pos[0]
        y_pos = mouse_pos[1]

        if(y_pos >= 50 & y_pos <= 155):
            implementLater = True

        if(y_pos >= 180):
            num1 = x_pos
            count1 = 0

            while num1 >= 110:
                num1 = num1 - 110
                count = count + 1

            if num1 >= 25:
                stack_number = count

            num2 = y_pos
            count2 = 0

            while num2 >= 180:
                num2 = num2 - 25
                count2 = count2 + 1





