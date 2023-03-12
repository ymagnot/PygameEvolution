import pygame
from pygame.locals import *
from sys import exit


largura=800
altura=600
y=altura/2-50
x=0

pygame.init()
pygame.display.set_caption('Mama Aqui')
tela=pygame.display.set_mode((largura,altura))
fps=pygame.time.Clock()

   
while True:
    fps.tick(280)
    tela.fill ((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_p:
                exit() 
 
    pygame.draw.rect(tela, (0,0,0), (x,y,50,50))
    if y >= altura:
        y = 0
    if x >= largura:
        x = 0

    y = y + 0
    x = x + 10


    pygame.display.update()       