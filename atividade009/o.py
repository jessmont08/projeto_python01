import os

os.system('cls')

academia = dict()

for i in range(1, 2):
    nome = input('Digite o nome do aparelho: ')
    tipo = input('Digite se ele é de cardio ou/e musculação: ')
    estado = input('Digite o estado de conservação dele: ')
    quantidade = int(input('Digite quantos dele tem: '))

    academia[nome] = {'tipo': tipo, 'estado': estado, 
                      'quantidade': quantidade}
    
print(academia)

print('Menu de opções.')
print('1. Alterar estado.')
print('2. Alterar quantidade.')
print('3. Sair.')

while True:
    opcao = input('Digite o número do menu: ')

    if opcao == '1':
        alterando_estado = input('Digite o nome do aparelho que'
                                 '\ndeseja alterar o estado: ').strip().lower()
        
        if alterando_estado in academia:
            novo_estado = input('Digite o novo estado: ')

            academia[alterando_estado]['estado'] = novo_estado

    elif opcao == '2':
        alterando_quantidade = input('Digite o nome do aparelho'
                                 '\ndeseja alterar a quantidade: ')
        
        if alterando_quantidade in academia:
            nova_quantidade = input('Digite a nova quantidade: ')

            academia[alterando_quantidade]['quantidade'] = nova_quantidade

    elif opcao  == '3':
        print('Saindo.')
        break

    else:
        print('Digite um dos valores.')

ordenados = sorted(academia.items(), key= lambda item: item[1]['tipo'])
for keys, values in ordenados:
    print(f'{keys} : {values}')

cardio_aparelhos = 0

for values in academia.values():
    if values['tipo'] == 'cardio':
        cardio_aparelhos += 1

print(f'Há {cardio_aparelhos} aparelhos na academia.')

reparos = 0

for values in academia.values():
    if values['estado'] == 'necessitando reparos':
        reparos += 1

print(f'Há {reparos} precisando de reparos.')
