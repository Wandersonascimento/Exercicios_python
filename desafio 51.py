
termo = int(input('Infome um numero: '))
razao = int(input('informe a razao: '))
dec = termo + (10 - 1) * razao
for c in range (termo, dec + razao, razao):
    print(c, end=(' → '))
print('Acabou')

