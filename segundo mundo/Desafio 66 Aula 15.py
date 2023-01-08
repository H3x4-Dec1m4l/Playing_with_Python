'''Feito 98% por mim'''
n = 0
s = 0
count = 0
while True:

    n = int(input('Digite um Número(999 para parar)'))
    if n == 999:
        break
    s += n
    count += 1
print(f'A soma dos {count} Numeros é de {s}')