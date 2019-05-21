import pygame

watch = pygame.image.load("Watch.png").convert_alpha()
pause = pygame.image.load("Pause.png").convert_alpha()

surfHud = pygame.surface.Surface((320,180))

timeWatch = pygame.surface.Surface((65,55))
sacWatch = pygame.surface.Surface((65,55))

def hud(surface, time, sac, maxSac, inGame):
    timeWatch.fill(0xcc00cc)
    timeWatch.blit(watch, (0,0), (0,0,65,55))
    if time%60<30:
        timeWatch.blit(watch, (30,21), (90,55,4,16))
    if time<0:
        if time%20<10:
            timeWatch.blit(watch, (20,12), (94,59,24,6))
    else:
        timeWatch.blit(watch, (20,12), (94,59,24,6))
    time = int(time/60)+1
    minute = str(int(time/60))
    if len(minute)<2:
        minute = "0"+minute
    seconde = str(time%60)
    if len(seconde)<2:
        seconde = "0"+seconde
    if time<0:
        minute , seconde = "00" , "00"
    for x in range(2):
        timeWatch.blit(watch, (13+x*9,21), (int(minute[x])*9,55,9,16))
    for x in range(2):
        timeWatch.blit(watch, (34+x*9,21), (int(seconde[x])*9,55,9,16))
    
    surfHud.fill(0xcc00cc)
    surfHud.blit(timeWatch, (0,0))
    surfHud.blit(sacWatch, (255,0))
    
    zoomHud = pygame.transform.scale(surfHud, (640,360))
    zoomHud.set_colorkey(0xcc00cc)
    
    surface.blit(zoomHud.convert_alpha(), (0,0))
    if not inGame:
        surface.blit(pause, (0,0))
    
