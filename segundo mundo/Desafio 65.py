'''Tentado por mim'''
n = 0
op = 0
count = 0

while op != 'N':
    count += 1

    n = int(input('Digite um Número: '))
    op = str(input('Quer continuar? S/N?')).upper()
    m = (n + n)/ count
print('A média dos números digitados é de {}'.format(m))
print(count)

