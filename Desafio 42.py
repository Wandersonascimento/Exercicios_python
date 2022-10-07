# programa que leia os lados de um triangulo e  informe:
# equilatero todos os lados sao iguais
#isosceles dois lados iguais
#escaleno todos os lados diferentes.

r1 = int(input('Informe o primeiro seguimento: '))
r2 = int(input('Informe o segunmdo seguimento: '))
r3 = int(input('Informe o terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and  r3 < r1 + r2:
    print('Os seguimentos acima, PODEM FORMAR um triangulo', end=' ')
    if r1 == r2 == r3:
        print('\033[34mEquilatero')
    elif r1 != r2 != r3 != r1:
        print('\033[34mEscaleno')
    else:
        print('\033[34mIsoceles')
else:
    print('\033[1;31mOs seguimentos acima informado NAO PODEM formar um triangulo.')