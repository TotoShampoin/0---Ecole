import os
import pygame
import text

os.environ['SDL_VIDEO_WINDOW_POS'] = "319,551"
pygame.init()

window = pygame.display.set_mode((640,360))
screen = pygame.surface.Surface((320,180), 0, 8)

menu = {
    "  Play  ":{
        "1 player":1,
        "2 players":2,
        "3 players":3,
        "4 players":4},
    " Option ":{
        " Sound  ": True,
        " Music  ": True},
    "  Exit  ":None}
dmen = menu
curs = 0
imen = 0

cont = True
while cont:
    screen.fill(0)
    for i in dmen:
        text.plotxt(screen, 255, i, (128,96+list(dmen.keys()).index(i)*16))
        if type(dmen[i]) == bool and dmen[i]:
            text.plotxt(screen, 255, chr(4), (200,96+list(dmen.keys()).index(i)*16))
    text.plotxt(screen, 252, list(dmen.keys())[curs], (128,96+curs*16))
    pygame.transform.scale(screen.convert(32), window.get_size(), window)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cont = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                curs = (curs-1)%len(dmen)
            if event.key == pygame.K_DOWN:
                curs = (curs+1)%len(dmen)
            if event.key == pygame.K_RETURN:
                if type(dmen[list(dmen.keys())[curs]]) == dict:
                    dmen = dmen[list(dmen.keys())[curs]]
                    imen += 1
                elif type(dmen[list(dmen.keys())[curs]]) == bool:
                    if dmen[list(dmen.keys())[curs]]:
                        dmen[list(dmen.keys())[curs]] = False
                    else:
                        dmen[list(dmen.keys())[curs]] = True
                else:
                    cont = False
            if event.key == pygame.K_ESCAPE:
                dmen = menu
                imen -=1
                for j in range(imen):
                    dmen = dmen[list(dmen.keys())[0]]
                

pygame.display.quit()
