nome = str(input('Qual o seu nome? ')).strip().title()
if nome == 'Wanderson':
    print(f'{nome} que nome lindo!')
elif nome == 'Pedro' or nome == 'Ronaldo' or nome == 'Maria':
    print(f'Seu nome é bem popular no Brasil {nome}')
elif nome in ' Ana Cláudia Jessica Juliana':
    print(f'O seu nome é {nome}, um belo nome feminino.')
else:
    print(f'Tenha um otimo dia {nome}')