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

txtIni= font.render(str("Iniciar Jogo"), True, WHITE)
window.blit(txtIni,[220,100])

txtPongClassic = font.render(str("Pong Classico"), True, WHITE)
window.blit(txtPongClassic,[190,200])

txtPongPaddle = font.render(str("Pong Less Paddle"), True, WHITE)
window.blit(txtPongPaddle,[210,300])

txtPongObjects = font.render(str("Pong Obstaculos"), True, WHITE)
window.blit(txtPongObjects,[210,400])

circleX = 350
circleY = 250

pygame.display.update()
while sys:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx > 190 and mx < 400 and my > 200 and my < 234:
                import PongClassic
            if mx > 210 and mx < 530 and my > 300 and my < 334:
                import PongLessPaddle
