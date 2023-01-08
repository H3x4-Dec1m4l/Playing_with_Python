lis = 'lápis', 1.50,\
      'Caderno', 15.80, \
      'Caneta', 9.000, \
      'borracha', 2.00, \
      'Régua', 5.75
print('listagem de preços')
for i in range(0, len(lis)):
    if i % 2 == 0:
        print(f'{lis[i]:.<30}',end='')
    else:
        print(f'{lis[i]:>7.2f}')
