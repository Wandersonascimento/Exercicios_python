# fazer um programa de imc
#abixo de 18.5 - abaixo do peso
#entre 18.5 e 25 peso ideal
#entre 25 a 30 sobrepeso
#entre 30 ate 40 obesidade
#acima de 40 obesidade morbida

peso = float(input('Informe o seu peso: '))
print(f'O peso informado foi \033[34m{peso:.1f} Kg\033[m')
altura = float(input('Informe sua altura em cm: '))
altura = altura/100
print(f'A altura informada foi: \033[34m{altura:.2f}\033[m metros:')
imc = peso/(altura ** 2)
print(f'\033[1;34mO IMC desta pessoa é = {imc:.1f}\033[m ')
if imc < 18.5:
    print('\033[33mVoce está abaixo do peso.')
elif imc>=18.5 and imc<=25:
    print('\033[32mVoce esta no peso ideal')
elif imc >25 and imc <=30:
    print('\033[35mVoce esta com sobre-peso')
elif imc >30 and imc <=40:
    print('\033[91mvoce esta obeso')
elif imc > 40:
    print('\033[31mvoce esta com obseidade morbida')

