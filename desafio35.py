#desafio 35 triangulo

print('Desafio 35\n')
print('-='*15)
print('Calculo de triangulo')
print('-='*15)

r1 = float(input('Informe o primeiro seguimento: '))
r2 = float(input('Informe o segundo seguimento: '))
r3 = float(input('Informe o terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas PODEM formar um triangulo.')
else:
    print('As retas NAO PODEM formar um triangulo!')
