#Escrva um programa que leia a velocidade de um carro e ese ele ultrapoassar  80km/h mostre a msg que ele foi multado
# a multa vai custar 7,00 por cada km acima do limite.
print('Desafio 29\n')
v1 = int(input('Informe a velocidade aferida: '))
print(f'A velocidade informada foi {v1}km/h')
print('-='*40)
if v1 >80:
    v2 = (v1 - 80)*7
    print(f'Voce foi multado em R$ {v2:.2f} por exeder a velocidade de 80km/h em {v1-80}km/h')
else:
    print('Voce nao foi multado parabens.')
