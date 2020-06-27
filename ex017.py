import math

catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o cateto adjacente: '))
r = math.hypot(catetoOposto, catetoAdjacente)
print('A hipotenusa resultada do cateto oposto {} e do cateto adjacente {} é {:.2f}.'.format(catetoOposto, catetoAdjacente, r))

