# Evolua o programa anterior para um código que pergunte
# ao usuário qual o intervalo que ele deseja ver  impresso.

import os

os.system('cls')


inicio = int(input('Entre com o valor inicial: '))
fim = int(input('Entre com o valor final: '))

for i in range(inicio, fim + 1):


    print(f'Valor: {i}')

print()