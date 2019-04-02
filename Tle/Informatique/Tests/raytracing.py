import math
import random
import pygame

pygame.init()

window = pygame.display.set_mode((256,256))
screen = pygame.surface.Surface((32,32))

w , h = screen.get_width() , screen.get_height()

zone = [[0 for y in range(w)] for x in range(h)]

pos = [8,8]

for a in range(6):
    x = random.randint(0,w-2)
    y = random.randint(0,h-2)
    zone[x  ][y  ] = 1
    zone[x+1][y  ] = 1
    zone[x+1][y+1] = 1
    zone[x  ][y+1] = 1

cont = True
while cont:
    view = [[0 for y in range(w)] for x in range(h)]
    for a in range(0, 360, 1):
        for r in range(16):
            b = a*math.pi/180
            x = int(r*math.cos(b)+pos[0])
            y = int(r*math.sin(b)+pos[1])
            if 0<=x<w and 0<=y<h:
                if zone[x][y]:
                    view[x][y] = 0
                    break
                else:
                    view[x][y] = 1

    for x in range(w):
        for y in range(h):
            pygame.draw.rect(screen, view[x][y]*16777215, (x,y,1,1))
            if zone[x][y]:
                pygame.draw.rect(screen, (255,0,0), (x,y,1,1))
    pygame.draw.rect(screen, (0,0,255), pos+[1,1])
    
    pygame.transform.scale(screen, window.get_size(), window)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
    key = pygame.key.get_pressed()
    if    key[pygame.K_UP]: pos[1] = (pos[1]-1)%h
    if  key[pygame.K_DOWN]: pos[1] = (pos[1]+1)%h
    if  key[pygame.K_LEFT]: pos[0] = (pos[0]-1)%w
    if key[pygame.K_RIGHT]: pos[0] = (pos[0]+1)%w

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cont = False

pygame.quit()
