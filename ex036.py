print('Bem vindo ao serviço de financiamento de casas!')
print('Banco MaisRico - Seu dinheiro nas nossas mãos, com juros!')
salario = float(input('Digite seu salário: '))
anos = float(input('Em quantos anos quer pagar: '))
emprestimo = float(input('Digite o valor do empréstimo que você necessita: '))
parcela = (emprestimo / (anos * 12)) * 1.15

if parcela <= salario * 0.3:
    print('O seu empréstimo foi aceito!\nO valor da sua parcela é de {:.2f} mensais'.format(parcela))
else:
    print('Seu empréstimo foi negado')
