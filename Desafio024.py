#criar um programa que diga se comseça com santo ou nao
print('Desafio024\n')
cidade = str(input('Digite o nome de um cidade: ')).strip().upper()
print(f'{cidade[:5] == "SANTO"}')

