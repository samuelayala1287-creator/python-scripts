altura = float(input('Qual a sua altura em metros?'))
km = altura * 0.001
hm = altura * 0.01
dam = altura * 0.1
dm = altura * 10
cm = altura * 100
mm = altura * 1000
print('Suas medidas são: {}km, {}hm, {:.2f}dam, {}dm, {}cm e {}mm!'.format(km, hm, dam, dm, cm, mm))