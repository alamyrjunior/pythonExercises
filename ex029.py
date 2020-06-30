vel = int(input('Qual a velocidade do carro: '))
if vel > 80:
    multa = (vel - 80)*7
    print('Você foi multado em {} reais'.format(multa))
else:
    print('Está dentro da velocidade')


