frase = str(input('Digite uma Frase: ')).strip().upper()
pa = frase.split()
junto = ''.join(pa)
inverso = ''
for le in range(len(junto) -1, -1, -1):
    inverso += junto[le]
print('{}'.format(inverso))
if inverso == junto:
    print('Essa palavra é um Palindromo')

