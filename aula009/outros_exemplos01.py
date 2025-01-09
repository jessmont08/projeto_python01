import os


os.system('cls')

elementos = {}
periodica = []

for c in range(2):
    print(f"Entrada de dados {c+1}: ")
    simbolo = str(input('Digite o símbolo do elemento: '))
    nome = str(input('Digite o nome do elemento: '))

    elementos['simbolo'] = simbolo
    elementos['nome'] = nome
    
    periodica.append(elementos.copy())

print()
print('-' * 90)
print('Elementos na tabela periódica')
print('=' * 90)

print('Detalhes dos elementos.')
for elemento in periodica:
    for chave, valor in elemento.items():
        print(f'{chave.capitalize()} : {valor}')
    print('-' * 90)

