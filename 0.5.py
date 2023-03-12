import pygame
from pygame.locals import *
from sys import exit
from random import randint

largura=1024
altura=768
y=altura/2-50
x=largura/2-50
x1=randint(50,710)
y1=randint(50,970)

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
            if event.key == K_p:
                exit() 
    if pygame.key.get_pressed()[K_a]:
            x=x-25
    if pygame.key.get_pressed()[K_d]:
            x=x+25
    if pygame.key.get_pressed()[K_w]:
            y=y-25
    if pygame.key.get_pressed()[K_s]:
            y=y+25
    ponto1=pygame.draw.rect(tela, (30,144,255), (x,y,50,50))
    ponto2=pygame.draw.rect(tela, (255,10,10), (y1,x1,50,50))

    if ponto1.colliderect(ponto2):
          x1=randint(50,710)
          y1=randint(50,970)



    
    pygame.display.update()        