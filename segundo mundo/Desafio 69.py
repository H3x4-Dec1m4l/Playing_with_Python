tot18 = toth = totm = 0
while True:
    id = int(input('Qual sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu Sexo:? [M/F')).upper().strip()[0]
    if id >=18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and id <20:
        totm += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {tot18} ')
print(f'total de Homens {toth}')
print(f'Total de Mulheres com menos de 20 anos {totm} ')