a = float(input('Digite o valor da reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    if a == b and a == c:
        print('Você tem um triângulo EQUILÁTERO')
    elif (a == b and a != c) or (a == c and a != b):
        print('Você tem um triângolo ISÓSCELES')
    else:
        print('Você tem um triângulo ESCALENO')
else:
    print('Você não tem um triângulo')
