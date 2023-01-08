from random import randint
com = (randint(0, 10), randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
for c in com:

    print(c , end= ' ')
print(f'\n o maior valor sorteado foi {max(com)}')
print(f'o menor numero sorteado foi {min(com)}')


