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
start = True

#escreve os textos
txtIni= font.render(str("INICIAR JOGO"), True, WHITE)
window.blit(txtIni,[220,100])

txtPongClassic = font.render(str("Pong Classico"), True, WHITE)
window.blit(txtPongClassic,[210,200])

txtPongPaddle = font.render(str("Pong Less Paddle"), True, WHITE)
window.blit(txtPongPaddle,[190,300])

txtPongObjects = font.render(str("Pong Obstaculos"), True, WHITE)
window.blit(txtPongObjects,[200,400])

pygame.display.update()
while start:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            start = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx > 200 and mx < 461 and my > 190 and my < 237:
                import PongClassic
            if mx > 180 and mx < 494 and my > 282 and my < 341:
                import PongLessPaddle
            if mx > 210 and mx < 530 and my > 398 and my < 438:
                import PongObjects
