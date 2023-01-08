p = float(input('Qual o seu peso? '))
al = float(input('Qual a sua altura? (em metros) '))
imc = p / (al ** 2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está a baixo do peso! favor ganhar mais massa corporal')
elif imc >=18.5 and imc <= 24.9:
    print('está no peso ideal!')
elif imc >= 25 and imc <= 29.9:
    print('Você está com sobre peso')
elif imc >=30 and imc <=39.9:
    print('Você está com obesidade!')
elif imc >= 40:
    print('Você logo logo se tornará um planeta, cuidado!')

