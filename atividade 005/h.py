#Faça um programa que imprima os valores no intervalo definidos pelo usuário. 
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

inicio = int(input('Entre com o ínicio: '))
fim = int(input('Entre com o fim: '))

for i in range(inicio, fim):

    if i == 22:
        continue

    elif i == 12:
        continue

    elif i == 32:
        continue

    else:
        print(f'Contando: {i}')