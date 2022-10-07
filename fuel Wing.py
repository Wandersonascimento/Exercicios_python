# cada asa pega 1000kg
# o restante vai para o central
print('\033[32m-=\033[m'*20)
print('{: ^45}'.format('\033[34mCALCULO DE FUEL\033[m'))
print('\033[32m-=\033[m'*20)


fuel = float(input('\033[1;33mInforme a quantidade de combustivel: \033[m'))
if fuel > 12500 or fuel < 500:
    print('\033[1;31;40m O combustivel deve ser no minimo 500.00 kgs e o maximo de 12500.00 kgs \033[m')
    exit()
if fuel >= 7000:
    print(f' Asa esquerda \033[34m3500.00 Kg\033[m\n Asa Direita \033[34m3500,00 Kgs\033[m\n Tanque central \033[34m{fuel-7000:.2f} kgs\033[m')
else:
    print(f' Asa esquerda \033[34m{fuel/2:.2f} / {3500 - (fuel/2):.2f}\033[m\n Asa Direita \033[34m{fuel/2:.2f} / {3500 - (fuel/2):.2f}\033[m\n Central \033[34m0.00 / 5500.00\033[m')
print(f' Disponivel \033[1;32m{12500 - fuel:.2f} kgs')


