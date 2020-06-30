d = float(input('Qual é a distância de sua viagem em km: '))
v = ""
if d <= 200:
    v = d*0.50
else:
    v = d*0.45
print('Sua viagem custa {} reais'.format(v))