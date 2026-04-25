# Primeiros coletamos os dados a serem utilizados na estrutura.
idade = int(input('Qual a idade do cliente? '))
dias = input('Qual o dia da semana?')
INTEIRA = 40
MEIA = 20

# Agora, vamos criar a estrutura de decisão utilizando if, elif e else.
if idade <= 12:
    print('O ingresso vai custar R${:.2f} (Meia).'.format(MEIA))
    print('O desconto é aplicado por ser uma criança.')
elif idade >= 60:
    print('O ingresso vai custar R${:.2f} (Meia).'.format(MEIA))
    print('O desconto é aplicado por ser um idoso.')
elif idade >= 13 and idade <= 60 and dias == 'quarta-feira':
    print('O ingresso vai custar R${:.2f} (Meia).'.format(MEIA))
    print('O desconto é aplicado pelo cliente ter entre 13 e 59 anos e ser uma quarta-feira.')
else:
    print('O ingresso vai custar R${:.2f} (Inteira).'.format(INTEIRA))