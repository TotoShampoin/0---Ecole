import pygame
from text import *

watch = pygame.image.load("Watch.png").convert_alpha()
conte = pygame.image.load("Chest.png").convert_alpha()
pause = pygame.image.load("Pause.png").convert_alpha()

surfHud = pygame.surface.Surface((320,180))

timeWatch = pygame.surface.Surface((65,55))
sacWatch = pygame.surface.Surface((65,55))
chestWatch = pygame.surface.Surface((128,80))

def hud(surface, time, sac, maxSac, inGame, isOpen, niv, curs):
    if isOpen!=None: chest = niv.contenu[isOpen]
    timeWatch.fill(0xcc00cc)
    timeWatch.blit(watch, (0,0), (0,0,65,55))
    if time%60<30:
        timeWatch.blit(watch, (30,21), (90,55,4,16))
    if time<0:
        if time%20<10:
            timeWatch.blit(watch, (20,12), (94,59,24,6))
    else:
        timeWatch.blit(watch, (20,12), (94,59,24,6))
    tim = int(time/60)+1
    minute = str(int(tim/60))
    if len(minute)<2:
        minute = "0"+minute
    seconde = str(tim%60)
    if len(seconde)<2:
        seconde = "0"+seconde
    ms = str(int(time%60*10/6))
    if time<0:
        minute , seconde = "00" , "00"
    for x in range(2):
        timeWatch.blit(watch, (13+x*9,21), (int(minute[x])*9,55,9,16))
    for x in range(2):
        timeWatch.blit(watch, (34+x*9,21), (int(seconde[x])*9,55,9,16))
    
    sacWatch.fill(0xcc00cc)
    sacWatch.blit(watch, (0,0), (65,0,65,55))
    sacWatch.blit(watch, (34,12), (94,65,18,6))
    for x in range(int(sac/maxSac*8)):
        sacWatch.blit(watch, (17,40-4*x), (94,55,16,4))
    masse = str(sac)
    if len(masse)<2:
        masse = "0"+masse
    for x in range(2):
        sacWatch.blit(watch, (34+x*6,23), (int(masse[x])*6,71,6,10))
    sacWatch.blit(watch, (47,23), (60,71,4,10))
    
    surfHud.fill(0xcc00cc)
    surfHud.blit(timeWatch, (0,0))
    surfHud.blit(sacWatch, (255,0))
    if isOpen!=None:
        chestWatch.fill(0xffaa55)
        chestWatch.blit(conte, (0,0))
        for x in range(8):
            plotxt(chestWatch, (85,0,0), chest[x][0], (8,8+x*8))
        chestWatch.fill(0xff55aa, (8,8+curs*8,112,8))
        plotxt(chestWatch, (85,0,0), chest[curs][0], (8,8+curs*8))
        surfHud.blit(chestWatch, (192,56))
    
    zoomHud = pygame.transform.scale(surfHud, (640,360))
    zoomHud.set_colorkey(0xcc00cc)
    
    surface.blit(zoomHud.convert_alpha(), (0,0))
    if not inGame:
        surface.blit(pause, (0,0))
    
