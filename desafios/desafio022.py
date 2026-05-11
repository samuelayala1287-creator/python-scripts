# Formarto de String:
numero = input('Digite um número com 4 dígitos:')

print('Unidade: {}'.format(numero[3]))
print('Dezena: {}'.format(numero[2]))
print('Centena: {}'.format(numero[1]))
print('Milhar: {}'.format(numero[0]))

# Formato Numerico:
n = int(input('Digite um número com 4 dígitos: '))
print('Unidade: {}'.format(n % 10))
print('Dezena: {}'.format((n // 10) % 10))
print('Centena: {}'.format((n // 100) % 10))
print('Milhar: {}'.format((n // 1000) % 10))