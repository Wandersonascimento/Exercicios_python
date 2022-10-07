pista = int(input('Informe a pista em uso: '))
wind = int(input('Informe o vento: '))
dmg = int(input('Informe a Declinação: '))
winddmg = wind + dmg
rwy = pista *10
rwy180 = pista + 18
if rwy180 > 36:
    rwy180 = rwy180 - 36
print(f'\033[1;32m{pista}\033[1;34m → → → →:::===------\033[33m-------\033[31m===||| \033[33m{rwy180}\033[m')
print(f'vento {wind} + a DMG de {dmg} = {winddmg}º')
ang = rwy - winddmg
if rwy >= winddmg:
    ang = rwy - winddmg
if winddmg >= rwy:
    ang = winddmg - rwy
print(f'angulo de {ang}º')
if ang == 0 or ang == 360:
    print('Vento de proa alinhado em 000º.')
if ang == 180:
    print(f'Vento totalmente de calda. Use a Cabeceira {rwy180}')
if ang > 0 and ang <85:
    print(f'Vento de proa pela DIREIRA em {ang}º.')
if ang > 85 and ang <95:
    print(f'Vento de travez pela direita em {ang}º.')
if ang > 95 and ang < 180:
    print(f'Vendo de CALDA pela direita em {ang}º. Use a Cabeceira {rwy180}.')
if ang > 180 and ang < 265:
    print(f'Vento de CALDA pela ESQUERDA em {ang}º. use a Cabeceira: {rwy180}.')
if ang >265 and ang < 275:
    print(f'Vento de Travez em {ang}º pela Esquesda.')
if ang > 275 and ang < 360:
    print(f'Vento de proa pela ESQUERDA em {ang}º.')
