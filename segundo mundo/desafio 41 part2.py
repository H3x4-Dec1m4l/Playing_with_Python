from datetime import date
atual = date.today().year
nas = int(input('Ano de nascimento '))
idade = atual - nas
print('O atleta tem {} anos'.format(idade))
if idade <=9:
    print('Classificação : MIRIM')
elif idade <=14:
    print('Clasificalção: INFANTL')
elif idade <=19:
    print('Clasificação: Junior')
elif idade < 25:
    print('Classificação: SÊNIOR')
else:
    print('Clasificação: MASTER')