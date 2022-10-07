#criar um programa que leia quantos dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar:
#dollar us$ 3,27
print('Desafio 010\n')
m = ' Seja bem vindo conversor de dolar '
mf = ' Final de Programa '
print('{:*^60}\n'.format(m))
real = float(input('Informe quantos reais voce tem para compra de Dollar: R$ '))
dollar = 3.27
compra = real/dollar
print('\nCom R${:.2f} , voce pode comprar US${:.2f} .'.format(real, compra))
print('\n{:*^60}'.format(mf))



