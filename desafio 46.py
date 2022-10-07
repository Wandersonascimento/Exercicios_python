# faça um programa que mostre  na tela uma contagem regreciva com pausa de 1 segundo
from time import sleep
print('Contagem regreciava para contagem:')
s = input('pressione enter para iniciar ')
for c in range(10, -1, -1):
    sleep(0.5)
    print(c, end=' - ')
print('\033[31m\n     \n    Fogos de artificio acionado ! ! !')
