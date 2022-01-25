# Pygame Collision Detection Practice, Jada Dantzler, January 25, 2011, 1:54pm, v0.4

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

# Setup the player and food data structures.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []

for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSZIE))
