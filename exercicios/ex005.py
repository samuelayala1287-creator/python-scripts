media = float(input('Qual foi a sua média no último semestre? '))

if media < 7:
    print('Reprovado!')
elif media < 9.5:
    print('Aprovado!')
else:
    print('Aprovadíssimo!')