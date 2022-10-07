print('Inforne qual tabuada deseja:')
n = int(input('Informe qual a tabuada:'))
f = int(input('Infome ate qnt quer multiplicar: '))
for c in range(0, f+1):
    print(f'{n} x {c} = {n*c}')
