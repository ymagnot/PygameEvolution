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
    pygame.display.update()       