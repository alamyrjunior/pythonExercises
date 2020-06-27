lar = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = (alt * lar)

print('A área da parede é {:.2f} m²'.format(area))
print('Você precisa de {:.2f} litros de tinta para pintá-la'.format(area/2))
