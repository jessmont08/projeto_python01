# Faça um programa que receba o nome completo 
# de uma pessoa e, em seguida, mostre
#  o primeiro e o último nome.

import os

os.system('cls')

print('-' * 90)
print('PRIMEIRO E ÙLTIMO NOME.')
print('=' * 90)

nome = str(input('Nome: '))

lista = nome.split()

nome1 = lista[:1]
nome3 = lista[-1:]

print(f'Nome: {nome1}, sobrenome: {nome3}.')
print('-' * 90)
print()