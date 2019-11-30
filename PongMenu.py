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
window.blit(txtIni,[300,60])
pygame.draw.line(window, GREEN, [28,70], [280,70], 5)
pygame.draw.line(window, GREEN, [50,90], [280,90], 5)
pygame.draw.line(window, GREEN, [50,110],[280,110], 5)
pygame.draw.line(window, GREEN, [30,68], [30, 670], 5)


pygame.draw.line(window, GREEN, [630,70], [872,70], 5)
pygame.draw.line(window, GREEN, [630,90], [850,90], 5)
pygame.draw.line(window, GREEN, [630,110], [850,110], 5)
pygame.draw.line(window, GREEN, [870,70], [870,670], 5)


pygame.draw.line(window, GREEN,[28,670] ,  [872,670], 5)

txtPongClassic = font.render(str("EASY"), True, WHITE)
window.blit(txtPongClassic,[400,250])
pygame.draw.line(window, GREEN, [399,285], [492,285], 5)

txtPongPaddle = font.render(str("MEDIUM"), True, WHITE)
window.blit(txtPongPaddle,[380,350])
pygame.draw.line(window, GREEN, [379,385], [520,385], 5)

txtPongObjects = font.render(str("HARD"), True, WHITE)
window.blit(txtPongObjects,[400,450])
pygame.draw.line(window, GREEN, [399,485], [500,485], 5)


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

    

