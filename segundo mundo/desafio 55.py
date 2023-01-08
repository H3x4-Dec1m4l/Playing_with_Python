totlev = 0
totpes = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa'.format(c)))
    if c == 1:
        totpes = peso
        totlev = peso
    else:
        if peso > totpes:
            totpes = peso
        if peso < totlev:
            totlev = peso



print('O mais leve é o de {}Kg'.format(totlev))
print('O mais pesado é o de {}Kg'.format(totpes))
