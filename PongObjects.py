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
RED = (255,0,0)

##fontes
font = pygame.font.Font(None, 100)
CountFont = pygame.font.Font(None,200)
OverFont = pygame.font.Font(None,80)

##Pintar a Janela de Preto
window.fill(BLUE)

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

#contador
i = 3

##Posicao da bola
ballX = 450
ballY = 350

#velocidade bola
velX = 10
velY = 10

#tempo
dt = 1

##Posicao inicial do paddle
paddle1_Y = 410
paddle2_Y = 410

#comprimento do paddle
paddle1_H = 120
paddle2_H = 120

#objeto1
object1_Y = 160
object1_YFinal = object1_Y + 60

#objeto2
object2_Y = 600
object2_YFinal = object2_Y + 60

#objeto3
object3_Y = 160
object3_YFinal = object3_Y + 60

#objeto4
object4_Y = 600
object4_YFinal = object4_Y + 60

'''___Update das Pontuacoes___'''
def updateScore():
    window.blit(txtScore,[225,15])
    window.blit(txtScore2,[675,15])

'''___Funcao jogar outra vez___'''
def continueGame(ballX, ballY, bounceBall, start, txtScore, txtScore2):
    if scorePlayer1 > scorePlayer2:
        txtOver= OverFont.render(str("PLAYER 1 WINS!"), True, WHITE)
    elif scorePlayer1 < scorePlayer2:
        txtOver= OverFont.render(str("PLAYER 2 WINS!"), True, WHITE)
    window.blit(txtOver,[230,200])
    txtCONT= OverFont.render(str("CONTINUE?"), True, WHITE)
    window.blit(txtCONT,[285,280])
    txtYES = OverFont.render(str("YES"), True, WHITE)
    window.blit(txtYES,[320,340])
    txtNO = OverFont.render(str("NO"), True, WHITE)
    window.blit(txtNO,[500,340])
    ballX = 450
    ballY = 350
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
                if mx > 499 and mx < 583 and my > 342 and my < 384:
                   import PongMenu

'''___Countdown___'''
while i > 0:
    txtCountdown = CountFont.render(str(i), True, WHITE)
    window.blit(txtCountdown,[415,300])
    pygame.display.update()
    time.sleep(1)
    i -= 1
    window.fill(BLUE)
    
'''___iniciar o jogo____'''
while bounceBall:

    #controlos
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
              bounceBall = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                     bounceBall=False
 
    ##movimento dos paddles                     
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_Y-=15
    if keys[pygame.K_s]:
        paddle1_Y+=15
    if keys[pygame.K_UP]:
        paddle2_Y-=15
    if keys[pygame.K_DOWN]:
        paddle2_Y+=15
    
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

         #posicoes aleatorias dos objetos
        #obejto1
        object1_Y = random.randint(160,280)
        object1_YFinal = object1_Y + 60
        #obejto2
        object2_Y = random.randint(300,600)
        object2_YFinal = object2_Y + 60
        #obejto3
        object3_Y = random.randint(160,280)
        object3_YFinal = object3_Y + 60
        #obejto4
        object4_Y = random.randint(300,600)
        object4_YFinal = object4_Y + 60
        
        #jogador um ganha um ponto
        scorePlayer1 += 1
        txtScore = font.render(str(scorePlayer1), True,WHITE)

        #repoe as variaveis
        velY = 10
        dt = 1

        #se o jogador tiver mais de 10 pontos ao marcar um ponto o paddle do inimigo diminui
        if scorePlayer1 > 5:
            paddle2_H -=20

        #se o jogador tiver o paddle diminuido ao marcar um ponto o paddle volta a aumentar
        if paddle1_H < 120:
            paddle1_H +=20

    #Bola bater nas borda esquerda
    if ballX < 10:

        #Bola volta a posicao inicial
        ballX = 450
        ballY = 350

        #posicoes aleatorias dos objetos
        #obejto1
        object1_Y = random.randint(160,280)
        object1_YFinal = object1_Y + 60
        #obejto2
        object2_Y = random.randint(300,600)
        object2_YFinal = object2_Y + 60
        #obejto3
        object3_Y = random.randint(160,280)
        object3_YFinal = object3_Y + 60
        #obejto4
        object4_Y = random.randint(300,600)
        object4_YFinal = object4_Y + 60

        #jogador dois ganha um ponto
        scorePlayer2+=1
        txtScore2 = font.render(str(scorePlayer2), True,WHITE)

        #repoe as variavies
        velY = 10
        dt = 1

        #se o jogador tiver mais de 10 pontos ao marcar um ponto o paddle do inimigo diminui
        if scorePlayer2 > 5:
            paddle1_H -= 20
        
        #se o jogador tiver o paddle diminuido ao marcar um ponto o paddle volta a aumentar
        if paddle2_H < 120:
            paddle2_H +=20

    #Bola bater nas borda inferior
    if ballY > 690:
        ballY = 690
        velY = velY * -1

    #Bola bater nas borda superior
    if ballY < 100:
        ballY = 100
        velY = velY * -1

    ##colisao no objeto 1
    if (ballY+10)>=object1_Y and (ballY+10)<=(object1_Y+75) and ballX+10 == (150): 
        velX = velX * -1
        velY = random.randint(2,4)* -1
        dt = 1

    ##colisao no objeto 2
    if (ballY+10)>=object2_Y and (ballY+10)<=(object2_Y+75) and ballX+10 == (350): 
        velX = velX * -1
        velY = random.randint(8,10)* -1
        dt = 1

    ##colisao no objeto 3
    if (ballY+10)>=object3_Y and (ballY+10)<=(object3_Y+75) and ballX+10 == (550): 
        velX = velX * -1
        velY = random.randint(2,4)* -1
        dt = 1

    ##colisao no objeto 4
    if (ballY+10)>=object4_Y and (ballY+10)<=(object4_Y+75) and ballX+10 == (750): 
        velX = velX * -1
        velY = random.randint(8,10)* -1
        dt = 1

    ##colisao no paddle esquerdo
    if (ballY+10)>=paddle1_Y+10 and (ballY+10)<=(paddle1_Y+paddle1_H+10) and ballX+10 == (50): 
        velX = velX * -1
        dt = random.randint(1,2)
        velY = random.randint(4,5) * -1

    ##colisao no paddle direito
    if (ballY+10)>=paddle2_Y+10 and (ballY+10)<=(paddle2_Y+paddle2_H+10) and ballX+10 == (870): 
        velX = velX * -1
        dt = random.randint(1,2)
        velY = random.randint(4,5) * -1
        
    ##Jogo acaba quando a pontuacao chegar ao 30 ou quando um dos paddles deixar de existir
    if scorePlayer1 == 30 or scorePlayer2 == 30 or paddle1_H == 0 or paddle2_H == 0:
        continueGame(ballX, ballY, bounceBall, start, txtScore, txtScore2)
        scorePlayer2 = 0
        txtScore2 = font.render(str(scorePlayer2), True,WHITE)
        scorePlayer1 = 0
        txtScore = font.render(str(scorePlayer1), True,WHITE)
        paddle1_H = 120
        paddle2_H = 120
        paddle1 = pygame.draw.rect(window, DARKGREEN, (20, paddle1_Y, 10, paddle1_H))
        paddle2 = pygame.draw.rect(window, DARKGREEN, (870, paddle2_Y, 10, paddle2_H))
        pygame.display.flip()

    ##Pinta a janela
    window.fill(BLUE)
    
    ##desenha os paddles
    paddle1 = pygame.draw.rect(window, DARKGREEN, (20, paddle1_Y, 10, paddle1_H))
    paddle2 = pygame.draw.rect(window, DARKGREEN, (870, paddle2_Y, 10, paddle2_H))
    ##desenha a rede
    pygame.draw.line(window, GREEN, [450, 0], [450, 700], 5)
    pygame.draw.line(window, GREEN, [0, 90], [900, 90], 5)

    ##Desenha a bola
    pygame.draw.circle(window, WHITE, (ballX, ballY), 10)


    pygame.draw.line(window, RED, [150, object1_Y], [150, object1_YFinal], 10)
    pygame.draw.line(window, WHITE, [350, object2_Y], [350, object2_YFinal], 10)

    pygame.draw.line(window, RED, [550, object3_Y], [550, object3_YFinal], 10)
    pygame.draw.line(window, WHITE, [750, object4_Y], [750, object4_YFinal], 10)


    ##SCORE 1
    window.blit(txtScore,scorePlacement)
    ##SCORE 2
    window.blit(txtScore2,scorePlacement2)
    pygame.display.update()

    time.sleep(0.01)
   
