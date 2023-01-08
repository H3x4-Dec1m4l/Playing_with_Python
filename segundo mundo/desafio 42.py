r1 = float (input('Primeiro Segmento: '))
r2 = float (input('Segundo segment: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3  and r3 < r1 + r2:
    print('Os segmentos a cima podem formar um triângulo', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1!= r2 !=r3 !=r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('os seguimentos não podem formar um triângulo')