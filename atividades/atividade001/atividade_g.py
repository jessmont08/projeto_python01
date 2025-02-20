# Crie um programa que converta uma medida em metros para centímetros e milímetros.


import os 

os.system('cls')

print('-' * 90)
print('CONVERTER MEDIDAS')
print('=' * 90)

valor = float(input('ENTRE COM O VALOR DE MILíMETROS:'))

centimetros = valor / 10

print('-' * 90)
print('RESULTADOS')
print('=' * 90)

print(f'O valor de milímetros foi: {valor}')
print(f'A conversão para centrímetros é: {centimetros}')
print()
print('-' * 90)