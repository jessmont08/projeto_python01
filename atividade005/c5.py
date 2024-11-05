# Faça um programa que leia o nome de uma pessoa e verifique se a palavra 'Oliveira' está presente neste nome, mostrando True ou False.

import os

os.system('cls')

print('-' * 90)
print('Verificação de nomes.')
print('=' * 90)

nome = str(input('ENTRE COM SEU NOME: '))

if 'oliveira' in nome:
    print(f'O nome {nome} contêm o sobrenome Oliveira.')
else:
    print(f'O nome {nome} não contêm o sobrenome Oliveira.')

print('=' * 90)
print()