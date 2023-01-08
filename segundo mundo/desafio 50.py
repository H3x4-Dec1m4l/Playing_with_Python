soma = 0
count = 0
for c in range(1, 7):
    num = int(input('Digite o {}{} um valor: '.format(c, 'º')))
    if num % 2 ==0:
        soma += num
        count += 1
print('Dos numeros que você escolheu, {} são pares e a soma deles é {}'.format(count, soma))