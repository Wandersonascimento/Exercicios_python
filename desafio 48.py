contador = 0
soma = 0
for c in range(1, 501, 2): # contando de 2 em dois 1, 3, 5... ate 501.
    if c % 3 == 0: # multiplo de tres
        soma = soma + c # soma c que no caso agora e multoplo de tres, conforme o exercio informa/ simplicado: soma += c
        contador = contador + 1 # pode ser escrito simplicado contador += 1
print(f' A soma de todos os numeros impares multplos de tres é {soma}, realizado por {contador}')
