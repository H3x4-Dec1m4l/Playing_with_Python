r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Valor da segunda reta: '))
r3 = float(input('terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os seguimentos a cima podem formar um triangulo')
else:
    print('não formam um triangulo')