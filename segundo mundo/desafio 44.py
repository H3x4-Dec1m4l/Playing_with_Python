print('{:=^40}'.format('LOJA HP'))
com = float(input('Valor das compras: '))
op = float(input('''Formas de pagamento
[ 1 ] à vista dinheiro/Débito
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
qual é a opção?'''))
avistad = (com * 10)/ 100
avistac = (com * 5) / 100
juros = (com * 20/ 100)
if op == 1:
    print('O pagamento vai ser de {:.2f}R$'. format(com - avistad))
    print('com desconto de 10%, que são {:.2f}R$ de desconto'.format(avistad))
elif op == 2:
    print('O pagamento vai ser de {:.2f}R$'.format(com - avistac))
    print('Com desconto de 5%, que são {:.2f}R$ de desconto'.format(avistac))
elif op == 3:
    par = com / 2
    print('O pagamento será o mesmo valor de {:.2f}R$, não tendo\n nenhum valor de desconto e de juros na conta final!'.format(com))
    print('as parcelas serão de 2x de {:.2f}R$'.format(par))
elif op == 4:
    par = int (input('Total de parcelas : '))
    s = (com + juros) / par
    print('O pagamento será de {:.2f}R$'.format(com + juros ))
    print('O juros será de 20%, e será adicionado mais {:.2f}R$ no valor final'.format(juros))
    print('Com as parcelas sendo de {:.2f}R$'.format(s))




