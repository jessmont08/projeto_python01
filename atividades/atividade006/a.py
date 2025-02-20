# Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.


import os 

os.system('cls')

lista = [1, 2, 3, 5, 6]

print(f'A lista errada é: {lista}.')

lista.insert(3, 4)

print(f'A lista corrigida é: {lista}.')