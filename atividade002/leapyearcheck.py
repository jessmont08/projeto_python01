# A empresa "LeapYearCheck" está desenvolvendo um software de verificação de anos bissextos para auxiliar usuários na 
# identificação desses anos de forma rápida e precisa. Eles precisam de um programa que permita aos usuários inserir um ano e,
#  em seguida, determine se esse ano é bissexto ou não, de acordo com as regras estabelecidas pelo calendário gregoriano.
#  Além disso, é necessário realizar a validação de entrada de dados para garantir que o ano inserido pelo usuário 
# seja um valor válido, ou seja, um número inteiro positivo.

import os

os.system('cls')

print('-' * 90)
print('LEAP YEAR CHECK.')
print('=' * 90)

ano_atual = int(input('ENTRE COM O ANO: '))

if  (ano_atual % 4 == 0) or (ano_atual % 100 != 0) and (ano_atual % 400 == 0):
    print(f'O ano {ano_atual} é bissexto.')
else:
    print(f'O ano {ano_atual} não é bisssexto.')

print('=' * 90)