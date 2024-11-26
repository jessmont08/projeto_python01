import os

os.system('cls')

lista = []

for i in range(1, 7):
    nomes = input('Entre com o nome: ').lower().strip()

    lista.append(nomes)
    
if 'pedro' in lista:
    print('Pedro está na lista.')
else:
    print('Pedro não está na lista.')

print()