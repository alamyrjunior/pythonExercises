a = float(input('Digite o tamanho de uma reta: '))
b = float(input('Digite o tamanho de outra reta: '))
c = float(input('Digite o tamanho de mais uma reta: '))

if (b - c) < a < b + c and (a-c) < b < a + c and (a-b) < c < a + b:
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')