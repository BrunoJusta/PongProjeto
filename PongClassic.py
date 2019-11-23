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
bounceBall= True
sys = True

##Pontuacoes
scorePlayer1 = 0
scorePlayer2 = 0

##Escreve as Pontuacoes
txtScore = font.render(str(scorePlayer1), True,WHITE)
scorePlacement = [175,20]
txtScore2 = font.render(str(scorePlayer2), True,WHITE)
scorePlacement2 = [525,20]

##Valor do countdown
i = 3

##Posicao Bola
circleX = 350
circleY = 250

#Velocidade Bola
velX = 5
velY = 5

#tempo
dt = 1

##Posicao inicial do Paddle
paddle1_Y = 215
paddle2_Y = 215

##Comprimento do Paddle 
paddle1_H = 80
paddle2_H = 80

##Update das Pontuacoes
def updateScore():
    window.blit(txtScore,[175,20])
    window.blit(txtScore2,[525,20])

##Funcao jogar outra vez
def continueGame(circleX, circleY, bounceBall, sys, txtScore, txtScore2):
    if scorePlayer1 > scorePlayer2:
        txtOver= OverFont.render(str("JOGADOR 1 VENCE!"), True, WHITE)
    elif scorePlayer1 < scorePlayer2:
        txtOver= OverFont.render(str("JOGADOR 2 VENCE!"), True, WHITE)
    window.blit(txtOver,[120,200])
    txtCONT= font.render(str("QUER CONTINUAR?"), True, WHITE)
    window.blit(txtCONT,[185,250])
    txtYES = font.render(str("SIM"), True, WHITE)
    window.blit(txtYES,[240,300])
    txtNO = font.render(str("NAO"), True, WHITE)
    window.blit(txtNO,[400,300])
    circleX = 350
    circleY = 250
    pygame.display.update()
    while sys:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                bounceBall = False 
                sys = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 240 and mx < 304 and my > 300 and my < 334:
                    sys = False
                if mx > 400 and mx < 464 and my > 300 and my < 334:
                    import PongMenu

##Countdown
while i > 0:
    txtCountdown = CountFont.render(str(i), True, WHITE)
    window.blit(txtCountdown,[325,225])
    pygame.display.update()
    time.sleep(1)
    i -= 1
    window.fill(BLUE)
    window.blit(txtScore, scorePlacement)
    
    ##DRAW NET 
    pygame.draw.line(window, GREEN, [350, 0], [350, 500], 5)
    pygame.draw.line(window, GREEN, [0, 70], [700, 70], 5)
    pygame.display.flip()

    ##SCORE 1
    window.blit(txtScore,scorePlacement)
    pygame.display.update()

    ##SCORE 2
    window.blit(txtScore2,scorePlacement2)
    pygame.display.update()

    
    paddle1 = pygame.draw.rect(window,DARKGREEN,(20,paddle1_Y,10,paddle1_H))
    paddle2 = pygame.draw.rect(window,DARKGREEN,(670,paddle2_Y,10,paddle2_H))
    pygame.display.update()

##iniciar o jogo
while bounceBall:

    ##Controlos
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
              bounceBall = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                     bounceBall=False
 
    ##movimento dos paddles                     
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_Y-=10
    if keys[pygame.K_s]:
        paddle1_Y+=10
    if keys[pygame.K_UP]:
        paddle2_Y-=10
    if keys[pygame.K_DOWN]:
        paddle2_Y+=10

    #bola a andar
    circleX += velX * dt
    circleY += velY * dt
        
    #limites paddle 1
    if paddle1_Y<80:
        paddle1_Y = 80
    if paddle1_Y>490-paddle1_H:
        paddle1_Y = 490-paddle1_H

    #limites paddle 2
    if paddle2_Y<80:
        paddle2_Y = 80
    if paddle2_Y>490-paddle2_H:
        paddle2_Y = 490-paddle2_H

    #Bola bater nas borda direita
    if circleX > 690:
                
        #Bola volta a posicao inicial
        circleX = 350 
        circleY = 250 
        #jogador um ganha um ponto
        scorePlayer1 += 1
        txtScore = font.render(str(scorePlayer1), True,WHITE)
        velY = 5
        dt = 1
        
    #Bola bater nas borda esquerda
    if circleX < 10:
        
        #Bola volta a posicao inicial
        circleX = 350
        circleY = 250

        #jogador dois ganha um ponto
        scorePlayer2+=1
        txtScore2 = font.render(str(scorePlayer2), True,WHITE)
        velY = 5
        dt = 1

    #Bola bater nas borda inferior
    if circleY > 490:
        circleY = 490
        velY = velY * -1
       
    #Bola bater nas borda superior
    if circleY < 80:
        circleY = 80
        velY = velY * -1

    ##colisao no paddle direito
    if (circleY+10)>=paddle2_Y and (circleY+10)<=(paddle2_Y+90) and circleX+10 == (670): 
        velX = velX * -1
        dt = random.randint(1,2)
        velY = random.randint(4,7) * -1
        
    
    ##colisao no paddle esquerdo
    if (circleY+10)>=paddle1_Y and (circleY+10)<=(paddle1_Y+90) and circleX+10 == (50): 
        velX = velX * -1
        dt = random.randint(1,2)
        velY = random.randint(4,7) * -1
        
         

    ##Jogo acaba quando a pontuacao chegar a 15
    if scorePlayer1 == 15 or scorePlayer2 == 15:
        continueGame(circleX, circleY, bounceBall, sys, txtScore, txtScore2)
        scorePlayer2 = 0
        txtScore2 = font.render(str(scorePlayer2), True,WHITE)
        scorePlayer1 = 0
        txtScore = font.render(str(scorePlayer1), True,WHITE)
        paddle1 = pygame.draw.rect(window, DARKGREEN, (20, paddle1_Y, 10, paddle1_H))
        paddle2 = pygame.draw.rect(window, DARKGREEN, (670, paddle2_Y, 10, paddle2_H))
        pygame.display.flip()

    ##Pinta a janela
    window.fill(BLUE)
    
    ##desenha os paddles
    paddle1 = pygame.draw.rect(window, DARKGREEN, (20, paddle1_Y, 10, paddle1_H))
    paddle2 = pygame.draw.rect(window, DARKGREEN, (670, paddle2_Y, 10, paddle2_H))
    
    ##desenha a rede
    pygame.draw.line(window, GREEN, [350, 0], [350, 500], 5)
    pygame.draw.line(window, GREEN, [0, 70], [700, 70], 5)

    ##Desenha a bola
    pygame.draw.circle(window, WHITE, (circleX, circleY), 10)

    pygame.display.flip()

    ##SCORE 1
    window.blit(txtScore,scorePlacement)
    pygame.display.update()

    ##SCORE 2
    window.blit(txtScore2,scorePlacement2)
    pygame.display.update()

    time.sleep(0.01)