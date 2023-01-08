'''Solucionado em partes por mim'''
op = 0
for c in range(1, 3):
    n1 = int(input('{}º valor'.format(c)))
while op != 5:

    op = int (input('''O que você deseja fazer com esses valores?
    [1]somar
    [2]Multiplicar
    [3]saber qual numero é maior
    [4] novos números
    [5]finalizar o programa'''))
    if op == 1:
        soma = n1 + n1
        print('a soma desses números é de {}'.format(soma))
    elif op == 2:
        mul = n1 * n1
        print('{}x{} é igual á {}'.format(n1, n1, mul))
    elif op == 3:
        maior = n1