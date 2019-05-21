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
timer = 3*60*60
enJeu = True
niv = Niveau("Test.txt")
niv.depart(player,timer)

def buffer():
    inView.fill(0)
    posX , posY = 0,0
    for x in range(16):
        for y in range(16):
            frame = niv.sol[x][y]
            if frame>3:
                inView.blit(coffres, (x*16,y*12), (int(frame/4)*48,(frame%4)*52,48,52))
            else:
                inView.blit(floors, (x*16+16,y*12+28), (frame*16,0,16,12))
            if (x == player.x and y == player.y) or (x == player.x and y == player.y+1) or (x == player.x+1 and y == player.y+1)or (x == player.x+1 and y == player.y):
                plfr = [int(player.frame[0])*16,int(player.frame[1]/2)*28]
                posX = player.x*16+16+player.tr_x
                posY = player.y*12+28+int(player.tr_y)-16
                inView.blit(sprites, (posX,posY),plfr+[16,28])
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
    control(player, enJeu)
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
