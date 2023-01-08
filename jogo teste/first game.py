import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()
l = 720
a = 720
xplayer = 40
yplayer = a / 2
xbot = randint(40, 650)
ybot = randint(40, 650)
tela = pygame.display.set_mode((l, a))
pygame.display.set_caption("Colidir com a mãe do joão")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    player = pygame.draw.rect(tela, (95, 4, 4), (xplayer, yplayer, 10, 10))
    bot = pygame.draw.circle(tela, (48, 164, 125), (xbot, ybot), 45)

    pygame.display.update()