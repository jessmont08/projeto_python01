

import os

os.system('cls')

print('-' * 90)
print('LISTAS')
print('=' * 90)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f'A lista é {lista}')

# intervalo de 0 a 9
lista2 = lista[0:9]
print(f'Em intervalo de 1 a 9: {lista2}')

print('=' * 90)

lista3 = lista[7:13]
print(f'Em intervalo de 8 a 13: {lista3}')

print('=' * 90)


for c in range(0, 15):
    if c % 2 == 0:
        print(f'Os números pares são: {c}')
    
    else:
        continue

print('=' * 90)

for c in range(0, 16):
    if c % 2 != 0:
        print(f'Os números ímpares são: {c}')
    else: 
        continue

print('=' * 90)

for c in range(15):

    if c % 2 == 0:
        print(f'É multiplo de 2: {c}')
    else:
        continue

print('=' * 90)

for c in range(16):

    if c % 3 == 0:
        print(f'É multiplo de 3: {c}')
    else:
        continue

print('=' * 90)

for c in range(16): 
            
    if c % 4 == 0:
         print(f'É multiplo de 4: {c}') 
                
    else:
        continue

print('=' * 90)

lista.reverse()

print(f'A lista reversa é {lista}')

produto1 = lista[6] * lista[12]
produto2 = lista[5] * lista[11]

print(f'O primeiro produto de soma é: {produto1}')
print(f'O segundo produto de soma é: {produto2}')

print('=' * 90)
print()