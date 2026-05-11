nome = 'Samuel Ayala Marques Brito'

print('Seu nome em maiúsculo: {}.'.format(nome.upper()))
print('Seu nome em minúsculo: {}.'.format(nome.lower()))

print('A quantidade de indices no seu nome é {}.'.format(len(nome)))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))

separado = nome.split()
print('Seu primeiro nome tem {} indices.'.format(len(separado[0])))