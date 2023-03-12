from cmath import rect
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

altura=768
largura=1024
y=altura/2-50
x=largura/2-50
y1=randint(50,710)
x1=randint(50,970)
tamanho=50
tamanho2=50
ganhos=0

pygame.display.set_caption('ESTAVA 11 A 3, E A LOUD PERDEU..')
tela=pygame.display.set_mode((largura,altura))
fps=pygame.time.Clock()
fonte=pygame.font.SysFont('courier_new', 25, True,)


while True:
    mensagem=f'Putas : {ganhos}'
    mensagem2=fonte.render(mensagem, False, (255,255,255))
    fps.tick(120)
    tela.fill ((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_p:
                exit() 
    if pygame.key.get_pressed()[K_a]:
            x=x-15
    if pygame.key.get_pressed()[K_d]:
            x=x+15
    if pygame.key.get_pressed()[K_w]:
            y=y-15
    if pygame.key.get_pressed()[K_s]:
            y=y+15
    ponto1=pygame.draw.rect(tela, (30,144,255), (x,y,tamanho, tamanho2))
    ponto2=pygame.draw.rect(tela, (255,10,10), (x1,y1,50,50))
    tela.blit(mensagem2,(1,1))
    if ponto1.colliderect(ponto2):
          y1=randint(50,710)
          x1=randint(50,970)
          ganhos = ganhos + 1
          '''print (ganhos)  
          tamanho =  tamanho - 1
          tamanho2 = tamanho2 - 1'''
          






 
    pygame.display.update()        