print('O programa vai dizer qual é o maior e qual é o menor peso')
pesomin = 9999
pesomax = 0
for c in range(0,5):

    peso = float(input('Digite o peso da {}ª pessoa: '.format(c+1)))
    if peso < 9999 and peso > 0:
        if peso > pesomax:
            pesomax = peso
        if peso < pesomin:
            pesomin = peso
    else:
        print('Peso inválido! Digite um peso entre 0 e 9999.')

print('O maior peso da lista é {} kg'.format(pesomax))
print('O menor peso da lista é {} kg'.format(pesomin))



