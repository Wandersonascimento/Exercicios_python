# Escreva um programa que leia dois numeros e compare mostrando na tela a mensagem, qual valor é maior ou igual:

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor '))
if  valor1 > valor2:
    print('O primeiro valor é maior que o segundo valor.')
elif valor2 > valor1:
    print('O segundo valor é maior que o primeiro valor.')
else:
    print('Os valores são iguais')
