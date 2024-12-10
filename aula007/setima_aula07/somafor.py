import os


import os


print('=' * 90)

soma = 0

for var_iteradora in range(0,4):
    numero = int(input(f'Digite o {var_iteradora + 1}ª numero: '))

    soma += numero

print('=' * 90)
print(f'A soma dos valores é o número: {soma}')
print('.' * 90)