#Criar um programa que conte qnts letras 'a' aparece na frase e a posição da primeira e ultima
print('\033[1;31;40mDesafio 026\033[m\n')
print('{:*^20}'.format(' Bem vindo '))
frase = str(input('\033[1;33mDigite uma Frase: \033[m')).strip().upper()
print(f'A frase tem \033[1;34m{frase.count("A")}\033[m letras "A"')
print(f'A letra A apareceu na primeira vez na posição \033[1;34m{frase.find("A")+1}\033[m')
print(f'A letra A apareceu pela ultima vez na posição \033[1;34m{frase.rfind("A")+1}\033[m')








