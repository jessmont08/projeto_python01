# Faça um programa que receba o nome completo de 
# uma pessoa e, posteriormente, imprima esse nome 
# separadamente.

import os

os.system('cls')

print('-' * 90)
print('NOME SEPARADAMENTE.')
print('=' * 90)

nome = str(input('NOME COMPLETO: '))

nome_separado = nome.split()

print(f'Bem vindo ao sistema, {nome_separado}.') 

print('=' * 90)

print()