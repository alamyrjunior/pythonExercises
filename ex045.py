from random import randint
from time import sleep
print('Jokenpython')
print('Escolha entre pedra, papel e tesoura.')

itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!!')
sleep(0.7)
print('-='*15)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-='*15)
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCEU')

    elif jogador == 2:
        print('COMPUTADOR VENCEU')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR VENCEU')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')

    elif jogador == 1:
        print('COMPUTADOR VENCEU')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('JOGADA INVÁLIDA!')
