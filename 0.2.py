import pygame
from pygame.locals import *
from sys import exit



pygame.init()
pygame.display.set_caption('Mama Aqui')

largura=800
altura=600
tela=pygame.display.set_mode((largura,altura))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (255,255,255), (400,250,50,50))
    pygame.draw.circle(tela, (50,255,50), (423,220), 25)
    pygame.draw.line(tela, (155,155,155), (0,0), (800,600), 10)
    pygame.draw.line(tela, (155,155,155), (0,600), (800,0), 10)
    
    pygame.display.update()       