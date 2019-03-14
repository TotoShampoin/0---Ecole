import pygame
from random import *
from array import *
from math import *

maps = array('B')

i = 0
j = 0

level = [[randint(0,3) for i in range(16)] for j in range(16)] 


pygame.init()
ecran = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Test map")


tiles = pygame.image.load("Tiles.png").convert_alpha()

picLevel = pygame.Surface((256,256))

r = 2
q = .5

continuer = True
while continuer:
    pygame.draw.rect(ecran, (0, 0, 0), (0, 0, 640, 360))
    
    for i in range(len(level)):
        for j in range(len(level[i])):
            picx = int(level[i][j]%2)
            picy = int(level[i][j]/2)
            picLevel.blit(tiles, (i*16,j*16), (picx*16, picy*16, picx*16+16, picy*16+16))

    zoomLevel = pygame.transform.scale(picLevel, (1024,1024))
    
    if 4*round(q,2)!=r:
        dispLevel = pygame.transform.rotozoom(zoomLevel, 0., q)
    else:
        dispLevel = pygame.transform.scale(zoomLevel, (256*r, 256*r))

    ecran.blit(dispLevel, (0,0))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                r += 1
            if event.key == pygame.K_DOWN:
                r -= 1

    if r > round(q,2)*4:
        q+=.01
    if r < round(q,2)*4:
        q-=.01
    
pygame.quit()
