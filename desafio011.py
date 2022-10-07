#criar um programa que calcula a area de um "parede" altura x largura em metros e, calculçe a quantidade de tinta
# 1 litro igual a 2m²
print('Desafio 011\n')
print('Programa de cálculo de tinta\n')
print('{:*^50}\n'.format(' Bem vindo '))
altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
area = altura * largura
tinta = area / 2
print('A area total é de {:.2f}m²'.format(area))
print('Voce gastara nesta pintura {:.2f} Litros de tinta'.format(tinta))
print('\n{:*^50}'.format(' Final de programa '))
