import os
import pygame

pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
window = pygame.display.set_mode((0,0),pygame.NOFRAME)

rnbsqr = pygame.image.load("rnbsqr.png").convert_alpha()

pos = [32,32]

spd = 4

cont = True

while cont:
    window.fill(0)
    window.blit(rnbsqr, pos)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cont = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: cont = False
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]: pos[1] = (pos[1]-spd+16)%(window.get_height()+16)-16
    if key[pygame.K_DOWN]: pos[1] = (pos[1]+spd+16)%(window.get_height()+16)-16
    if key[pygame.K_LEFT]: pos[0] = (pos[0]-spd+16)%(window.get_width()+16)-16
    if key[pygame.K_RIGHT]: pos[0] = (pos[0]+spd+16)%(window.get_width()+16)-16

pygame.quit()
