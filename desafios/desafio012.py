p1 = float(input('Rodou quantos quilômetros?'))
p2 = int(input('Passou quantos dias com o carro?'))
km = p1*0.15
dias = p2*60

preço = km+dias
print('Considerando a quantidade de dias corridos e quilômetros rodados, você terá que pagar R${:.2f}'.format(preço))