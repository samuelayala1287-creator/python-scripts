qnt = int(input('Digite a quantidade de somas que você deseja somar: '))
soma = 0

i = 1
while i < qnt:
    num1 = int(input('Digite o primeiro número:'))
    num2 = int(input('Digite o segundo número:'))
    i += 1
    soma = num1 + num2

print(soma)