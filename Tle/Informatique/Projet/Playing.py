import pygame
from Classes import *
from Command import *
from text import *

print("Initialisation")
pygame.init()
window = pygame.display.set_mode((1280,720))
screen = pygame.surface.Surface((640,360))
inView = pygame.surface.Surface((288,232))

plotxt(screen, (255,255,255), "Loading...", (8*39,8*22))
pygame.transform.scale(screen, window.get_size(), window)
pygame.display.flip()


from Hud import *

sprites = pygame.image.load("PlayerSprites.png").convert_alpha()
floors  = pygame.image.load("Floors.png").convert_alpha()
coffres = pygame.image.load("Containers 4ways.png").convert_alpha()
#meubles = pygame.image.load("Meubles.png").convert_alpha()

musique = pygame.mixer.Sound("Sneaky 2.wav")
muzike = pygame.mixer.Sound("Sneaky drum.wav")
alarme =  pygame.mixer.Sound("Alarme.wav")

clock = pygame.time.Clock()

muzike.play(loops=-1, maxtime=0, fade_ms=0)
muzike.set_volume(1)
musique.play(-1, 0, 0)
musique.set_volume(0)

player = Joueur()
enJeu = True
niv = Niveau("LVL 1.txt")
timer = niv.time*60
niv.depart(player,timer)
isOpen = None
curs = 0

diplayer = False

def plot(x,y,c):
    frame = niv.sol[y][x]
    idd = niv.coffres[y][x]
    if frame!=0:
        if c:
            if isOpen==idd and isOpen!=None:
                inView.blit(coffres, (x*16,y*12), (0,104,48,52))
            else:
                inView.blit(coffres, (x*16,y*12), (0,52,48,52))
        if frame>3:
            if isOpen==idd:
                inView.blit(coffres, (x*16,y*12), (int(frame/4)*96,(frame%4)*52,48,52))
            else:
                inView.blit(coffres, (x*16,y*12), (int(frame/4)*96-48,(frame%4)*52,48,52))
        if frame>47:
            #inView.blit(meubles, (x*16,y*12), (int(frame/4)*96-48,(frame%4)*52,48,52))

def buffer():
    inView.fill(0)
    posX , posY = 0,0
    for x in range(16):
        for y in range(16):
            frame = niv.sol[y][x]
            if frame!=0:
                plot(x,y,1)
            if y>0:
                plot(x,y-1,0)
            px , py = player.x , player.y
            if (x == px and y == py) or (x == px and y == py+1) or (x == px+1 and y == py+1) or (x == px+1 and y == py):
                plfr = [int(player.frame[0])*16,int(player.frame[1]/2)*28]
                posX = px*16+16+player.tr_x
                posY = py*12+28+int(player.tr_y)-16
                inView.blit(sprites, (posX,posY),plfr+[16,28])
                if py<15:
                    plot(px,py+1,0)
                if py<14:
                    plot(px,py+2,0)
                if px<15:
                    plot(px+1,py,0)
                if px>0:
                    plot(px-1,py,0)
                if px>0 and py<15:
                    plot(px-1,py+1,0)
                if px>0 and py<14:
                    plot(px-1,py+2,0)
                
            
    inView2 = pygame.transform.scale(inView, (inView.get_width()*4,inView.get_height()*4))
    camX = posX
    camY = posY
    if camX<72: camX = 72
    if camX>200: camX = 200
    if camY<31: camY = 31
    if camY>173: camY = 173
    screen.blit(inView2, (0,0), ((camX-72)*4,(camY-31)*4,(camX+88)*4,(camY+58)*4))
    
    hud(screen, timer, player.pdSac, player.maxSac, enJeu, isOpen, niv, curs)
            
    pygame.transform.scale(screen, window.get_size(), window)
    pygame.display.flip()


print("\nLancement de la boucle presque infinie")

plotxt(screen, (255,255,255), "PRET", (8*39,8*25))
pygame.transform.scale(screen, window.get_size(), window)
pygame.display.flip()

pygame.time.delay(1000)

muzike.stop()
musique.set_volume(1)

end = False
alar = False
win = False
cont = True
stop = False
while cont:
    if isOpen == None:
        stop = control(player, enJeu, niv)
    move(player, enJeu)
    buffer()
    clock.tick(60)
    if enJeu:
        timer -= 1
    
    if timer<=0:
        musique.stop()
        if not alar:
            alarme.play(0,0,0)
            alarme.set_volume(0.25)
            alar = True
    if timer<-120:
        alarme.stop()
        cont = False
        end = True
        win = False
    
    if stop:
        musique.stop()
        cont = False
        end = True
        win = True
    
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
            if event.key == pygame.K_SPACE:                                 #barre espace
                dirr = int(player.frame[1]/2)
                if isOpen==None:
                    if dirr == 0:
                        isOpen = niv.coffres[player.y+1][player.x]
                    if dirr == 1:
                        isOpen = niv.coffres[player.y][player.x+1]
                    if dirr == 2:
                        isOpen = niv.coffres[player.y][player.x-1]
                    if dirr == 3:
                        isOpen = niv.coffres[player.y-1][player.x]
                else:
                    isOpen = None
            if isOpen!=None:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        curs = (curs-1)%8
                    if event.key == pygame.K_DOWN:
                        curs = (curs+1)%8
                    if event.key == pygame.K_RETURN:
                        if niv.contenu[isOpen][curs] != [None, 0, 0]:
                            if len(player.sac)<player.maxSac:
                                player.sac += [niv.contenu[isOpen][curs]]
                                niv.contenu[isOpen][curs] = [None, 0, 0]

if end:
    muswin =  pygame.mixer.Sound("win c=.wav")
    musloose =  pygame.mixer.Sound("loose =c.wav")
    screen.fill(0)
    if win:
        timer = -120
        muswin.play(0,0,0)
        muswin.set_volume(1)
        plotxt(screen, (255,255,255),"Resultats", (8*4,8*2))
        gain = 0
        for i in range(len(player.sac)):
            plotxt(screen, (255,255,255), player.sac[i][0], (8*6,8*4+i*8))
            plotxt(screen, (255,255,255), str(player.sac[i][1])+" $", (8*25,8*4+i*8))
            gain += player.sac[i][1]
        plotxt(screen, (255,255,0), str(gain)+" $", (8*5,8*40))
    else:
        gain = 0
        for i in range(len(player.sac)):
            gain += player.sac[i][1]
        musloose.play(0,0,0)
        musloose.set_volume(1)
        plotxt(screen, (255,255,255),"Vous ne vous etes pas echape a temps", (8*21,8*25))
        plotxt(screen, (255,255,255)," Le proprietaire a appele la police", (8*21,8*26))
        plotxt(screen, (255,255,255),str(gain)+"$ qui tombent à l'eau", (8*30,8*28))
    pygame.transform.scale(screen, window.get_size(), window)
    pygame.display.flip()
    while timer>-420:
        timer -= 1
        clock.tick(60)
        for event in pygame.event.get():        #Gestion des événements
            if event.type == pygame.QUIT:           #fermeture de la fenêtre
                cont = False
else:
    musique.stop()

pygame.quit()

for name in dir():                  #Suppression intégrale
    if not name.startswith('_'):    #
        del globals()[name]         #
    
from menu import *
