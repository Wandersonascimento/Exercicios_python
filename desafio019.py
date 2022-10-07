#criar um programa para sortear um entre quatro nomes
import random
print('desafio 019\n')
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quato aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido é: {}'.format(escolhido))
