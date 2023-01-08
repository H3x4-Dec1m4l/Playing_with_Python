'''Tentei resolver sozinho'''
count = 0
n = 0
s = 0
print('Digite a quantidade de numeros que desejar\n e digite 999 para parar o programa fechar')
while n != -1:

    count += 1
    s += 1
    n = int(input('Digite o {}° Número'.format(count)))
    n += 1
    if n == -1:
        s = s + n
        print('A soma dos números foi de {}'.format(s))
