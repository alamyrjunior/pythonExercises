from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('idade:', idade)
if idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda vai se alistar, faltam {} anos para seu alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18:
    print('Está na hora de se alistar')
else:
    saldo = idade - 18
    ano = atual - saldo
    print('Já passaram {} anos de quando você deveria se alistar'.format(saldo))
    print('Seu alistamento foi em {}.'.format(ano))
