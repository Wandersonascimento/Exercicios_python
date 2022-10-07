# criar um programa que leia um angulo qualquer e informe o valkor do seno consseno e tangente

import math

print('Deafio 018\n')
print('{:*^50}\n'.format(' Seja bem vindo '))
angulo = int(input('Informe um angulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O seno de {} é: {:.2f}'.format(angulo, seno))
print('O Cosseno de {}, é: {:.2f}'.format( angulo, cos))
print('A tengente de {} é: {:.2f}'.format(angulo, tan))
print('-'*50)
print('{:*^50}'.format(' Final de programa '))









