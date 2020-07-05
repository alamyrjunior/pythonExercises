nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media < 5.0:
    print('Sua média foi {:.1f}, infelizmente você está REPROVADO.'.format(media))
elif media < 7:
    print('Sua média foi {:.1f}, você está de RECUPERAÇÃO'.format(media))
else:
    print('Parabéns! Sua média foi {:.1f}, você foi APROVADO!'.format(media))
