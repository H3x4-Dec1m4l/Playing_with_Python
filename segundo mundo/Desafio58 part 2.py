'''Feito pelo Guanabara'''
from random import randint
com = randint(0 , 10)
palpite = 0
print('Pensei em um número, tente adivinhar qual numero eu pensei')
acerto = False
while not acerto:
    player = int(input('Qual número eu pensei?'))
    palpite += 1
    if com == player:
        acerto = True
    else:
        if player < com:
            print('Mais... tente novamente!')
        elif player > com:
            print('Menos... tente novamente') 
print('Parabéns')
print('Você precisou de {} palpites para acertar!'.format(palpite))