import pygame
pygame.init()

#Define colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND = (26, 155, 43)

#Open a window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Start Screen")

#Text Surface
basicFont = pygame.font.SysFont(None, 48)
text = basicFont.render("Double Solitaire", True, BLACK, BACKGROUND)
textRect = text.get_rect()
textRect.centerx = screen.get_rect().centerx
textRect.centery = 150

#Button
startButton = pygame.Rect(275, 250, 150, 25)
instructButton = pygame.Rect(275, 290, 150, 25)
exitButton = pygame.Rect(275,330, 150, 25)

#Text Button
basicFontSmall = pygame.font.SysFont(None, 24)
startText = basicFontSmall.render("Start", True, BLACK, (275, 250))
startTextRect = startText.get_rect()
startTextRect.centerx = startButton.centerx
startTextRect.centery = startButton.centery

#Text Button
instructText = basicFontSmall.render("Instructions", True, BLACK, (275, 290))
instructTextRect = instructText.get_rect()
instructTextRect.centerx = instructButton.centerx
instructTextRect.centery = instructButton.centery

#Text Button
exitText = basicFontSmall.render("Exit", True, BLACK, (275, 330))
exitTextRect = exitText.get_rect()
exitTextRect.centerx = exitButton.centerx
exitTextRect.centery = exitButton.centery

carryOn = True

clock = pygame.time.Clock()


while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos

        if startButton.collidepoint(mouse_pos):
            print("start button pressed")

        if instructButton.collidepoint(mouse_pos):
            print("instruction button pressed")

        if exitButton.collidepoint(mouse_pos):
            carryOn = False

    screen.fill(BACKGROUND)
    screen.blit(text, textRect)


    pygame.draw.rect(screen, WHITE, startButton)
    pygame.draw.rect(screen, WHITE, instructButton)
    pygame.draw.rect(screen, WHITE, exitButton)

    screen.blit(startText, startTextRect)
    screen.blit(instructText, instructTextRect)
    screen.blit(exitText, exitTextRect)

    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()