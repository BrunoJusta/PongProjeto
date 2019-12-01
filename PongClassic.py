##importar libraria pygame
import pygame, time, random

##iniciar pygame
pygame.init()

##Definir Jaanela
window = pygame.display.set_mode((900,700))

##cores
POLICE_BLUE =  (52, 73, 94)
GREEN = (65, 184, 131)
DARKGREEN = (51, 163, 113)
WHITE = (255, 255, 255)
YELLOW = (255, 207, 51)
BLUE = (64, 184, 255)

ballColor = WHITE

##fontes
font = pygame.font.Font(None, 100)
CountFont = pygame.font.Font(None,200)
OverFont = pygame.font.Font(None,80)
MenuFont = pygame.font.Font(None,25)


##Pintar a Janela de Preto
window.fill(POLICE_BLUE)

##Definir Variaveis
bounceBall= True
start = True

##Pontuacoes
scorePlayer1 = 0
scorePlayer2 = 0

##Escreve as Pontuacoes
txtScore = font.render(str(scorePlayer1), True,WHITE)
scorePlacement = [225,15]
txtScore2 = font.render(str(scorePlayer2), True,WHITE)
scorePlacement2 = [675,15]
menuBack = MenuFont.render(str("Menu [M]"), True,WHITE)
menuBackPlacement = [10,10]

##Valor do countdown
i = 3

##Posicao Bola
ballX = 450
ballY = 350

#Velocidade Bola
velX = 5
velY = 5

#tempo
dt = 1

##Posicao inicial do Paddle
paddle1_Y = 410
paddle2_Y = 410

##Comprimento do Paddle 
paddle1_H = 120
paddle2_H = 120

##Update das Pontuacoes
def updateScore():
     window.blit(txtScore,[225,15])
     window.blit(txtScore2,[675,15])
     window.blit(menuBack,[10,10])


##Funcao jogar outra vez
def continueGame(ballX, ballY, bounceBall, start, txtScore, txtScore2, ballColor):
    if scorePlayer1 > scorePlayer2:
        txtOver= OverFont.render(str("PLAYER 1 WINS!"), True, YELLOW)
    elif scorePlayer1 < scorePlayer2:
        txtOver= OverFont.render(str("PLAYER 2 WINS!"), True, BLUE)
    window.blit(txtOver,[230,200])
    txtCONT= OverFont.render(str("CONTINUE?"), True, WHITE)
    window.blit(txtCONT,[285,280])
    txtYES = OverFont.render(str("YES"), True, WHITE)
    window.blit(txtYES,[320,340])
    txtNO = OverFont.render(str("NO"), True, WHITE)
    window.blit(txtNO,[500,340])
    ballX = 450
    ballY = 350
    ballColor = WHITE
    pygame.display.update()
    while start:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                bounceBall = False 
                start = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 320 and mx < 433 and my > 343 and my < 385:
                    start = False
                if mx > 499 and mx < 583 and my > 343 and my < 385:
                    pygame.quit()


##Countdown
while i > 0:
    txtCountdown = CountFont.render(str(i), True, WHITE)
    window.blit(txtCountdown,[410,300])
    pygame.display.update()
    time.sleep(1)
    i -= 1
    window.fill(POLICE_BLUE)  

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
    if keys[pygame.K_m]:
        import PongMenu
    

    #bola a andar
    ballX += velX * dt
    ballY += velY * dt
        
    #limites paddle 1
    if paddle1_Y<100:
        paddle1_Y = 100
    if paddle1_Y>690-paddle1_H:
        paddle1_Y = 690-paddle1_H

    #limites paddle 2
    if paddle2_Y<100:
        paddle2_Y = 100
    if paddle2_Y>690-paddle2_H:
        paddle2_Y = 690-paddle2_H

    #Bola bater nas borda direita
    if ballX > 890:
                
        #Bola volta a posicao inicial
        ballX = 450 
        ballY = 350 
        #jogador um ganha um ponto
        scorePlayer1 += 1
        txtScore = font.render(str(scorePlayer1), True,WHITE)
        velY = 5
        dt = 1
        ballColor = WHITE

        
    #Bola bater nas borda esquerda
    if ballX < 10:
        
        #Bola volta a posicao inicial
        ballX = 450
        ballY = 350

        #jogador dois ganha um ponto
        scorePlayer2+=1
        txtScore2 = font.render(str(scorePlayer2), True,WHITE)
        velY = 5
        dt = 1
        ballColor = WHITE


    #Bola bater nas borda inferior
    if ballY > 690:
        ballY = 690
        velY = velY * -1
       
    #Bola bater nas borda superior
    if ballY < 100:
        ballY = 100
        velY = velY * -1

    ##colisao no paddle direito
    if (ballY+10)>=paddle2_Y and (ballY+10)<=(paddle2_Y+135) and ballX+10 == (870): 
        velX = velX * -1
        dt = random.randint(1,2)
        velY = random.randint(-5,5)
        ballColor = BLUE

        
        
    
    ##colisao no paddle esquerdo
    if (ballY+10)>=paddle1_Y and (ballY+10)<=(paddle1_Y+135) and ballX+10 == (50): 
        velX = velX * -1
        dt = random.randint(1,2)
        velY = random.randint(-5,5)
        ballColor = YELLOW
    
    if velY >= -3 and velY <= 3:
        velY = velY + 2

      
        
         

    ##Jogo acaba quando a pontuacao chegar a 5
    if scorePlayer1 == 5 or scorePlayer2 == 5:
        continueGame(ballX, ballY, bounceBall, start, txtScore, txtScore2, ballColor)
        scorePlayer2 = 0
        txtScore2 = font.render(str(scorePlayer2), True,WHITE)
        scorePlayer1 = 0
        txtScore = font.render(str(scorePlayer1), True,WHITE)
        paddle1_Y = 410
        paddle2_Y = 410
        pygame.display.flip()

    ##Pinta a janela
    window.fill(POLICE_BLUE)
    
    ##desenha os paddles
    paddle1 = pygame.draw.rect(window, YELLOW, (20, paddle1_Y, 10, paddle1_H))
    paddle2 = pygame.draw.rect(window, BLUE, (870, paddle2_Y, 10, paddle2_H))
    
    ##desenha a rede
    pygame.draw.line(window, GREEN, [450, 0], [450, 700], 5)
    pygame.draw.line(window, GREEN, [0, 90], [900, 90], 5)

    ##Desenha a bola
    pygame.draw.circle(window, ballColor, (ballX, ballY), 10)


    ##SCORE 1
    window.blit(txtScore,scorePlacement)
    ##SCORE 2
    window.blit(txtScore2,scorePlacement2)

    window.blit(menuBack,menuBackPlacement)

    pygame.display.update()

    time.sleep(0.01)