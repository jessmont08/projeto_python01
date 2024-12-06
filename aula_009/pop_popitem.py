import os


os.system('cls')

dicionario = dict()

print('\nMenu de opções')

while True:

    print('1. Adicionar um par de chave-valor')
    print('2. Remover item usando pop.')
    print('3. Remover o último item usando pop item')
    print('4. Mostrar dicionário atual.')
    print('5. Sair')

    opcao = input('Escolha a opção: ')

    if opcao == '1':
        chave = input('Digite a chave:')
        valor = input('Digite o valor: ')

        dicionario[chave] = valor
        print(f'Par {chave} : {valor} adicionado.')
    
     
    elif opcao == '2':
        if dicionario:
            chave = input('Digite a chave que deseja remover: ')
            valor_removido = dicionario.pop(chave, 'Chave não encontrada.')
            print(f'Item removido: {chave} : {valor_removido}')

        else:
            print('O dicionário está vazio. Adicione itens primeiros.')

    elif opcao == '3':
        if dicionario:
            chave, valor = dicionario.popitem()
            print(f'Último item removido: {chave} : {valor}')
        else:
            print('O dicionário está vazio. Adicione itens primeiros.')

    
    elif opcao == '4':
        if dicionario:
            print(f'Dicionário atual: {dicionario}')

        else:
            print('O dicionário está vazio.')

    
    elif opcao == '5': 
        print('Saindo...')
        break

    else:
        print('Opção ínvalida.')