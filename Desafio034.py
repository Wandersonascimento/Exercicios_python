#escreva um programa que pergunte o salario de um funcionario e calcule o seu almento:
#para salkarios superiores a a 1250,00 aumentos de 10%
#para salarios inferiores, aumento de 15%.
print('Desafio 034\n')
salario = int(input('Informe o salario: R$'))
print(f'O salário informado foi R${salario:.2f}')
if salario > 1250:
    print(f'O salario teve aumento de 10%. Salario agora é: R${salario+((salario/100)*10):.2f}')
else:
    print(f'O salario teve aumento de 15%. Salario agora é: R${salario+((salario/100)*15):.2f}')
