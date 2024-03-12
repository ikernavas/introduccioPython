# Lletra C amb Rectangles.

import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0,0)
BLANC = (255,255,255)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Rectangle')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    pantalla.fill(BLANC)
    rectangle1 =  pygame.Rect(110, 100, 300, 50)
    rectangle2 = pygame.Rect(110, 100, 50, 300)
    rectangle3 = pygame.Rect(110, 400, 300, 50)
    pygame.draw.rect(pantalla, VERMELL, rectangle1)
    pygame.draw.rect(pantalla, VERMELL, rectangle2)
    pygame.draw.rect(pantalla, VERMELL, rectangle3)
    pygame.display.update()
