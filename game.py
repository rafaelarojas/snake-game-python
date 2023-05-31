import pygame, random #importa a biblioteca de jogos do python
from pygame.locals import *

def on_grid(): #função que gera posição aleatória dentro do grid para o block
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init() #inicializa a biblioteca pygame
screen = pygame.display.set_mode((600,600)) #tela do jogo
pygame.display.set_caption('Snake')

snake = [(200,200), (210,200), (220,200)] #uma lista contida por tuplas que representam partes da cobra
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

s_block = on_grid() #posição aleatória para o bloco
block = pygame.Surface((10,10))
block.fill((104,190,255))

direction = LEFT
time = pygame.time.Clock() #limita o fps

while True:
    time.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT: #evento de fechar
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direction = UP
            if event.key == K_DOWN:
                direction = DOWN
            if event.key == K_RIGHT:
                direction = RIGHT
            if event.key == K_LEFT:
                direction = LEFT

    if collision(snake[0], s_block):
        s_block = on_grid()
        snake.append((0, 0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    #mudanças de posição do inicio da cobra
    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1] - 10)


    screen.fill((0,0,0,)) #para limpar a tela
    screen.blit(block, s_block)
    for pos in snake: #para cada posição
        screen.blit(snake_skin,pos)
        pygame.display.update()