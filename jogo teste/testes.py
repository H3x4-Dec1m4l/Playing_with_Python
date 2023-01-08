import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()
l = 720
a = 720
xplayer = 40
yplayer = a / 2
xbot = 0
ybot = 0

tela = pygame.display.set_mode((l, a))
pygame.display.set_caption("Colidir com a mãe do joão")
fps = pygame.time.Clock()
while True:
    fps.tick(60)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    player = pygame.draw.rect(tela, (95, 4, 4), (xplayer, yplayer, 10, 10))
    bot = pygame.draw.circle(tela, (48, 164, 125), (xbot, ybot), 45)


    if ybot >= a:
        ybot = 0
    ybot = ybot + 5
    if ybot >= a:
        xbot = randint(0,650)

    pygame.display.update()