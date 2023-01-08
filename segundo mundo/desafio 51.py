p = int (input('Primeiro termo'))
r = int (input('Razão'))
de = (10 -1) * r
for c in range(p, de + r, r):
    print('{}'.format(c), end='->')