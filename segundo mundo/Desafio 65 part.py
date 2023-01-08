'''Feito pelo Guanabara''' '''(consegui resolver sozinho o bug da linha 12, que 
quando ia digitar os numeros na hora de ver o menor e o maior o programa não lia o primeiro numero 
caso ele fosse o menor. Além de usar o if count == 1, passei o valor '1'para 0 '''
resp = 'S'
s = 0
count = 0
m = 0
ma = 0
me = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    if count == 0:
        ma = me = n
    else:
        if n > ma:
            ma = n
        elif n < me:
            me = n

    resp = str(input('Quer continuar S/N?')).upper().strip()[0]

    s += n
    count += 1
m = s / count
print('A quantidade de números digitados foi de {}, e a média é de {}'.format(count, m))
print('o maior número foi {} e o menor foi {}'.format(ma, me))