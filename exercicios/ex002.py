palavra = 'Programador'
print(type(palavra))
print(palavra.isspace())
print(palavra.isnumeric())
print(palavra.isalpha())
print(palavra.isalnum())
print(palavra.isupper())
print(palavra.islower())
print(palavra.istitle())
raiz = int(81**(1/2))
print(raiz)

nome = input('Digite seu nome:')
print('Prazer em te conhecer {:^20}'.format(nome))