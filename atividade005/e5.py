# Faça um programa que receba uma frase e, em seguida, mostre quantas vezes as vogais foram utilizadas.

import os

os.system('cls')

print('-' * 90)
print('VOGAIS NA FRASE.')
print('=' * 90)

frase = str(input('ENTRE COM A FRASE: '))

a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o') 
u = frase.count('u')

total = a + e + i + o + u 

print('-' * 90)
print(f'A vogal A é usada {a} vezes.')
print('.' * 90)

print('-' * 90)
print(f'A vogal E é usada {e} vezes. ')
print('.' * 90)

print('-' * 90)
print(f'A vogal I é usada {i} vezes. ')
print('.' * 90)

print('-' * 90)
print(f'A vogal O é usada {o} vezes. ')
print('.' * 90)

print('-' * 90)
print(f'A vogal U é usada {u} vezes. ')
print('.' * 90)

print()