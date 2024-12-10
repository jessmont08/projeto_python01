# Implemente um programa que receba um número inteiro e imprima sua tabuada de multiplicação.

import os

os.system('cls')

print('-' * 90)
print('TABUADA DO VALOR DESEJADO')
print('-' * 90)

numero = float(input('ENTRE COM O VALOR DESEJADO: '))

valor1 = numero * 1
valor2 = numero * 2
valor3 = numero * 3
valor4 = numero * 4
valor5 = numero * 5
valor6 = numero * 6
valor7 = numero * 7
valor8 = numero * 8
valor9 = numero * 9
valor10 = numero * 10

print('-' * 90)
print('RESULTADO')
print('-' * 90)

print(f'A tabuada de {numero} do 1 é: {valor1}')
print(f'A tabuada de {numero} do 2 é: {valor2}')
print(f'A tabuada de {numero} do 3 é: {valor3}')
print(f'A tabuada de {numero} do 4 é: {valor4}')
print(f'A tabuada de {numero} do 5 é: {valor5}')
print(f'A tabuada de {numero} do 6 é: {valor6}')
print(f'A tabuada de {numero} do 7 é: {valor7}')
print(f'A tabuada de {numero} do 8 é: {valor8}')
print(f'A tabuada de {numero} do 9 é: {valor9}')
print(f'A tabuada de {numero} do 10 é: {valor10}')

print()
