from cmath import rect
import time
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
#tempo=60

pygame.display.set_caption('Gemidomentro')
pygame.mixer.music.set_volume (0.35)
tela=pygame.display.set_mode((largura,altura))
fps=pygame.time.Clock()
fonte=pygame.font.SysFont('courier_new', 25, True,)
tema=pygame.mixer.music.load('tema.mp3')
gemido=pygame.mixer.Sound('geme.wav')
gemido.set_volume (0.5)
pygame.mixer.music.play(-1)


while True:    
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
        

    mensagem=f'Gemidos : {ganhos}'
    mensagem2=fonte.render(mensagem, False, (255,255,255))
    #mensagemtempo=f'Tempo Restante : {tempo}'
    #mensagemtempo2=fonte.render(mensagemtempo, False, (255,255,255))    
    ponto1=pygame.draw.rect(tela, (30,144,255), (x,y,tamanho, tamanho2))
    ponto2=pygame.draw.rect(tela, (255,10,10), (x1,y1,50,50))
    tela.blit(mensagem2,(1,1))    
    #tela.blit(mensagemtempo2,(740,1))
    
    
    if ponto1.colliderect(ponto2):
          y1=randint(50,710)
          x1=randint(50,970)
          gemido.play()
          ganhos = ganhos + 1          
          #tamanho =  tamanho - 1
          #tamanho2 = tamanho2 - 1

    

    pygame.display.update()
