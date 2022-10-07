#criar um programa que leia salario e aplique um aumento de 15%
print('Desafio 013\n')
print('{:*^60}\n'.format(' Seja bem vindo '))
salario = float(input('Informe o salario: R$ '))
percente = float(input('Informe o aumento: '))
calc = (salario / 100) * percente
print('O novo salario com aumento de {}%, e de R${:.2f}'.format(percente, calc + salario))
print('-'*60)
print('{:*^60}'.format(' Final de programa '))
