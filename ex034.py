sal = float(input('Escreva o sálario de um funcionário: '))
aumento = ""
if sal < 1250.00:
    aumento = sal*0.15
else:
    aumento = sal*0.10
print('O novo salário é de {} reais.'.format(sal + aumento))
