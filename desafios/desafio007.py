produto = float(input('Qual o preço do produto?'))
desc = produto*0.05
print('Durante a promoção de 5%, esse produto vai sair por R${:.2f}'.format(produto-desc))