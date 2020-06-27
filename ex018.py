import math
ang = int(input('Digite o angulo que você deseja: '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('Para o angulo de {}° temos:\nSeno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(ang, sin, cos, tan))
