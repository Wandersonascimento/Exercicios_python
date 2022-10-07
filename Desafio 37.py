# Escreva um progara que leia um numero inteiro qualquere peça ao usuario esqu escolha a base de conversao:
# 1 para binario
# 2 para Octal
# 3 para hexadecimal

numero = int(input('Informe um numero '))
print('Informe a base de confsao:\n[ 1 ] Binario\n[ 2 ] Octal\n[ 3 ] Hexadecimal')
base = int(input('Qual a base: ' ))
if base ==1:
    print(f'O numero {numero} convertido para binario é {bin(numero)[2:]}')
elif base ==2:
    print(f'O numero {numero} convertido para octal é {oct(numero)[2:]}')
elif base == 3:
    print(f'O numero {numero} convertido para hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção invalida tente novamente')

