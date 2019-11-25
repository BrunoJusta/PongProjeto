##importar libraria pygame
import pygame, time, random

##iniciar pygame
pygame.init()

##Definir Jaanela
window = pygame.display.set_mode((900,700))

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
txtIni= CountFont.render(str("PONG"), True, GREEN)
window.blit(txtIni,[310,100])
pygame.draw.line(window, GREEN, [70,118], [310,118], 5)
pygame.draw.line(window, GREEN, [80,138], [310,138], 5)
pygame.draw.line(window, GREEN, [80,158], [310,158], 5)
pygame.draw.line(window, GREEN, [70,116], [70,535], 5)


pygame.draw.line(window, GREEN, [620,118], [875,118], 5)
pygame.draw.line(window, GREEN, [620,138], [865,138], 5)
pygame.draw.line(window, GREEN, [620,158], [865,158], 5)
pygame.draw.line(window, GREEN, [875,116], [875,535], 5)


pygame.draw.line(window, GREEN,[70,535] ,  [875,535], 5)

txtPongClassic = font.render(str("EASY"), True, WHITE)
window.blit(txtPongClassic,[415,250])
pygame.draw.line(window, GREEN, [414,285], [508,285], 5)

txtPongPaddle = font.render(str("MEDIUM"), True, WHITE)
window.blit(txtPongPaddle,[395,350])
pygame.draw.line(window, GREEN, [390,385], [540,385], 5)

txtPongObjects = font.render(str("HARD"), True, WHITE)
window.blit(txtPongObjects,[415,450])
pygame.draw.line(window, GREEN, [410,485], [517,485], 5)

pygame.display.update()
while start:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            start = False
            pygame.quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx > 396 and mx < 540 and my > 239 and my < 300:
                import PongClassic
            if mx > 371 and mx < 564 and my > 334 and my < 391:
                import PongLessPaddle
            if mx > 382 and mx < 544 and my > 438 and my < 495:
                import PongObjects

