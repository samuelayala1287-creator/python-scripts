idade = int(input('Qual sua idade? '))
if idade <= 12:
    print('criança')
elif idade < 18:
    print('adolecente')
elif idade < 60:
    print('adulto')
else:
    print('idoso')