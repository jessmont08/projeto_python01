# Elabore um programa que peça as dimensões de um retângulo e calcule seu perímetro.

import os
os.system('cls')

print('-' * 90)
print('CALCULAR A BASE DO PERÍMETRO')
print('=' * 90)

base = float(input('ENTRE COM O VALOR DA BASE:'))
lados = float(input('ENTRE COM O VALOR DOS LADOS:'))

perimetro = (base * 2) + (lados * 2)

print('-' * 90)
print('RESULTADO')
print('=' * 90)

print(f'A área do perímetro é: {perimetro}')
