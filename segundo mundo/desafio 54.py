totma = 0
totme = 0
for c in range(1 , 8):
    id = int(input('{}{} idade:'.format(c, 'º')))
    if id >=18:
        totma +=1
    else:
        totme +=1
print('Ao todo tivemos {} pessoas maior de idade'.format(totma))
print('E ao todo tivemos {} pessoas menor de idade'.format(totme))


