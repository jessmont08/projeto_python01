import os


os.system('cls')

dicionario = dict()

print('\nMenu de opções')

while True:

    print('1. Adicionar um par de chave-valor')
    print('2. Mostrar chaves do dicionário.')
    print('3. Mostrar valores do dicionário')
    print('4. Mostrar itens do dicionário')
    print('5. Sair')

    opcao = input('Escolha a opção: ')

    if opcao == '1':
        chave = input('Digite a chave:')
        valor = input('Digite o valor: ')

        dicionario[chave] = valor
        print(f'Par {chave} : {valor} adicionado.')

    elif opcao == '2':
        if dicionario:
            print('Chaves do dicionário', dicionario.keys())
        else:
            print('O dicionário está vazio. Adicione os itens primeiro.')

    elif opcao == '3':
        if dicionario:
            print('Valores do dicionário:', dicionario.values())

        else:
            print('O dicionário  está vazio. Adicione os itens primeiro.')

    elif opcao == '4':
        if dicionario:
            print('Itens do dicionário:', dicionario.items())

        else:
            print('O dicionário está vazio. Adicione os itens primeiro.')

    elif opcao == '5': 
        print('Saindo...')
        break

    else:
        print('Opção ínvalida.')