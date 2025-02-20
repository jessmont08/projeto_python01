import os

os.system('cls')

informacoes = {'nome': 'john', 'idade' : '40', 'peso': '80',
               'altura' : '1.70'}              

print('=' * 90)
for keys, values in informacoes.items():
    print(f'{keys}: {values}')

print('=' * 90)

del informacoes['peso']

for keys, values in informacoes.items():
    print(f'{keys}: {values}')

print('=' * 90)