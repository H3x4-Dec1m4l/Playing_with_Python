n1 = int(input('Digte o Número: '))
c = n1
f = 1
print('calculando o fatorial de {}!: '.format(n1), end=' ')
while c > 0 :
    print('{}'.format(c), end=" ")
    print('x' if c > 1 else '=', end= ' ')
    f *=c
    c -= 1
print('{}'.format(f))
