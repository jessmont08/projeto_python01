import os


os.system('cls')

dicionario = dict()

print('\nMenu de opções')

while True:

    print('1. Adicionar um par de chave-valor')
    print('2. Mostrar dicionário')
    print('3. AMostrar tamanho do dicionário')
    print('4. Fazer uma cópia do dicionário')
    print('5. Limpar dicionário')
    print('6. Sair')

    opcao = int(input('Escolha a opção: '))

    if opcao == '1':
        chave = input('Adicione a chave: ')

        while not chave: 
            print('A chave não pode estar vazia.')
            chave = input('Adicione a chave: ')

        valor = input('Digite o valor: ')

        while not valor: 
            print('A valor não pode estar vazia.')
            
            valor = input('Adicione a valor: ')

        dicionario[chave] = valor
        print(f'Par: {chave}: {valor} adicionado.')

    elif opcao == '2':
        print(f'Dicionário atual = {dicionario}')

    elif opcao == '3':
        tamanho = len(dicionario)
        print(f'O dicionário tem {tamanho} elementos.')

    elif opcao == '4':
        copia_dicionario = dicionario.copy()
        print('Copia do dicionário', copia_dicionario)

    elif opcao == '5':
        dicionario.clear()
        print('Dicionário limpo.')

    elif opcao == '6':
        print('Saindo...')
        break

    else:
        print('Opção inválida.')