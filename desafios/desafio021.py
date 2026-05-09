nome = input('Digite seu nome completo: ')

maiuscula = nome.upper()
print(maiuscula)
minuscula = nome.lower()
print(minuscula)

print('A quantidade de indices no seu nome é: {}.'.format(len(nome)))

separado = nome.split()
print('Seu primeiro nome tem {} indices.'.format(len(separado[0])))