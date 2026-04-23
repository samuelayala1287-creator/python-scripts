oposto = float(input('Qual o comprimento dos cateto oposto? '))
adjacente = float(input('Qual o comprimento dos cateto adjacente? '))

hipotenusa = (oposto**2)+(adjacente**2)

print('A hipotenusa vai medir {:.2f}m'.format(hipotenusa**(1/2)))