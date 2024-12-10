import os

import datetime

os.system('cls')

print('-' * 90)
print('CALCULAR A IDADE DO USUÁRIO')
print('=' * 90)
print()

nome = str(input('ENTRE COM SEU NOME COMPLETO: '))
idade = int(input('ENTRE COM SEU ANO DE NASCIMENTO: '))

ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - idade

print('-' * 90)
print('DEFINIÇÕES')
print('=' * 90)

print(f'{nome}, você atualmente tem {idade} anos.')