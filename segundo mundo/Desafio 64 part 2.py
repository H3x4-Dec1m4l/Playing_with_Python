'''Resolvido pelo Guanabara''' #Aula 15 vai ter uma melhor solução
n = c = s = 0
n = int(input('Digite um número: '))
while n != 999:

    s += n
    c += 1
    n = int(input('Digite um número: '))
print('O total de números digitados é {}, e a soma entre eles é de {}'.format(c, s))