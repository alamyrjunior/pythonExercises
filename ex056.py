mIdade = 0
fCount = 0
maisVelho = 0
nomeMaisVelho =''
for c in range(0, 4):
    print('----{}ª PESSOA----'.format(c+1))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo(m ou f): ')).strip()
    mIdade += idade
    if c == 1 and sexo in 'Mm':
            maisVelho = idade
            nomeMaisVelho = nome
    if sexo in 'Mm' and  idade > maisVelho:
        maisVelho = idade
        nomeMaisVelho = nome
    elif sexo in 'Ff':
        if idade < 20:
            fCount = fCount + 1


print('O grupo tem {} mulheres com idade abaixo de 20 anos'.format(fCount))
print('A média de idade do grupo é de {} anos' .format(mIdade/4))
print('A idade do homem mais velho é {} anos e ele se chama {}.'.format(maisVelho, nomeMaisVelho))
