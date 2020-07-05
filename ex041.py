print('Cofederação Nacional de Natação')
nasc = int(input('Digite a sua data de nascimento: '))
idade = 2020 - nasc
categoria = ''
if idade < 10:
    categoria = 'Mirim'
elif idade < 15:
    categoria = 'Infantil'
elif idade < 20:
    categoria = 'Junior'
elif idade == 20:
    categoria = 'Sênior'
else:
    categoria = "Master"

print('Você tem {} anos'.format(idade))
print('Você está na categoria', categoria)
