saldo = float(input('Qual o saldo da sua conta? R$'))
saque = float(input('Quanto você deseja sacar? R$'))

if saldo >= saque:
    print('Saque realizado com sucesso!')
    print('Seu novo saldo é de R${:.2f}'.format(saldo + saque))
else:
    print('Saldo insuficiente. Operação cancelada.')
    print('Seu saldo atual é de R${:.2f}'.format(saldo))