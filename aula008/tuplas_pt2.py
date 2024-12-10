import os


os.system('cls')

numeros = int(input('Quantos elementos na tupla? '))

elementos = []

for c in range(numeros):
    while(True):
        valor = int(input(f'Digite o valor {c + 1}: '))
        if valor.isdigit():
            elementos.append(int(valor))
            
        else:
            print('Entrada inválida, digite um número.')

tupla = tuple(elementos)
print('.' * 90)
print(f'Tupla criada: {elementos}')
print('.' * 90)

while(True):

    valor = int(input('Verificar se o número está na tupla: '))
    
    if valor in tupla:
        print(f'O valor está na tupla.')

        contagem = tupla.count(valor)

        print(f'O valor aparece {contagem} vez(es)')

        indice = tupla.index(valor)
            
        print(f'O primeiro índice é em {indice}.')

    else:

        print(f'O número {valor} não está na tupla.')

    continuar = input('Deseja continuar? Digite sim ou não: ')

    if continuar != 'sim':
        break
print()

