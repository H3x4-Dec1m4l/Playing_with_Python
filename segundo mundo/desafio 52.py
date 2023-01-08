n1 = int (input('Digite o numero: '))
tot = 0
for c in range(1, n1 + 1):
    if n1 % c ==0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m O numero {} foi dividido {} vezes'.format(n1, tot), end=' ')
if tot == 2:
    print('E por isso ele é número primo!')
else:
    print('Ele foi dividido mais que 2 vezes, então por isso ele não é número primo')