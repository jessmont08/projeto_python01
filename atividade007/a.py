
import os
os.system('cls')

lista = []
soma = 0

while (True):

    print('Digite "s" para sair.')
    notas = input('Entre com as notas: ').lower().strip()
    

    if notas != "s":
        print(f'Digite a proxíma.')
    else:
        break
    
    lista.append(notas)
    number = int(notas)
    soma += number

print(f'A lista gerada é {lista}')

quantidade = len(lista)

print(f'A quantidade de notas inseridas no sistema foi: {quantidade}.')

reversa = lista[::-1]

print('Notas invertidas: ')
for i in range(len(lista)):
    print(f'{reversa[i]}')

print(f'A soma das notas é {soma}')

media = soma / quantidade

print(f'A média das notas é {media}')