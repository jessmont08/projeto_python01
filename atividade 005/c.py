#Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

import os


os.system('cls')

for i in range(0, 11)[::-1]:
    print(f'Números decrescentes: {i}', end= ' | ')
    
    if i == 7:
        print()
    if i == 3:
        print()
        

print()