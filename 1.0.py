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
comprimentocobra = 5
volumetema = 0.1
ganhos = 0
prenivel= 0
nivel = 1
nivelmaximo = 0
nivelmaximo2 = 0
morreu = False
fontegameover = pygame.font.SysFont('courier_new', 75, True)
fonterecord = pygame.font.SysFont('courier_new', 20, True)

pygame.display.set_caption('Gemidomentro')
pygame.mixer.music.set_volume (volumetema)
tela = pygame.display.set_mode((largura,altura))
fps = pygame.time.Clock()
fonte = pygame.font.SysFont('courier_new', 25, True,)
tema = pygame.mixer.music.load('tema.mp3')
gemido = pygame.mixer.Sound('geme.wav')
gemido.set_volume (0.3)
pygame.mixer.music.play(-1)

def morte ():
    global y, x, y1, x1, ganhos, lcobra, lcabeca, comprimentocobra, morreu, velocidadecobra, avelocidade, dvelocidade, wvelocidade, svelocidade, nivel, nivelmaximo, nivelmaximo2
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
    nivelmaximo = 0
    comprimentocobra = 5    
    morreu = False

def crescimento(lcobra):
      for XeY in lcobra:
            pygame.draw.rect(tela, (50,205,50),(XeY[0], XeY[1], tamanhocorpocobra, tamanhocorpocobra2))
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
    gameover = f'MORREU'    
    gameover2 = fontegameover.render(gameover, True, (255,0,0))
    gm = f'Pressione R para Reiniciar'
    gm2 = fonte.render(gm, True, (255,255,255))
    gm3 = f'Maior Pontuação: {nivelmaximo2}'
    gm4 = fonterecord.render(gm3, True, (255,0,0))
    mensagem = f'Gemidos : {ganhos}'
    mensagem2 = fonte.render(mensagem, False, (255,255,255))
    mensagemnivel= f'Nivel :{nivel}'
    mensagemnivel2 = fonte.render(mensagemnivel, False, (255,255,255))
    gemidao = f'AAAnnnnnnnnnn'
    gemidao2 = fonte.render(gemidao, False, (255,255,255))    
    ponto1 = pygame.draw.rect(tela, (0,100,0), (x,y,tamanho, tamanho2))
    ponto2 = pygame.draw.rect(tela, (178,34,34), (x1,y1,tamanhocomida,tamanhocomida2))
    tela.blit(mensagem2,(1,1))    
    tela.blit(mensagemnivel2,(888,1)) 

    if x > largura:
        x = 0
    if x < 0:
        x = largura
    if y > altura:
        y = 0
    if y < 0:
        y = altura            

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
            tela.blit(gameover2,(altura/2-20,275))
            tela.blit(gm2,(305,650))
            tela.blit(gm4, (389, 390))          
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
          nivelmaximo = nivelmaximo + 1         
          comprimentocobra = comprimentocobra + 1
          if nivelmaximo >= nivelmaximo2:
              nivelmaximo2 = nivelmaximo
          else:
              pass               
          tela.blit(gemidao2,(altura/2,740))
                       
                
    pygame.display.update()

