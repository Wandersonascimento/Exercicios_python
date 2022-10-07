cont = 0
soma = 0
for c in range(1, 7):
    num = int(input(f'{c} - Informe um numero: '))
    if num % 2 == 0:
        soma += num # simplificando; soma = soma + num...
        cont = cont + 1
print(f'\nO resultado da soma de todos os numeros pares informado é \033[1:34m{soma}')
print(f'Foi informado {cont} numeros pares')
