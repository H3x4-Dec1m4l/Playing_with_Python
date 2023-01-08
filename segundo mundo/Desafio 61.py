p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
t = p
c = 1
while c <=10:
    t += r
    c += 1
    print('{} ->'.format(t), end= ' ')
print('fim')