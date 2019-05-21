import pygame

def control(player, inGame):
    key = pygame.key.get_pressed()          #Les fonctions où la touche peut être maintenue
    if inGame:
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

def move(player, inGame):
    if inGame:
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
            
