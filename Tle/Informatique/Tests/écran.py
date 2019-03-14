import pygame

pygame.init()
screen = pygame.display.set_mode((256,256))

for r in range(4):
    for g in range(4):
        for b in range(4):
            pygame.draw.rect(screen, (int(r*255/3),int(g*255/3),int(b*255/3)),
                             (b*32+int(r%2)*128,g*32+int(r/2)*128,128,128))

pygame.display.flip()

