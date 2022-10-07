#desenvolçva um progara que pergunte a distancia em kms e calcule o valor da passagem cobrando 0,50 por km
# e 0,45 por viagens acima de 200km
print('Desafio 31\n')
km1 = int(input('Informe a distancia da viagem em kms: '))
print(f'A viagem tem {km1} kms')
print('-'*50)
if km1 > 200:
    print(f'O valor da passagem é R${km1*0.45:.2f} .')
else:
    print(f'O valor da passagem é R$ {km1*.50:.2f}')
