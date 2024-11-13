# Faça um programa que leia o nome de um aluno e mostre quantas vezes a letra 'o' aparece e em que posição ela aparece pela primeira e última vez.
import os

os.system('cls')

print('-' * 90)
print('DESCOBRINDO NOMES.')
print('=' * 90)

nome = str(input('ENTRE COM SEU NOME: '))

o = nome.count('o')

primeiro = nome.find('o')
ultimo = nome.rfind('o')

print('=' * 90)
print('O nome {nome} tem {o} letras (o).')
print(f'A vogal aparece primeiro na casa {primeiro}.')
print(f'A vogal aparece por último na casa {ultimo}.')
print('.' * 90)
print()