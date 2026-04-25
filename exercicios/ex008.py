paes = int(input('Quantos pães você quer comprar? '))

if paes >= 10:
    print('Vai ficar por R${:.2f}'.format(paes*0.8))
else:
    print('Vai ficar por R${:.2f}'.format(paes))