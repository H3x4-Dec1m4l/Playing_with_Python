np = 0
pre = 0
mdemil = 0
menor = count = 0
barato = ' '
s = 0
while True:
    np = str(input('Nome Do Produto: '))
    pre = float(input('Preço do produto R$: '))
    op = ' '


    while op not in 'NS':
        op = str(input('Quer continuar? Sim ou Não? S/N: ')).strip().upper()[0]
    s += pre
    count += 1
    if count == 1:
        menor = pre
        barato = np
    else:
        if pre < menor:
            menor = pre
            barato = np

    if pre >1000:
        mdemil +=1
    if op == 'N':
        break
print(f'O preço total é de {s}')
print(f'tem {mdemil} protudos custando mais de R$ 1,000,00 ')
print(f'O produto mais barato foi {barato} que custa {menor}')