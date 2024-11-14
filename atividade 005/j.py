# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares,
# ao final do processo exiba na tela quantos números ímpares foram encontrados
# nesse intervalo, assim como a soma dos mesmos.

import os

os.system('cls')

soma = 0
quantidade = 0

for i in range (1, 100):
    
    if (i % 2 != 0):
        continue
    
    soma += i
    quantidade += 1
    

print(f'A soma desses números é: {soma}')   
print(f'A quantidade de números ímpares de 1-100 é: {quantidade}')

print()