# Pygame Collision Detection Practice, Jada Dantzler, January 19, 2011, 2:42pm, v0.3

import pygame, sys, random
from pygame.locals import *

# Setup PyGame
pygame.init()
mainClock = pygame.time.Clock()

# Setup PyGame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection 2022')

# Setup Colors
BLACK = (0, 0, 0)
GREEN = (O, 255, 0)
WHITE = (255, 255, 255)