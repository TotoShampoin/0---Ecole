import pygame
from Classes import *
from Command import *

print("Initialisation")
pygame.init()
window = pygame.display.set_mode((1280,720))
screen = pygame.surface.Surface((640,360))
inView = pygame.surface.Surface((288,232))

from Hud import *

sprites = pygame.image.load("PlayerSprites.png").convert_alpha()
floors  = pygame.image.load("Floors.png").convert_alpha()
coffres = pygame.image.load("Containers 4ways.png").convert_alpha()

clock = pygame.time.Clock()

player = Joueur()
enJeu = True
niv = Niveau("Test.txt")
timer = niv.time*60
niv.depart(player,timer)

diplayer = False

def buffer():
    inView.fill(0)
    posX , posY = 0,0
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
            px , py = player.x , player.y
            if (x == px and y == py) or (x == px and y == py+1) or (x == px+1 and y == py+1)or (x == px+1 and y == py):
                plfr = [int(player.frame[0])*16,int(player.frame[1]/2)*28]
                posX = px*16+16+player.tr_x
                posY = py*12+28+int(player.tr_y)-16
                inView.blit(sprites, (posX,posY),plfr+[16,28])
                if py<15:
                    frame = niv.sol[py+1][px]
                    if frame!=0:
                        if frame>3:
                            inView.blit(coffres, (px*16,(py+1)*12), (int(frame/4)*96-48,(frame%4)*52,48,52))
                if py<14:
                    frame = niv.sol[py+2][px]
                    if frame!=0:
                        if frame>3:
                            inView.blit(coffres, (px*16,(py+2)*12), (int(frame/4)*96-48,(frame%4)*52,48,52))
                if px<15:
                    frame = niv.sol[py][px+1]
                    if frame!=0:
                        if frame>3:
                            inView.blit(coffres, ((px+1)*16,(py)*12), (int(frame/4)*96-48,(frame%4)*52,48,52))
                if px>0 and py<15:
                    frame = niv.sol[py+1][px-1]
                    if frame!=0:
                        if frame>3:
                            inView.blit(coffres, ((px-1)*16,(py+1)*12), (int(frame/4)*96-48,(frame%4)*52,48,52))
                if px>0 and py<14:
                    frame = niv.sol[py+2][px-1]
                    if frame!=0:
                        if frame>3:
                            inView.blit(coffres, ((px-1)*16,(py+2)*12), (int(frame/4)*96-48,(frame%4)*52,48,52))
                
            
    inView2 = pygame.transform.scale(inView, (inView.get_width()*4,inView.get_height()*4))
    camX = posX
    camY = posY
    if camX<72: camX = 72
    if camX>200: camX = 200
    if camY<31: camY = 31
    if camY>173: camY = 173
    screen.blit(inView2, (0,0), ((camX-72)*4,(camY-31)*4,(camX+88)*4,(camY+58)*4))
    
    hud(screen, timer, player.sac, player.maxSac, enJeu)
            
    pygame.transform.scale(screen, window.get_size(), window)
    pygame.display.flip()
    clock.tick(60)


print("Lancement de la boucle presque infinie")

cont = True
while cont:
    control(player, enJeu, niv)
    move(player, enJeu)
    buffer()
    if enJeu:
        timer -= 1
    
    for event in pygame.event.get():        #Gestion des événements
        if event.type == pygame.QUIT:           #fermeture de la fenêtre
            cont = False
        if event.type == pygame.KEYDOWN:        #simple pression de touche de clavier
            if event.key == pygame.K_ESCAPE:        #touche échape, pour faire pause
                if enJeu:
                    enJeu = False
                else:
                    enJeu = True
                print(str(enJeu))

pygame.quit()
