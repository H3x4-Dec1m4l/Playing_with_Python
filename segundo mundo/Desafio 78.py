num = list()
mai = men = 0
for c in range(0,5):
    num.append(int(input(f'Digite o numero da pocição {c}: ')))
    if c == 0:
        mai = men = num[c]
    else:
        if num[c] > mai:
            mai = num[c]
        if num[c] < men:
            men = num[c]
print(num)
print(f'O maior valor digitado foi {mai} nas posições')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}...', end = ' ')
print(f'O menor valor digitado foi {men} nas posições')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}...', end= ' ')