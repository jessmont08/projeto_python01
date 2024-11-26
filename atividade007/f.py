import os

import random

os.system('cls')

lista = []
crescente = []
decrescente = []

for i in range(6):
    numeros = random.randint(0, 5)

    lista.append(numeros)

crescente = lista
crescente.sort()

decrescente = lista
decrescente.sort(reverse=True)

print(f'A ordem crescente é {crescente}')
print(f'A ordem decrescente é {decrescente}')

