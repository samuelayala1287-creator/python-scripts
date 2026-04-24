# Primeiro definimos quais funções da biblioteca math vamos usar
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))

# Depois usamos a função radians() para converter graus centigrados em rdiandos.
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

# E por fim fazemos o print() sem utilizar o termo math.
print('O ângulo de {}° tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}.'.format(angulo, seno, cosseno, tangente))