# programa que leia a média de duas notas. abaixo de 5.0 reprovado, media entre 5.0 e 6.9 recupeção 7.0 acima aprovado:

nota1 = float(input('Informe a primeira nota: '))
if  nota1>10 or nota1<0:
    print('A nota deve ser comprendia entre 0 a 10')
    exit()
nota2 = float(input('Informe a segunda nota: '))
if  nota2>10 or nota2<0:
    print('A nota deve ser comprendia entre 0 a 10')
    exit()
media = (nota2+nota1)/2
print(f'A média foi \033[1;34m{media:.2f}\033[m')
if media < 5:
    print('Aluno \033[1;31mREPROVADO')
elif media >= 5 and media <=6.9:
    print('Aluno em \033[1;33mRECUPERAÇÃO')
elif media >= 7 and media <=9.9:
    print('Aluno \033[1;32mAPROVADO')
elif media == 10:
    print('\033[1;32mPARABENS, VOCE CONQUISTOU A MELHOR NOTA!!!!')


