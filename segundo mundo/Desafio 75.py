n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Os valores digitados foi {n}')
print(f'Quantidade de vezes que aparece o número 9: {n.count(9)}')
if 3 in n:
    print(f'O número 3 aparece na  {n.index(3)+ 1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os numeros pares foram', end= ' ')
for c in n:
    if c % 2 == 0:
        print(c,',', end= ' ')
