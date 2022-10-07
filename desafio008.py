# Criar um programa que leia em metros e exiba o valor convertido em centimetros e milimetros.
print('Desafio 008')
mgi = ' Bem vindo ao conversor de metros '
mgf = ' Final de programa '
print('\n{:*^50}\n'.format(mgi))
mts = float(input('Informe o número de metro(s): '))
cm = mts * 100
mm = mts * 1000
print('Metros informado foi: {} m.\n {} m equivale a {} cm.\n {} m equivale a {} mm.'.format(mts, mts, cm, mts, mm))
print('\n{:*^50}'.format(mgf))
