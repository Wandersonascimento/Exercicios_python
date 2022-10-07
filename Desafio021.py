frase ='Wanderson do Nascimento cardoso'
print(len(frase)) #serve para contar quantas letras tem uma frase
print(frase.count('d')) #serve para conta quantas letras tem uma frase
print(frase.find('n'))# mostra onde começa a frase (posição) nao havendo ele mostra -1.
print('nascimento' in frase) #serve para saber se tem a paravra ou frase ele retorna true our false
#transformação
print(frase.replace('Wanderson', 'lindo')) # serve para trocar uma palavra
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip()) # remove espaços em inicio e final de frases.
print(frase.rstrip()) # remove espaços do lado direito R/Right
print(frase.lstrip()) # remode espaços do lado esquerto L/Left
#divisao
print(frase.split()) # cria divisao entre as palavras gera um lista
#junção
print('´´'.join(frase))



