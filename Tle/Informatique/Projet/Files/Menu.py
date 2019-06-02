import pygame
from text import *

def plotbutton(px, py, lent, txt, col1, col2):
    col1 = pygame.color.Color(col1)
    col2 = pygame.color.Color(col2)
    pygame.draw.rect(screen, col2, (px-4,py-4,8*lent+8,8+8), 0)
    pygame.draw.rect(screen, col1, (px-4,py-4,8*lent+8,8+8), 1)
    plotxt(screen, tuple(col1[0:3]), txt, (px+(lent-len(txt))*8,py))



with open("config.txt", 'r') as f:
    config = eval(f.read())
with open("Levels.txt", 'r') as f:
    levels = eval(f.read())

print("Ouverture du menu")

pygame.init()
window = pygame.display.set_mode((640*config["zoom"],360*config["zoom"]), pygame.FULLSCREEN*config["fullscreen"])
screen = pygame.surface.Surface((640,360))

logo = pygame.image.load("Graphics/Logo.png")

cfgChg = config

curs = [0,0]
menu = {"Jouer":levels, "Options":config, "Autre":{"Quitter":None}}

x0 , y0 = 8 , 32

goPlay = False
cont = True
while cont:
    menu = {"Jouer":levels, "Options":config, "Autre":{"Quitter":None}}
    z = list(menu)
    u = list(menu[z[ curs[0] ]])
    if curs[1]>=len(u): curs[1] = len(u)-1
    
    screen.fill(0)
    screen.blit(logo, (0,0))
    for x in range(3):
        u = list(menu[z[x]])
        vx , vy = x0*8+x*8*24 , y0*8
        plotxt(screen, (255,170,85), str(z[x]), (vx+(11-len(str(z[x])))*8,vy))
        for y in range(len(u)):
            vx , vy = x0*8+x*8*24 , y0*8+3*8+y*16
            plotbutton(vx,vy,11, str(u[y]).title(), 0x55000000, 0xFFAA5500)
            if x==0:
                vx , vy = x0*8+x*8*24+12*8 , y0*8
                plotxt(screen, (255,85,85), "Score", (vx+(8-len(str(z[x])))*8,vy))
                vx , vy = x0*8+x*8*24+8*12 , y0*8+3*8+y*16
                plotxt(screen, (255,85,85), str( menu[z[0]][u[y]][1] ), (vx+(11-len(str( menu[z[0]][u[y]][1] )))*8,vy))
            if x==1:
                vx , vy = x0*8+x*8*24+8*12 , y0*8+3*8+y*16
                plotxt(screen, (255,85,85), str( menu[z[1]][u[y]] ), (vx,vy))
    x , y = curs[0] , curs[1]
    u = list(menu[z[x]])
    vx , vy = x0*8+x*8*24 , y0*8+3*8+y*16
    plotbutton(vx,vy,11, str(u[y]).title(), 0x55000000, 0xFF55AA00)
    pygame.transform.scale(screen, window.get_size(), window)
    pygame.display.flip()
    
    u = list(menu[z[ curs[0] ]])
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                curs[1] = ( curs[1]-1 ) % len(u)
            if event.key == pygame.K_DOWN:
                curs[1] = ( curs[1]+1 ) % len(u)
            if event.key == pygame.K_RIGHT:
                curs[0] = ( curs[0]+1 ) % len(z)
            if event.key == pygame.K_LEFT:
                curs[0] = ( curs[0]-1 ) % len(z)
            if event.key == pygame.K_SPACE:
                if curs[0]==0:
                    goPlay = levels[u[curs[1]]][0]
                    isPlay = list(levels)[curs[1]]
                    cont = False    
                if curs[0]==1:
                    if curs[1]==0:
                        config["zoom"] = (config["zoom"])%3 +1
                    if curs[1]==1:
                        config["fullscreen"] = bool((config["fullscreen"]+1)%2)
                    window = pygame.display.set_mode((640*config["zoom"],360*config["zoom"]), pygame.FULLSCREEN*config["fullscreen"])
                    f = open("config.txt","w+")
                    f.write("{\n    \"zoom\": "+str(config["zoom"])+",\n    \"fullscreen\": "+str(config["fullscreen"])+"\n}")
                    f.close()
                if curs[0]==2:
                    cont = False
                    
        if event.type == pygame.QUIT:
            cont = False
        

pygame.quit()
if goPlay:
    f = open("play.txt",'w+')
    f.write("\""+goPlay+"\"\n")
    f.write("\""+isPlay+"\"")
    f.close()
    from Playing import *
