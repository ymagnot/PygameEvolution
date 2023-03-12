from cmath import rect
import time
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

altura=768
largura=1024
y=altura/2-19
x=largura/2-19
y1=randint(50,710)
x1=randint(50,970)
tamanho=19
tamanho2=19
ganhos=0
tempo=60
volumetema=0.25
tamanhocobra=1

pygame.display.set_caption('Gemidomentro')
pygame.mixer.music.set_volume (volumetema)
tela=pygame.display.set_mode((largura,altura))
fps=pygame.time.Clock()
fonte=pygame.font.SysFont('courier_new', 25, True,)
tema=pygame.mixer.music.load('tema.mp3')
gemido=pygame.mixer.Sound('geme.wav')
gemido.set_volume (0.5)
pygame.mixer.music.play(-1)

def crescimento(lcobra):
      for XeY in lcobra:
            pygame.draw.rect(tela, (30,144,255),(XeY[0], XeY[1], 15, 15))
lcobra=[]     

while True:    
    fps.tick(144)
    tela.fill ((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:  
            if event.key == K_p:
                exit()
                
    if pygame.key.get_pressed()[K_a]:
            x=x-4
    if pygame.key.get_pressed()[K_d]:
            x=x+4
    if pygame.key.get_pressed()[K_w]:
            y=y-4
    if pygame.key.get_pressed()[K_s]:
            y=y+4
        

    mensagem=f'Gemidos : {ganhos}'
    mensagem2=fonte.render(mensagem, False, (255,255,255))
    mensagemtempo=f'e Nao chora Nao'
    mensagemtempo2=fonte.render(mensagemtempo, False, (255,255,255))
    gemidao=f'AAAnnnnnnnnnn'
    gemidao2=fonte.render(gemidao, False, (255,255,255))    
    ponto1=pygame.draw.rect(tela, (30,144,255), (x,y,tamanho, tamanho2))
    ponto2=pygame.draw.rect(tela, (255,255,255), (x1,y1,15,15))
    tela.blit(mensagem2,(1,1))    
    tela.blit(mensagemtempo2,(777,1))     
    
    lcabeca=[]    
    lcabeca.append(x)
    lcabeca.append(y)    
    lcobra.append(lcabeca)
    if len(lcobra) > tamanhocobra:
          del lcobra[0]

    crescimento(lcobra)    
    
    if ponto1.colliderect(ponto2):
          y1=randint(50,710)
          x1=randint(50,970)          
          gemido.play()          
          ganhos = ganhos + 1          
          tamanhocobra = tamanhocobra + 1          
          tela.blit(gemidao2,(altura/2,740))              
                
                
                
    pygame.display.update()
