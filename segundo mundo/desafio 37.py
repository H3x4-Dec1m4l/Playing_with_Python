n1 = int (input('digite um número: '))
print('''escolha uma das opções das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
op = int(input('sua opção '))
if op == 1:
    print('{} convertido em BINÁRIO é igual a {}'.format(n1, bin(n1)[2:]))
elif op == 2:
    print('{} convertido para OCTAL  é igual a {}'.format(n1, oct(n1)[2:]))
elif op == 3:
    print('{} convertido em HEXADECIMAL é igual a {}'.format(n1, hex(n1)[2:]))
else:
    print('opção inválida')
