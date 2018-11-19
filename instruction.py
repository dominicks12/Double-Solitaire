import pygame, sys
pygame.init()
   #Define some colors


BLACK = (0,0,0)
GREEN = (26,155,43)
RED = (255, 0, 0)
WHITE = (255,255,255)
   #OPEN A NEW WINDOW
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Instructions")
button = pygame.Rect(12.5, 25, 100, 35)
black_rec = pygame.Rect(125, 25, 450, 450)
basicfont = pygame.font.SysFont(None, 48)
smallfont = pygame.font.SysFont(None,20)
text1 = basicfont.render(' Back', True, (0, 0, 0), (255, 255, 255))
carryOn = True
clock = pygame.time.Clock()

my_string = "                                             Instructions\n\n" \
           "Race against your opponent to see who can solve the game of solitaire first. Each player is distributed an identical solitaire layout," \
           "the player with the fastest solitaire time or with the most amount of cards stacked wins.\n\nHOW TO PLAY: Use the mouse or touchpad to drag cards into desired position"


class TextRectException:
   def __init__(self, message=None):
       self.message = message

   def __str__(self):
       return self.message


def render_textrect(string, font, rect, text_color, background_color, justification=0):


   import pygame

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
       if accumulated_height + font.size(line)[1] >= rect.height:
           raise TextRectException("Once word-wrapped, the text string was too tall to fit in the rect.")
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

while carryOn:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           carryOn = False
       if event.type == pygame.MOUSEBUTTONDOWN:
           mouse_pos = event.pos  # gets mouse position

           # checks if mouse position is over the button

           if button.collidepoint(mouse_pos):
               # prints current location of mouse
               print('button was pressed at {0}'.format(mouse_pos))
   screen.fill(GREEN)

   pygame.draw.rect(screen, BLACK, black_rec, 0)
   pygame.draw.rect(screen, WHITE,button)
   screen.blit(text1, button)
   pygame.display.flip()
   pygame.display.update()
   rendered_text = render_textrect(my_string,smallfont, black_rec,WHITE,BLACK,0)
   screen.blit(rendered_text, black_rec.topleft)
   pygame.display.update()
   clock.tick(60)
pygame.quit()

