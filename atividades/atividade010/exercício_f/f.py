import os


os.system('cls')

from unir.listas import juntar_listas

unindo = juntar_listas()

for keys, values in unindo.items():
    print(f'{keys}: {values}')