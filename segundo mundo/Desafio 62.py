
p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
t = p
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        t += r
        c += 1
        print('{} ->'.format(t), end= ' ')
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais:? '))


