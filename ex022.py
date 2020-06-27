nome = str(input('Digite seu nome completo: '))
up = nome.upper()
low = nome.lower()
l = nome.replace(" ", "").__len__()
s = nome.split()
print('O seu nome completo é {}\nEm maiúsculas: {}\nEm minúsculas:{}\nContém {} letras.\nSeu primeiro nome é: {} e tem {} letras.'.format(nome, up, low, l, s[0],len(s[0])))


