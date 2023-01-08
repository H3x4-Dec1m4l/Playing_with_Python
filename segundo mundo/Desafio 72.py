n = ('zero', 'um', 'Dois', 'Três', 'quatro', 'Cinco', 'Seis', 'sete', 'oito', 'nove', 'dez')
while True:
    resp = int(input('Digite um número entre 0 e 10 para ver escrito por extenso '))
    if 0<= resp <= 10:
        break
    print('TENTE NOVAMENTE', end= ' ')
print(f'voce digitou o número {n [resp]}')
