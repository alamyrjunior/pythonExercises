print('Será que sua frase é um palindromo?')
a = str(input('Digite sua frase: '))
b = str(a.replace(' ', ''))
r = ""
for c in range(len(b),0,-1):
    r += b[c-1]
if r == b:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palindromo...')


