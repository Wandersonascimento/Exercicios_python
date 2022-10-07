#Criar um programa que mostre o primeiro e ultimo nome de uma pessoa
print('Desafio02\n')
nome = str(input('Digite o seu nome completo: ')).strip().title()
nome1 = nome.split()
print(f'O primeiro nome é: {nome1[0]}')
print(f'O ultimo nome é: {nome1[len(nome1)-1]}')
