n = ('zero', 'um', 'Dois', 'Três', 'quatro', 'Cinco', 'Seis', 'sete', 'oito', 'nove', 'dez')
while True:
    resp = int(input('Digite um número entre 0 e 10 para ver escrito por extenso '))
    if 0 <= resp <= 10:
        print(f'voce digitou o número "{n [resp]}" ')
    op = ' '
    while op  not in 'SN':
        op = str(input('Quer Continuar Sim ou Não? S/N: ')).strip().upper()[0]
    if op == 'N':
        break
print('Acabou')



