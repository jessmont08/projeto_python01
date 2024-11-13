#Faça um programa que imprima os números no intervalo
# entre 1 e 100. Os números devem ser apresentados na horizontal.

import os


os.system('cls')

print('-' * 90)
print('Contagem de 1 a 100')
print('=' * 90)

for i in range(1, 101):
    print(f'{i}', end= '|')
    if i == 20:
        print()
    if i == 37:
        print()
    if i == 54:
        print() 
    if i == 71:
        print()
    if i == 88:
        print()     
        
print()