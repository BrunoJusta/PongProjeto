##importar libraria pygame
import pygame, time, random

##iniciar pygame
pygame.init()

##Definir Jaanela
window = pygame.display.set_mode((700,500))

##cores
BLUE =  (52, 73, 94)
GREEN = (65, 184, 131)
DARKGREEN = (51, 163, 113)
WHITE = (255, 255, 255)

##fontes
font = pygame.font.Font(None, 50)
CountFont = pygame.font.Font(None,150)
OverFont = pygame.font.Font(None,70)

##Pintar a Janela de Preto
window.fill(BLUE)

##Definir Variaveis
sys = True

##Countdown

txtCONT= font.render(str("Iniciar Jogo"), True, WHITE)
window.blit(txtCONT,[220,100])

txtPongClassic = font.render(str("Pong Classic"), True, WHITE)
window.blit(txtPongClassic,[190,200])

txtPongPaddle = font.render(str("Pong Dificil"), True, WHITE)
window.blit(txtPongPaddle,[210,300])

circleX = 350
circleY = 250

pygame.display.update()
while sys:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx > 210 and mx < 250 and my > 300 and my < 334:
                import PongClassic
            if mx > 400 and mx < 464 and my > 300 and my < 334:
                import PongLessPaddle
