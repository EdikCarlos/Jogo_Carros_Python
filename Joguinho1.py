import pygame
from random import randint
from time import sleep
pygame.init()
fim = 0
#Dados Tela
timer = 0
segundos = 0
#Dados Player
x = 190
y = 250
velocidade = 20
#Dados Carro rosa
posx_e1 = 50
posy_e1 = -1500
velocidade_e1 = -12
#Dados Caminhão
posx_e2 = 190
posy_e2 = -500
velocidade_e2 = -10
#Dados Fusca
posx_e3 = 320
posy_e3 = -800
velocidade_e3 = -8

#imagens
fundo = pygame.image.load('Pista.png')
carro_player = pygame.image.load('Carro_Player.png')
carro_enemy1 = pygame.image.load('Carro rosa.png')
carro_enemy2 = pygame.image.load('Caminhao.png')
carro_enemy3 = pygame.image.load('Fusca.png')
fimdejogo = pygame.image.load('Fim.png')

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Corrida Marota')
#Tempo str
fonte = pygame.font.SysFont('arial black', 20)
texto = fonte.render('Tempo: '+str(segundos), True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (59, 30)


janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            janela_aberta = False
    #Comandos Player
    comandos = pygame.key.get_pressed()
    #if comandos[pygame.K_UP]:
       # y -= velocidade
    #if comandos[pygame.K_DOWN]:
       # y += velocidade
    if comandos[pygame.K_LEFT] and x >= 1:
        x -= velocidade
    if comandos[pygame.K_RIGHT] and x <= 360:
        x += velocidade


    #Colisão
    if x - 80 < posx_e1 and y - 180 < posy_e1:
        fim = 1
        cont = 0
        while fim == 1:
            pygame.display.update()
            janela.blit(fimdejogo, (50, 0))
            cont += 1
            sleep(1)
            if cont == 5:
                pygame.quit()
    if x + 80 > posx_e3 and y - 150 < posy_e3:
        fim = 1
        cont = 0
        while fim == 1:
            pygame.display.update()
            janela.blit(fimdejogo, (50, 0))
            cont += 1
            sleep(1)
            if cont == 5:
                pygame.quit()
    if x - 75 < posx_e2 and y - 240 < posy_e2 and x + 75 > posx_e2 and y - 240 < posy_e2:
        fim = 1
        cont = 0
        while fim == 1:
            pygame.display.update()
            janela.blit(fimdejogo, (50, 0))
            cont += 1
            sleep(1)
            if cont == 5:
                pygame.quit()


    #Movimento Inimigos
    #Carro Rosa
    if posy_e1 >= 340:
        posy_e1 = randint(700, 3500) * -1
    posy_e1 -= velocidade_e1
    #Caminhão
    if posy_e2 >= 420:
        posy_e2 = randint(400,4000) * -1
    posy_e2 -= velocidade_e2
    #Fusca
    if posy_e3 >= 310:
        posy_e3 = randint(900, 4500) * -1
    posy_e3 -= velocidade_e3
    #Tempo
    if timer < 15:
        timer += 1
    else:
        segundos += 1
        texto = fonte.render('Tempo: '+str(segundos), True, (255, 255, 255), (0, 0, 0))
        timer = 0
    if segundos % 10 == 0 and segundos != 0:
        velocidade_e1 -= 0.4
        velocidade_e2 -= 0.4
        velocidade_e3 -= 0.4
        velocidade += 0.1
    #Imagens Carros
    janela.blit(fundo, (0, 0))
    janela.blit(carro_player, (x, y))
    janela.blit(carro_enemy1, (posx_e1, posy_e1))
    janela.blit(carro_enemy2, (posx_e2, posy_e2))
    janela.blit(carro_enemy3, (posx_e3, posy_e3))
    janela.blit(texto, pos_texto)


    pygame.display.update()
pygame.quit()