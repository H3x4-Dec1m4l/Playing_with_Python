id = int(input('Digite sua idade '))
print('Sua idade é {}'.format(id))
if id <=9:
    print('Você será nadador mirim')
elif id > 9  and id <=14:
    print('Você será nadador infantil')
elif id >14 and id <= 19:
    print('você será um nadador júnior')
elif id == 20:
    print('Você será um nadador sênior')
else:
    print('você será um nadador master')
