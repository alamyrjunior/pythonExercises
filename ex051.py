from time import sleep
print('Progressão aritmética!')
n1 = int(input('Digite o primeiro termo da sua progressão: '))
r = int(input('Digite a razão da sua progressão: '))

for c in range(n1, r * 10, r):
    print(c)
    sleep(0.4)
for c in range(1, 4):
    print('.')
    sleep(0.4)
