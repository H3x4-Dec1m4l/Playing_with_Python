from random import randint
from time import sleep
print('Escolha uma opção!')
op = int (input('''[1] Pedra 
 [2] Papel 
 [3] Tesoura
 Qual a sua jogada?!'''))
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(1)
print('POH!!')
sleep(0.5)
if op > 3:
    print('Opção inválida meu cidadão')
com = randint(1, 3)
if op == 1 and com == 2:
    print('Eu escolhi Papel')
    print('Você perdeu! hahahaha')
elif op == 1 and com == 1:
    print('eu também escolhi pedra')
    print('Empatamos')
elif op == 1 and com == 3:
    print('Eu escolhi tesoura')
    print('Você ganhou! boua soldado(a)')
elif op == 2 and com == 1:
    print('Escolhi Pedra')
    print('Você ganhou!')
elif op == 2 and com == 2:
    print('Eu também escolhi Papel')
    print('Empatamos!')
elif op == 2 and com == 3:
     print('Escolhi Tesoura')
     print("você perdeu meu parceiro!")
elif op == 3 and com == 1:
    print('Escolhi Pedra')
    print('Eu ganhei, e tu perdeste hahaha')
elif op == 3 and com == 2:
    print('Escolhi Papel')
    print('Você ganhou! me parece que está me roubando meu chará')
elif op == 3 and com == 3:
     print('Eu também escolhi tesoura')
     print('empatamos')


