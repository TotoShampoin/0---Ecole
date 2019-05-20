import pygame
from Classes import *

print("Initialisation")
pygame.init()
window = pygame.display.set_mode((1280,720))
screen = pygame.surface.Surface((640,360))
inView = pygame.surface.Surface((288,232))

sprites = pygame.image.load("PlayerSprites.png").convert_alpha()
floors  = pygame.image.load("Floors.png").convert_alpha()
coffres = pygame.image.load("Containers 4ways.png").convert_alpha()

clock = pygame.time.Clock()

player = Joueur()
timer = 0
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
            
    pygame.transform.scale(screen, window.get_size(), window)
    pygame.display.flip()
    clock.tick(60)

def control():
    key = pygame.key.get_pressed()          #Les fonctions où la touche peut être maintenue
    if key[pygame.K_DOWN]:                      #flèche bas
        player.frame[1] = 0
    if key[pygame.K_RIGHT]:                     #flèche droite
        player.frame[1] = 2
    if key[pygame.K_LEFT]:                      #flèche gauche
        player.frame[1] = 4
    if key[pygame.K_UP]:                        #flèche haut
        player.frame[1] = 6
    if key[pygame.K_DOWN] and key[pygame.K_RIGHT]:                  #bas droite
        player.frame[1] = 1
    if key[pygame.K_RIGHT] and key[pygame.K_UP]:                    #droite haut
        player.frame[1] = 3
    if key[pygame.K_LEFT] and key[pygame.K_DOWN]:                   #gauche haut
        player.frame[1] = 5
    if key[pygame.K_UP] and key[pygame.K_LEFT]:                     #flèche haut
        player.frame[1] = 7
    if key[32]:                                 #barre espace
        print("interagir")
    
    if key[pygame.K_DOWN] or key[pygame.K_UP] or key[pygame.K_RIGHT] or key[pygame.K_LEFT]:
        player.moving = True
    else:
        player.moving = False

def move():
    if player.moving:
        if player.tr_y==0:
            if player.frame[1] == 0:
                player.bouge( 0, 1)
            if player.frame[1] == 6:
                player.bouge( 0,-1)
        if player.tr_x==0:
            if player.frame[1] == 2:
                player.bouge( 1, 0)
            if player.frame[1] == 4:
                player.bouge(-1, 0)
        if player.tr_x==0 and player.tr_y==0:
            if player.frame[1] == 1:
                player.bouge( 1, 1)
            if player.frame[1] == 3:
                player.bouge( 1,-1)
            if player.frame[1] == 5:
                player.bouge(-1, 1)
            if player.frame[1] == 7:
                player.bouge(-1,-1)
        player.frame[0] = (player.frame[0]+1/8)%4
    else:
        player.frame[0] = 0
    if player.x<0:
        player.x = 0
        player.tr_x = 0
    if player.y<0:
        player.y = 0
        player.tr_y = 0
    if player.x>15:
        player.x = 15
        player.tr_x = 0
    if player.y>15:
        player.y = 15
        player.tr_y = 0
    player.routine()
            

print("Lancement de la boucle presque infinie")

cont = True
while cont:
    control()
    move()
    buffer()
    
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
