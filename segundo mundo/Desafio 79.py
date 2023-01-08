num = list()
while True:
    n = (int(input('Digite o Número: ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor Duplicado, não pode')
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar, Sim ou Não? ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Os valores adicionados foram {sorted(num)}')