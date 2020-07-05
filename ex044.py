print('{:=^40}'.format(' Lojas Andrade '))
preco = float(input('Digite o preço do produto: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA - DINHEIRO OU CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opcao = int(input('Qual a forma de pagamento? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif  opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2 vezes de {:.2f} reais.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {} vezes  de {:.2f} reais.'.format(totparc, parcela))
else:
    total = preco
    print('Opção inválida de pagamento, tente novamente!')
print('Sua compra de {:.2f} reais vai custar {:.2f} reais no final.'.format(preco, total))


