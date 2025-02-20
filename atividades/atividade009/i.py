import os

os.system('cls')

estoque = dict()

for i in range(1, 4):
    nome = input('Digite o nome do produto: ')
    unidades = int(input('Digite as unidades restante: '))
    preco_unitario = float(input('Digite o preço unitário: '))

    estoque[nome] = {'unidades': unidades, 'preço': preco_unitario}

print('Menu de opções.')
print('1. Alterar algo.')
print('2. Deletar algo.')
print('3. Sair.')


while True:
    opcao = input('Escolha entre 1 e 3: ')

    if opcao == '1':
        item_alterado = input('Digite o nome da peça que deseja alterar: ').strip().lower()

        if item_alterado in estoque:
            alterando = input('Digite o que deseja alterar'
                            '\n(nome, unidades ou preço): ').strip().lower()
            
            if alterando in estoque[item_alterado]:
                alteracao = input('Digite a alteração: ').strip().lower()
                
            else:
              print('Esse item não existe.')

        else:
          print('Esse item não existe.')

        
        estoque[item_alterado][alterando] = alteracao

    if opcao == '2':
        item_apagado = input('Digite o item que deseja excluir: ')
        if item_apagado in estoque:
            del estoque[item_apagado]

    elif opcao == '3':
        break

    else:
        print('Digite 1, 2 ou 3.')


ordenados = dict(sorted(estoque.items(), key= lambda item: item[0]))

for keys, values in ordenados.items():
    print(f'{keys}: {values}')

soma = sum(item['unidades'] * item['preço'] for item in estoque.values())

print(f'O valor atual do estoque é R${soma:.2f}')
