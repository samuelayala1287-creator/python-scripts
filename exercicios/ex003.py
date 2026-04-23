# Declaração das Variávei:
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

# Estrutura Condicional:
if idade >= 18:
    print('Olá {}, como você tem {} anos, então é considerado maior de idade.'.format(nome, idade))
else:
    print('Olá {}, como você só tem {} anos, então é considerado menor de idade.'.format(nome, idade))