cs = float(input('valor da casa?'))
salario = float(input('Seu salário '))
par = int(input('em quantos anos pretende pagar? '))
pres = cs / (par * 12)
mi = salario *30 / 100

print('para pagar a casa de {} em {} anos a prestação é de {:.2f} '.format(cs, par, pres))
if pres > mi:
    print('Enpréstimo negado'
if  
else:
    print('Emprestimo aceito!')