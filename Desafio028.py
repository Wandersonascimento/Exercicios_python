#Escreva um programa que informe um sorteio de um numero entre 0 e 5.
import random
from time import sleep
print('numero da sorte \n')
nome = str(input('Informe o seu nome:')).strip().title()
num = int(input(f'{nome}, escolha um número entre 1 e 05 e veja se vc ganhou: '))
r1 = random.randint(1, 5)
print(f'Seu numero é: {num}, boa sorte!')
print('-'*50)
print('Prcessando...')
sleep(1)
print(f'O número sorteado foi: {r1}.\n')
if r1 == num:
    print(f'***** Parabéns {nome} voce ganhou. *****')
else:
    print(f'Infelizmente {nome} voce nao ganhou! tente novamente!!!!')

