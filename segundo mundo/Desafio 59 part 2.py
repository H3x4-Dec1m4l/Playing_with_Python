'''Feito pelo Guanabara'''
from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
op = 0
while op != 5:
    print('==-==' * 10)
    op = int(input('''O que você deseja fazer com esses valores?
        [1]somar
        [2]Multiplicar
        [3]saber qual numero é maior
        [4] novos números
        [5]finalizar o programa: '''))

    print('==-==' * 10)
    if op == 1:
        s = n1 + n2
        print('A soma entre {} + {} é igual à {}'.format(n1, n2, s))
    elif op == 2:
        m = n1 * n2
        print('A multiplicação entre {}x{} é igual à {}'.format(n1, n2, m))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
    elif op == 4:
        print('Digite novamente os  números')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif op == 5:
        print('Finalizando....')
    else:
        print('Opção inválida, tente novamente!')
    sleep(2)
print('Fim Do programa')
