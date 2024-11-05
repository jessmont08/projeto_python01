# Faça um programa que solicite separadamente o nome, o nome do meio e o sobrenome de uma pessoa. Em seguida, imprima o nome completo.

import os


os.system('cls')


print('-' * 90)
print('NOME COMPLETO.')
print('=' * 90)

nome = str(input('NOME: '))
nome_do_meio = str(input('NOME DO MEIO: '))
sobrenome = str(input('SOBRENOME: '))

nome_completo = nome + ' ' + nome_do_meio + ' ' + sobrenome

print(nome_completo)