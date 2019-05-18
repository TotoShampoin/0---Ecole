import pygame
from Classes import *

pygame.init()

Player = Joueur()

Map = Niveau("Test.txt")

Niveau.depart(Player)


cont = True
while cont:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cont = False

pygame.quit()
