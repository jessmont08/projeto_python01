import os


dicionario = {}
os.system('cls')

while True:

    print('\nMenu de opções.')
    print('1. Criar dicionários com FromKeys.')
    print('2. Buscar valor de uma chave com Get().')
    print('3. Sair.')

    opcao = input('Escolha a opção: ')

    if opcao == "1":
        chaves = input('Digite as chaves separadas por vírgula: ').split(',')
        valor_padrao = input('Digite o valor padrão para as chaves: ')


        if not chaves or not valor_padrao:
            print('Erro: Chaves ou valor padrão não podem estar vazios.')
        else: 
            dicionario = dict.fromkeys(chaves, valor_padrao)
            print(f'Dicionário criado:' , dicionario)

    elif opcao == '2':
        if dicionario:
            print('Chaves disponiveis: ', ', '.join(dicionario.keys()))
            chave = input('Digite a chave que deseja buscar: ')
            valor = dicionario.get(chave, 'Chave não encontrada.')

            print()

            print(f"Valor para a chave '{chave}': {valor}'")

        elif opcao == '3':

            print('Saindo...')
            break

        else:

            print('Opção ínvalida, tente novamente.')