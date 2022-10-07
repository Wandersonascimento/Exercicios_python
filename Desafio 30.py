#criar um programa que leia u, numero inteiro e mostre se ele e par ou impar.
print('Desafio 30\n')
num = int(input('Informe um número: '))
res = num % 2
if res == 1:
    print(f'O numero {num} é um numero impar.')
else:
    print(f'O numero {num} é um numero par.')