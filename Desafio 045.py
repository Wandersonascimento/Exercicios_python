from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
#print(f'O computador escolheu {itens[computador]}')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador >3:
    print('Opção invalida')
    exit()
sleep(1)
print('\033[31mJo')
sleep(1)
print('   \033[34mken')
sleep(1)
print('      \033[33mpo!!!\033[m')
sleep(1)
print('-='*20)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*20)
if computador == 0: # pedra
    if jogador == 0: #pedra vs pedra
        print('\033[1;33mEmpate')
    elif jogador == 1: #pedra vs papel
        print('\033[1;32mJogador Vence')
    elif jogador == 2:#pedra vs tesoura
        print('Computador Vence')
elif computador == 1:# papel
    if jogador == 0: # papel vs pedra
        print('Computador vence!')
    elif jogador == 1: #papel vs papel
        print('\033[1;33mEmpate')
    elif jogador ==2: #papel vs tesoura
        print('\033[1;32mJogador vence')
elif computador == 2: # tesoura
    if jogador == 0: #tesoura vs pedra
        print('\033[1;32mJogador vence')
    elif jogador == 1: # tesoura vs papel
        print('Computador vence')
    elif jogador == 2: #tesoura vs tesoura
        print('\033[1;33mEmpate')

