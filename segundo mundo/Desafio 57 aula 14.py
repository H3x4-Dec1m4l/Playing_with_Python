'''Desafio Solucionado por mim'''
r = 0
while r != 'M' and r != 'F':
    r = str(input('Qual seu sexo?'))
    if r != 'M' and r != 'F':
        print('Tente novamete com uma resposta válida!\n Somente as letras M e F (em maiúsculas) são válidas')
    elif r == 'M' and r == 'F':
        print('Uau')
