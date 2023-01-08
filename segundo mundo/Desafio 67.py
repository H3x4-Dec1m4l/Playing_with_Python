s = 0


while True:
    print('-'*30)
    n = int(input('Digite o numero pra saber sua tabuada '))
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-'*30)
    if n == 0:
        break



