from datetime import date
data = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    nasc = int(input('Digite o ano do seu nascimento: '))
    if data - nasc < 21:
        menor += 1
    else:
        maior += 1
print('{} pessoas são maiores de idade'.format(maior))
print('{} pessoas são menores de idade.'.format(menor))
