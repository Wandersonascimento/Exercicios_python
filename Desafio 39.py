# Escreva um program que leia o nascimento e mostre se ele vai alistar se esta na hora ou se ja passou o tempo.

from datetime import date

anoatual = date.today().year
anonascimento = int(input('Informe o ano de nascimento: '))
if anoatual - anonascimento < 18:
    print(f'Falta {anonascimento + 18 - anoatual} anos para voce se alistar. voce ira se alista no ano {anonascimento + 18}.')
elif anoatual - anonascimento == 18:
    print('Parabens voce se alista esse ano')
elif anoatual - anonascimento > 18:
    print(f'Ja se passaram {anoatual - anonascimento - 18} anos do seu alistamento')
print(date.today())