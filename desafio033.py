#faça um programa que leia tres números e mostre qual deles é o maior e qual é o menor:
print('Desafio 033\n')
a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')
