#criar um programa que leia um numeros de 0 a 9999 e mostre:
# unidade/ dezena/ centena/ milhar
print('Desafio 023\n')
print('{:*^50}\n'.format(' Seja bem vindo '))
numero = int(input('Informe um número entre 0 e 9999: '))
und = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print(f'A Unidade é: {und}')
print(f'A Dezena é: {dez}')
print(f'A Centena é: {cen}')
print(f'A milhar é: {mil}')
print('-'*20)

print('{:*^50}'.format(' Final de Programa '))
