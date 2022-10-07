"""Fala um progrtama que leia o comprimento do cateto adjacente de um triangolo retango, e calcule
e mostre o comprimento da hipotenusa."""
import math

print('Deafio 017\n')
co = float(input('Cateto oposto:'))
ca = float(input('Cateto adjacente: '))
"""hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format((hi)))"""
hi =math.hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))

