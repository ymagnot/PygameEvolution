import pygame
from pygame.locals import *
from sys import exit


largura=1024
altura=768
y=altura/2-50
x=largura/2-50

pygame.init()
pygame.display.set_caption('ESTAVA 11 A 3')
tela=pygame.display.set_mode((largura,altura))
fps=pygame.time.Clock()

while True:
    fps.tick(60)
    tela.fill ((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                x=x-25
            if event.key == K_d:
                x=x+25
            if event.key == K_w:
                y=y-25
            if event.key == K_s:
                y=y+25
        if event.type == KEYDOWN:
            if event.key == K_p:
                exit() 

 
    pygame.draw.circle(tela, (30,144,255), (x,y,), 50)


    
    pygame.display.update()       