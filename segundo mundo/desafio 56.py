somaid = 0
médiaid = 0
maioridadem = 0
nvelho = ''
totmulher = 0

for p in range(1,5):
    print('---------{}ª---------'.format(p))
    nome = str(input('Nome:')).strip()
    id = int(input('Idade: '))
    sex = str(input('Sexo: [M/F]')).strip()
    somaid += id
    if p == 1 and sex in 'Mm':

        maioridadem += id
        nvelho = nome
        if sex in 'Mm' and id> maioridadem:
            maioridadem = id
            nvelho = nome
        if sex in 'Ff' and id < 20:
            totmulher += 1
médiaid = somaid/4
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadem, nvelho))
print('a média de idade do grupo é de {} anos'.format(médiaid))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))