import pygame,sys
black = (0,0,0)
white = (255,255,255)
pygame.init()
pygame.font.init()

scoreP1 = 0
scoreP2 = 0 
fuente = pygame.font.Font(None,50)
player1 = fuente.render('Player1',1,(white))
player2 = fuente.render('Player2',1,(white))
scorePlayer1 = fuente.render(str(scoreP1),1,(white))
scorePlayer2 = fuente.render(str(scoreP2),1,(white))
size = (800,600)



screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

#coordenadas y velocidad
player1X = 50
player1Y = 300 -45
player1YSpeed = 0

player2X = 750
player2Y = 300 -45
player2YSpeed = 0

#cord ball

pelotaX = 400
pelotaY = 300
pelotaSpeedX = 5
pelotaSpeedY = 5

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            #player 1
            if event.key == pygame.K_w :
                player1YSpeed = -4
            if event.key == pygame.K_s:
                player1YSpeed = 4


            #player 2
            if event.key == pygame.K_UP:
                player2YSpeed = -4
            if event.key == pygame.K_DOWN:
                player2YSpeed = 4

            

        if event.type == pygame.KEYUP:
            #player 1
            if event.key == pygame.K_w :
                player1YSpeed = 0
            if event.key == pygame.K_s:
                player1YSpeed = 0


            #player 2
            if event.key == pygame.K_UP:
                player2YSpeed = 0
            if event.key == pygame.K_DOWN:
                player2YSpeed = 0

    
        
    if player1Y  < 0 :
        player1Y = 0 
    
    if player1Y  > 600-90 :
        player1Y = 600-90 
    
    if player2Y  < 0 :
        player2Y = 0 
    
    if player2Y  > 600-90 :
        player2Y = 600-90 
    


    if pelotaY > 590 or pelotaY <10:
        pelotaSpeedY *= -1

    if pelotaX >800 :
        pelotaX = 400
        pelotaY = 300

        scoreP1 +=1
        scorePlayer1 = fuente.render(str(scoreP1),1,(white))
        pelotaSpeedX *= -1
        pelotaSpeedY *= -1

    if pelotaX <0 :
        pelotaX = 400
        pelotaY = 300
        scoreP2+= 1
        scorePlayer2 = fuente.render(str(scoreP2),1,(white))
        pelotaSpeedX *= -1
        pelotaSpeedY *= -1

    #logica
    player1Y += player1YSpeed
    player2Y += player2YSpeed

    #ball moving 
    pelotaX += pelotaSpeedX
    pelotaY += pelotaSpeedY

    screen.fill(black)

    #draw in the screen 
    screen.blit(player1,(70,40))
    screen.blit(player2,(560,40))
    screen.blit(scorePlayer1,(70,550))
    screen.blit(scorePlayer2,(730,550))
    jugador1 = pygame.draw.rect(screen,white, (player1X,player1Y,15,90))
    pelota = pygame.draw.circle(screen,white,(pelotaX,pelotaY),10)
    jugador2 = pygame.draw.rect(screen,white, (player2X,player2Y,15,90))

    #colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelotaSpeedX *= -1

    pygame.display.flip()

    clock.tick(60)
