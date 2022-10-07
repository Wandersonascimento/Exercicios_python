#Escreva um programa para aprovar um emprestimo bancario.
#valor da casa, o salario e em quantos anos ele vai pagar.
#o valor da prestação nao pode ser maior que 30% do salario.

emprestimo = float(input('informe o valor do emprestimo: '))
tempo = int(input('Informe a quantidade de parcelas: '))
salario = float(input('Informe o salario:'))

parcela = emprestimo / tempo
print(f'O valor da parcela é R${parcela:.2f}')
print(f'30% do salario corresponde R${salario/100*30:.2f}')
if parcela > (salario/100*30):
    print('O valor da parcela e superior a 30% do salario. \033[1;31mO emprestimo não foi aprovado.\033[m')
else:
    print('\033[1;32mO Emprestimo está aprovado')