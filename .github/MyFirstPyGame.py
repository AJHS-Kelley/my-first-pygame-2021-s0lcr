# My First Pygame, Jada Dantzler, 11/29/21 2:28, v0.3

import pygame, sys
from pygame.locals import *

# Start PyGame
pygame.init()

# Setup our window.
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')

# Setup Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 225)
LILAC = (243, 230, 255)

# Setup font.
basicFont = pygame.font.SysFont(None, 48)

# Setup text.
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Fill background color.
windowSurface.fill(LILAC)

# Draw a polygon onto the screen.
pygame.draw.polygon(windowSurface, BLUE, (146, 0), (291, 106), (236, 277), (56, 277), (0, 106))