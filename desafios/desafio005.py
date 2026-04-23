dolar = 5.16
euro = 5.94
kwanza = 179.6
dinheiro = float(input('Quantos reais você tem na carteira? R$'))
print('Isso dá: ${:.2f}'.format(dinheiro/dolar))
print('Isso dá: £{:.2f}'.format(dinheiro/euro))
print('Isso dá: Kz{:.2f}'.format(dinheiro*kwanza))