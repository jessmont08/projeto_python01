# Desenvolva um programa que solicite um valor em reais e calcule quantos dólares podem ser comprados com esse valor.

import os
os.system('cls')

print('-' * 90)
print('VALOR DE REAIS EM DOLÁRES')
print('=' * 90)

reais = float(input('ENTRE COM O VALOR EM REAIS: '))

doláres = reais / 5.71

print('-' * 90)
print('CONVERSÂO')
print('=' * 90)

print(f'Se você tem {reais} reais, comprará {doláres:.2f} doláres.')
print('-' * 90)
print()