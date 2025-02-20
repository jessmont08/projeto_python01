# Faça um programa que receba o nome 'João da Silva' e, em seguida, substitua 'Silva' por 'Oliveira'.


import os


os.system('cls')

print('-' * 90)
print('ALTERAÇÃO DO NOME')
print('=' * 90)

nome = str(input('NOME: '))
print('-' * 90)

substituindo = nome.replace('Silva' , 'Oliveira')

print(f'O nome original é {nome}.')
print(f'A alteração mudou ele para {substituindo}.')

print('.' * 90)
print()