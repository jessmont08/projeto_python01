# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.


import os


os.system('cls')

soma = 0

for i in range(1, 101):
    if i % 2 == 0:
        soma += i


    print(f'{soma}', end= ' | ')
      