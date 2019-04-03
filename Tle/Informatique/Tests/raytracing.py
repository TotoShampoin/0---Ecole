import math
import random
import pygame

pygame.init()

window = pygame.display.set_mode((256,256))
screen = pygame.surface.Surface((16,16))

w , h = screen.get_width() , screen.get_height()

pos = [8,8]

orien = 0

zone = [[0 for y in range(w)] for x in range(h)]
for a in range(4):
    x = random.randint(0,w-2)
    y = random.randint(0,h-2)
    zone[x][y] = 1

cont = True
while cont:
    view = [[0 for y in range(w)] for x in range(h)]
    for a in range(-45, 45, 1):
        for r in range(22):
            b = (orien+a)*math.pi/180
            x = round(r*math.cos(b)+pos[0])
            y = round(r*math.sin(b)+pos[1])
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
    pygame.time.Clock().tick(30)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]: pos[1] = (pos[1]-1)%h
    if key[pygame.K_DOWN]: pos[1] = (pos[1]+1)%h
    if key[pygame.K_LEFT]: pos[0] = (pos[0]-1)%w
    if key[pygame.K_RIGHT]: pos[0] = (pos[0]+1)%w
    if key[pygame.K_KP6]: orien =   0
    if key[pygame.K_KP3]: orien =  45
    if key[pygame.K_KP2]: orien =  90
    if key[pygame.K_KP1]: orien = 135
    if key[pygame.K_KP4]: orien = 180
    if key[pygame.K_KP7]: orien = 225
    if key[pygame.K_KP8]: orien = 270
    if key[pygame.K_KP9]: orien = 315

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cont = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                zone = [[0 for y in range(w)] for x in range(h)]
                for a in range(4):
                    x = random.randint(0,w-2)
                    y = random.randint(0,h-2)
                    zone[x][y] = 1
                    zone[x+1][y] = 1
                    zone[x+1][y+1] = 1
                    zone[x][y+1] = 1

pygame.quit()
