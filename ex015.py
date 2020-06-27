km = float(input('Quantos quilometros foram percorridos: '))
dias = float(input('Por quantos dias o carro foi alugado: '))
total = (km*0.15)+(dias*60)
print('O total a pagar é R${:.2f}'.format(total))