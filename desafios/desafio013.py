# Primeiro importar a função trunc() da biblioteca math
from math import trunc

# Depois digitar a sintaxe, não precisa usar math
numero = float(input('Digite um valor: '))
print('O número digitado foi {}, e sua parte inteira é {}.'.format(numero,trunc(numero)))