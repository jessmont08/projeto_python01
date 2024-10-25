# Implemente um programa que receba dois números e realize a divisão, formatando o resultado com quatro casas decimais.

import os

os.system('cls')

print('-' * 90)
print('DIVISÃO COM 4 DECIMAIS')
print('=' * 90)

valor1 = float(input('ENTRE COM O VALOR: '))
valor2 = float(input('ENTRE COM O VALOR 2: '))

divisao = valor1 / valor2 

print(f'A divisão será {divisao: 4f}')
