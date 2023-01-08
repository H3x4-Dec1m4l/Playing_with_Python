n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite uma nota: '))
n3 = float(input('Digite uma nota: '))
n4 = float(input('Digite uma nota: '))
s = (n1 + n2 + n3 + n4) / 4
print('Sua média foi de {:.1f}'.format(s))
if s < 5.0:
    print('Reprovado seu merda do karalho')
elif s >= 5.0 and s < 7:
    print('Você está de recuperação, que vergonha!')
elif s >= 7.0 and s < 9:
    print('Você passou ')
elif s >= 9.0:
    print('Você é demais garote')