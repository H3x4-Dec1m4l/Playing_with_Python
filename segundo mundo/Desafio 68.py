from random import randint
s = 0
v = 0
while True:
    player = int(input('Digite um número '))
    com = randint(1, 10)
    tot = player + com
    op = ' '
    while op not in 'PI':
        op = str(input('Voce escolhe Impar ou Par?')).upper().strip()[0]
    print(f'Você escolheu {player} e o Computador escolheu {com}, total foi de {tot}')
    print('Deu Par' if tot % 2 == 0 else 'Deu impar')
    if op == 'P':
        if tot % 2 == 0:
            print('Jogador venceu')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif op == 'I':
        if tot % 2 == 1:
            print('Você Ganhou!')
            v += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente')
print(f'números de vitórias {v}')

