#criar um programa que leia uma temperatura em Graus Cº e convereta para fahrenheint.
#formula e : ºF = ºC X 1,8 + 32
print('Desafio 014\n')
print('{:*^50}'.format(' Bem Vindo '))
celsius = float(input('Informe a temperatura em ºC: '))
f = (celsius * 1.8) + 32
print(' A temperatura informada foi de {:.1f}ºC,\n A temperatura em Fahrenheit é {:.1f}ºF .'.format(celsius, f))
print('\n{:*^50}'.format(' Final de programa '))
