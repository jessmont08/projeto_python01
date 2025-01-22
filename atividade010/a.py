import os


os.system('cls')


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def contar_num(*numeros): 

    lista_pares = []
    lista_impares = []

    for i in numeros: 
        if i % 2 == 0:
            lista_pares.append(i)
        else: 
            lista_impares.append(i)

    cont_par = len(lista_pares)
    cont_impar = len(lista_impares)

    return lista_pares, lista_impares, cont_par, cont_impar

lista_pares, lista_impares, cont_par, cont_impar = contar_num(*numeros)

print('=' * 90)
print(f'A lista é {numeros}')
print(f'Os número pares são: {lista_pares}')
print(f'Há {cont_par} números pares.')
print(f'Os número impares são: {lista_impares}')
print(f'Há {cont_impar} números impares.')
print('=' * 90)
print()