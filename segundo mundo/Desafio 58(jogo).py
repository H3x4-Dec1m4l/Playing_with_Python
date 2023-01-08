'''Solucionado por mim'''
from random import randint
com = randint(0, 10)
player = 0
while player != com:
    player = int(input('Qual Número o Computador pensou? '))
    if player != com:
        print('Tente novamente!')
    else:
        print('Você acertouuu seu fila da puta')

