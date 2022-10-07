# identifique numeros primos 
n = int(input('Informe um número:'))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[34m  O numero {n} foi divisivel {total} vezes')
if total == 2:
    print('\033[32mEle é primo')
else:
    print('Ele nao é primo')