import pygame

def plotxt(dest, color, text, pos):
    tileset = pygame.image.load("Graphics/ASCII.gif")
    np = list(tileset.get_palette())
    pos = list(pos)
    if type(color) == tuple:
        np[1] = color+(255,)
    if type(color) == int:
        np[1] = tuple(dest.get_palette()[color])
    tileset.set_palette(np)
    text = str(text)
    for i in range(len(text)):
        tileset.convert(32).set_colorkey((0,0,0,255))
        dest.blit(tileset, pos, ((ord(text[i])%16)*8,int(ord(text[i])/16)*8,8,8))
        pos[0] += 8
        
