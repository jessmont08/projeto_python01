import os

os.system('cls')


nomes = ['larissa', 'lorena', 'sarah', 'mariana']

for indice, nomes in enumerate(nomes):

    minha_tupla = (indice, nomes)

    print(f'O nome "{minha_tupla[1]}", posição {minha_tupla[0]} da lista')
    print(f'O nome "{nomes}", posição {indice} da lista')
    print('.' * 90) 