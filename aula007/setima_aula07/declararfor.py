import os


os.system('cls')

for var_iteradora in range(1, 7):
    print(f'Valor: {var_iteradora}',end= ' | ')

    print()
    print()

    # ou

    inicio = 1
    fim = 7
    passo = 2

    for var_iteradora in range(inicio, fim, passo):
        print(f'Valor: {var_iteradora}', end=' | ')

print()
print()