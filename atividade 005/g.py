#Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.

import os


os.system('cls')

inicio = int(input('Entre com o início: '))
fim = int(input('Entre com o final: '))

for i in range(inicio, fim):
    if i % 2 != 0:
        print(f'Valor: {i}')
    else:
        continue

    print('.' * 90)

    print()