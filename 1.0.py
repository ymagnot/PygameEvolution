from cmath import rect
import time
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

altura, largura = 768, 1024
y, x = altura/2-19, largura/2-19
y1, x1 = randint(50,710), randint(50,970)
controlex, controley= 5, 0
tamanho, tamanho2 = 20, 20
tamanhocorpocobra, tamanhocorpocobra2 = 20, 20
tamanhocomida, tamanhocomida2 = 20, 20
avelocidade, dvelocidade, wvelocidade, svelocidade = -5, 5, -5, 5
comprimentocobra = 3
volumetema = 0.1
ganhos = 0
prenivel= 0
nivel = 1
morreu = False


pygame.display.set_caption('Gemidomentro')
pygame.mixer.music.set_volume (volumetema)
tela = pygame.display.set_mode((largura,altura))
fps = pygame.time.Clock()
fonte = pygame.font.SysFont('courier_new', 25, True,)
tema = pygame.mixer.music.load('tema.mp3')
gemido = pygame.mixer.Sound('geme.wav')
gemido.set_volume (0.0)
pygame.mixer.music.play(-1)

def morte ():
    global y, x, y1, x1, ganhos, lcobra, lcabeca, comprimentocobra, morreu, velocidadecobra, avelocidade, dvelocidade, wvelocidade, svelocidade, nivel
    avelocidade, dvelocidade, wvelocidade, svelocidade = -5, 5, -5, 5
    nivel = 1
    y = altura/2-19
    x = largura/2-19
    y1 = randint(50,710)
    x1 = randint(50,970)
    ganhos = 0
    lcobra = []
    lcabeca = []
    velocidadecobra= 0
    comprimentocobra = 3
    morreu = False
    

    
def crescimento(lcobra):
      for XeY in lcobra:
            pygame.draw.rect(tela, (40,144,255),(XeY[0], XeY[1], tamanhocorpocobra, tamanhocorpocobra2))
lcobra = []     

while True:    
    fps.tick(59)
    tela.fill ((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:  
            if event.key == K_p:
                exit()    
        if event.type == KEYDOWN:
            if event.key == K_a:
                if controlex == dvelocidade:
                     pass
                else:            
                 controlex = avelocidade
                 controley = 0
            if event.key == K_d:
                if controlex == avelocidade:
                    pass
                else:
                 controlex = dvelocidade
                 controley = 0
            if event.key == K_w:
                if controley== svelocidade:
                    pass
                else:                    
                 controlex = 0
                 controley = wvelocidade
            if event.key == K_s:
                if controley== wvelocidade:
                    pass
                else:
                 controlex = 0
                 controley = svelocidade

        
    x = x + controlex
    y = y + controley
    mensagem = f'Gemidos : {ganhos}'
    mensagem2 = fonte.render(mensagem, False, (255,255,255))
    mensagemnivel= f'Nivel :{nivel}'
    mensagemnivel2 = fonte.render(mensagemnivel, False, (255,255,255))
    gemidao = f'AAAnnnnnnnnnn'
    gemidao2 = fonte.render(gemidao, False, (255,255,255))    
    ponto1 = pygame.draw.rect(tela, (30,144,255), (x,y,tamanho, tamanho2))
    ponto2 = pygame.draw.rect(tela, (255,255,255), (x1,y1,tamanhocomida,tamanhocomida2))
    tela.blit(mensagem2,(1,1))    
    tela.blit(mensagemnivel2,(888,1)) 

    if prenivel == 10:
        nivel = nivel + 1
        prenivel = 0
    else:
        pass
    
            
    
    lcabeca = []    
    lcabeca.append(x)
    lcabeca.append(y)    
    lcobra.append(lcabeca)
    if len(lcobra) > comprimentocobra:
          del lcobra[0]

    crescimento(lcobra)
    if lcobra.count(lcabeca) > 1:
        morreu = True
        while morreu:
            tela.fill((0,0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        morte()    
                
        

    
    
    
    if ponto1.colliderect(ponto2):
          tela.blit(gemidao2,(altura/2,740))
          pygame.display.update()
          gemido.play()
          y1 = randint(40,710)
          x1 = randint(40,970)
          ganhos = ganhos + 1
          avelocidade = avelocidade - 0.1
          dvelocidade = dvelocidade + 0.1
          svelocidade = svelocidade + 0.1
          wvelocidade = wvelocidade - 0.1
          prenivel = prenivel + 1

          print (prenivel)
          comprimentocobra = comprimentocobra + 1          
          tela.blit(gemidao2,(altura/2,740))
                       
                
    pygame.display.update()