
# Mostre a quantidade de notas que foram lidas.
# Exiba todas as notas na ordem em que foram informadas.
# Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# Calcule e mostre a soma das notas.
# Calcule e mostre a média das notas.

import os
os.system('cls')

lista = []

while (True):

    print('Digite "s" para sair.')
    notas = str(input('Entre com as notas: ')).lower().strip()

    if notas != "s":
        print(f'Digite a proxíma.')
    else:
        break
    
    lista.append(notas)
print(f'A lista gerada é {lista}')

quantidade = len(lista)

print(f' A quantidade de notas inseridas no sistema foi: {quantidade}.')

reversa = lista[::-1]

for i in range(len(lista)):
    print(f'notas invertidas {reversa[i]}')

    