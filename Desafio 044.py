# Elaborar um programa de pagamento e calcule a condição:
# a vista 10% de desconto
# a vista cartao 5% de desconto
# parcelado em 2x preço normal
# 3x ou mais , juros de 20%.

valor = float(input('Informe o valor das compras R$ '))
print('Informe a condição de pagamento:\n[ 1 ] - a vista 10% desconto.\n[ 2 ] - A vista Cartao 5% desconto\n[ 3 ] - Parcelado em 2x.\n[ 4 ] - Parcelado em 3 ou mais vezes + 20%.')
codigo = int(input('Informe o codigo de pagamento: '))
if codigo<1 or codigo>5:
    print('\033[1;31mErro, informe o codigo de pagamento correto.')
elif codigo == 1:
    print(f'O valor a ser pago com o desconto de 10% é: R${valor-(valor/100*10):.2f}') #(valor *10 /100)
elif codigo == 2:
    print(f'O valor a ser pago com desconto de 5% é: R$ {valor-(valor/100*5):.2f}')
elif codigo == 3:
    print(f'O valor parcelado em 2x sem juros é: R$ {valor:.2f}')
elif codigo == 4:
    print(f'O valor parcelado acima de 2x acrecimo de 20%, valor a ser pago é: R${valor+(valor/100*20):.2f}')
    parcelas = int(input('Informe a quantidade de parcelas: '))
    print(f'Total de {parcelas}x de R${(valor+(valor/100*20))/parcelas:.2f}.')
