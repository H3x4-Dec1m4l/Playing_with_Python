print('Banco PNC')

saque = int(input('Qual o valor que deseja sacar? R$: '))
tot = saque
ced = 50
totced = 0
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cédulas foi de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if tot == 0:
            break


