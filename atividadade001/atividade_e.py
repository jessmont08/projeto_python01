# Faça um programa que receba um número inteiro e exiba seu sucessor e antecessor.

import os
os.system('cls')

print('-' * 90)
print('ANTECESSOR E SUCESSOR')
print('=' * 90)

valor_inicial = float(input('ENTRE COM O NÚMERO: '))

antecessor = valor_inicial - 1
sucessor = valor_inicial + 1

print()
print('-' * 50)
print('RESULTADOS')
print('=' * 50)

print(f'O valor inicial é = {valor_inicial}')
print(f'O valor antecessor a ele é = {antecessor}')
print(f'O valor sucessor a ele é {sucessor}')
print('-' * 90)
print()