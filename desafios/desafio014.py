import math
oposto = float(input('Qual o comprimento do cateto oposto? '))
adjacente = float(input('Qual o comprimento do cateto adjacente? '))

hipotenusa = math.hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}m'.format(hipotenusa))