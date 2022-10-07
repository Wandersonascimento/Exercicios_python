# A CNN precisa de um programa que leia o ano de nascvimento de um atletae mostre a categoria:
# ate 9 anos mirim / ate 14 anos infantil/ ate 19 anos junior/ ate os 20 anos senior/ acima de 20 master
from datetime import date
anoatual = date.today().year
ano = int(input('Informe o ano de nascimento: '))
idade = anoatual - ano
print(f'quem nasceu em {ano} tem {idade} anos sua categoria é:')
if idade < 5:
    print('Nao tem idade para competir')
elif idade<=9:
    print('Categoria MIRIM.')
elif idade >9 and idade <=14:
    print('Categoria INFANTIL.')
elif idade >=19 and idade <= 20:
    print('Categoria SENIOR.')
elif idade>20:
    print('Categoria MASTER')