from datetime import date
id = int(input('Digite sua data de nascimento: '))
atual =  date.today().year
s = atual - id
if s < 18:
    saldo = 18 - s
    print('Você ainda não Precisa se alistar para ir ao exercito')
    print('ainda falta {} anos para o seu alistamento'.format(saldo))
elif s == 18:
    print('voce presisa se alistar ao exercito!')
elif s >18:
    saldo = s - 18
    print('já se passaram {} anos para seu alistamento'.format(saldo))
    print('Se voce não se alistou ao exército precisa se alistar imediatamente')
    print('se voce já se alistou fique tranquilo!')