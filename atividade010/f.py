import os


os.system('cls')


def juntar_listas():
    lista1 = ['nome', 'idade', 'peso']
    lista2 = ['john', '40', '80']

    return dict(zip(lista1, lista2))

unindo = juntar_listas()

for keys, values in unindo.items():
    print(f'{keys}: {values}')