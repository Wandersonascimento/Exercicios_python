# criar um programa que o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas // o nome com todas as letras minusculas // Qnts letras tem sem considerar os espaços
# Qtas letras tem // sem considerar os espaços // qtas letras tem o primeiro nome:
print('Desafio 022\n')
nome = str(input('Escreva o seu nome completo:  ')).strip()
print(f'Nome em Maiusculo: {nome.upper()}')
print(f'Nome em Minusculo: {nome.lower()}')
print(f'Primeira letras em Maiusculo: {nome.title()}')
print(f'Nome tem: {len(nome)-nome.count(" ")} Letras')
print(f'Total de caracteres + espaços: {len(nome.strip())}')
print(f'O nome tem: {nome.count(" ")} espaços vazios')
print(f'O nome tem: {"-".join(nome.split())}')
nome1 = nome.split()
print(f'O primeiro nome é: {nome1[0].upper()}, e tem {len(nome1[0])} letras.')
print(f'O primeiro nome tem: {len(nome1[0])} Letras')
