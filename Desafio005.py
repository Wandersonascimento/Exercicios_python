#criar programa que leia um numero e mostre o seu sucessor e o seu antecessor.
print('desafio 005\n')
msginicial = ' Seja bem vindo '
msgfinal = ' Fim de Programa '
print('{:*^50}'.format(msginicial))
n = int(input(' Digite um numero: '))
print(' O numero que vc digitou foi: {} \n O seu sucessor é: {}; \n E o seu antecessor é: {}.'.format(n, (n+1), (n-1)))
print('{:*^50}'.format(msgfinal))
