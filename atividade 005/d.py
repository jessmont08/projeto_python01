# Faça um programa que imprima os números pares entre 0 e 100.


import os

os.system('cls')

for i in range(0, 101):
    if i % 2 == 0:
        print(i, end= ' | ')
    if i == 50:
        print()
    
    else:
        continue

    print()