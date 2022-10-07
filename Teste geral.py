print('\033[1;34m-=\033[m'*20)
print('\033[1;34;48mCalculo de rumo e nivel de voo\033[m')
print('\033[1;34m-=\033[m'*20)

rumo = int(input('\033[1;33mInforme o rumo a ser voado: \033[m'))
if rumo>360 or rumo<0:
    print('\033[4;31mNao exite rumo maior que 360 ou menor que 0!\033[m')
    exit()
nivel = int(input('\033[1;33mInforme o nivel a ser voado: FL \033[m'))
if nivel > 450 or nivel < 49:
    print('\033[4;31mEscolha um nivel entre 050 a 450\033[m')
    exit()
niveldevoo = (nivel/10)%2
if niveldevoo == 1 and rumo >0 and rumo < 179:
    print(f'\033[1;32mO Nivel de voo está compativel ao rumo pretendido.\033[m')
elif niveldevoo == 0 and rumo >180 and rumo <360:
    print(f'\033[1;32mO Nivel de voo está compativel ao rumo pretendido.\033[m')
else:
    print(f'\033[1;31mO NÍVEL DE VOO INFORMADO NÃO É UM NIVEL VALIDO.\033[m')
    print('\033[4;34;40mEntre os rumos 000 a 179 use niveis IMPARES.\nEntre os rumos 180 a 359 use niveis PARES.\n*Todos os niveis de voo devem ser multiplos de 10')
