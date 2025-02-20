#) A empresa "TechSolutions" contratou você para desenvolver um programa em Python que irá automatizar uma parte do seu sistema de processamento de dados.
# Eles precisam de um programa que solicite ao usuário a entrada de um número inteiro e, em seguida, verifique se esse número é par ou ímpar.
#  Essa funcionalidade é essencial para o sistema deles, pois eles processam grandes conjuntos de dados e precisam classificar os números de forma eficiente
#  para realizar cálculos específicos em cada tipo de número.


import os


os.system('cls')

print('-' * 90)
print('Tech Solutions.')
print('=' * 90)

valor = int(input('Entre com o numéro, usuário: '))

print('.' * 90)

if valor % 2 == 0:
    print('o numéro é par.')
else:
    print('O numéro é ímpar.')

print('-' * 90)