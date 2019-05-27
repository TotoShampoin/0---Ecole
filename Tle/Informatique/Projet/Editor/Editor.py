import pygame
from Classes import *

pygame.init()

window = pygame.display.set_mode((1280,720))
inView = pygame.surface.Surface((288,232))

sprites = pygame.image.load("PlayerSprites.png").convert_alpha()
floors  = pygame.image.load("Floors.png").convert_alpha()
coffres = pygame.image.load("Containers 4ways.png").convert_alpha()

niv = Niveau("Map.txt")

cont = True
while cont:
    inView.fill(0)
    for x in range(16):
        for y in range(16):
            frame = niv.sol[y][x]
            if frame!=0:
                inView.blit(floors, (x*16+16,y*12+28), (frame*16,0,16,12))
                if frame>3:
                    inView.blit(coffres, (x*16,y*12), (int(frame/4)*96-48,(frame%4)*52,48,52))
            if y>1:
                frame = niv.sol[y-1][x]
                if frame!=0:
                    if frame>3:
                        inView.blit(coffres, (x*16,(y-1)*12), (int(frame/4)*96-48,(frame%4)*52,48,52))
    inView2 = pygame.transform.scale(inView, (864,696))
    window.blit(inView2, (0,0))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event == pygame.QUIT:
            cont = False
pygame.quit()
