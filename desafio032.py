#criar um programa que leia um ano bisexto e mostre se ele é ou nao bissexto.
print('Desafio 032\n')
from datetime import date
ano = int(input('Informe um ano com 04 digitos: '))
ano1 = ano %4
#print(ano1)
if ano1 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano}, é um ano bissexto.')
else:
    print(f'O ano de {ano}, não é um ano bissexto.')
print(f'O noso Ano atual é {date.today().year} se passaram {date.today().year - ano}')
