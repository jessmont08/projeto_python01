#Faça um programa que leia uma frase e depois exiba na tela:
# A frase em minúsculas, a frase em maiúsculas, a quantidade de caracteres na frase e quantas letras tem a 2ª palavra na frase.


import os

os.system('cls')

print('-' * 90)
print('ALTERAÇÔES POR FRASES.')
print('=' * 90)

frase = str(input('ENTRE COM A FRASE: '))

print('-' * 90)
quantidade = len(frase)
minusculas = frase.lower()
maiusculas = frase.upper()

print(f'A frase original é {frase}.')
print(f'A quantidade de caracteres são: {quantidade}.')
print(f'A versão maiúsculo é: {maiusculas}.')
print(f'A versão minúscula é: {minusculas}.')
print('.' * 90)

print()