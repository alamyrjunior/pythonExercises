s = 0
count = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        count += 1
print('A soma dos {} números pares digitados é igual a {}'.format(count, s))
