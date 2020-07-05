print('App: Saiba seu IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso/(altura*altura)
r =""
if imc < 18.5:
    r = 'abaixo do peso'
elif imc <=25:
    r = 'com o peso ideal'
elif imc <= 30:
    r = 'com sobrepeso'
elif imc <= 40:
    r = 'com obesidade'
else:
    r = 'com obesidade mórbida'

print('O seu IMC é de {:.2f} e você está {}.'.format(imc,r))


