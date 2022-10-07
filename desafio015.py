# escreva um programa que pergunete a quantidade de km percorridos por um carro alugado e a quantidade de dias
# pelo qua foi alugado.
#  a diaria custa r$ 60,00 e o km custa R$0,15.
print('Desafio 15\n')
print('{:*^80}\n'.format(' Seja bem vindo '))
dias = int(input('Quantos dias o carro ficou alugado? '))
km1 = int(input('Informe o km inicial: '))
km2 = int(input('Informe o KM final: '))
diaria = float(input('Informe o valor da diaria: R$ '))
valorkm = float(input('Informe o valor do KM: R$ '))
kmtotal = km2 - km1
print('- Diaria R${:.2f} , dias {}, Total: R${:.2f};\n- Valor por KM R$ {:.2f}, Km Ultilizados {}Kms, Total R$ {:.2f};\n- Total geral R$ {:.2f}\n'.format(diaria, dias, (diaria*dias), valorkm, kmtotal, kmtotal*valorkm, (diaria*dias)+(kmtotal*valorkm)))
print('{:*^80}'.format(' Final de Programa'))

