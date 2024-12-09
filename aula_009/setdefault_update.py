import os


os.system('cls')

dicionario = dict()

print('\nMenu de opções')

while True:

    print('1. Adicionar um par de chave-valor')
    print('2. Definir um valor padrão usando setdefault.')
    print('3. Atualizar o dicionário usando update.')
    print('4. Mostrar dicionário atual.')
    print('5. Sair')

    opcao = input('Escolha a opção: ')

    if opcao == '1':
        chave = input('Digite a chave:')
        valor = input('Digite o valor: ')

        dicionario[chave] = valor
        print(f'Par {chave} : {valor} adicionado.')

    elif opcao == '2': 
        chave = input('Digite a chave para definir um valor padrão: ')
        valor_padrao = input('Digite o valor padrão: ')
        valor_existente = dicionario.setdefault(chave, valor_padrao)
        print(f"O valor para a chave '{chave}': {valor_existente}")

    elif opcao == '3':
        novos_pares = input('Digite os novos pares chaves-valor'\
                            'no formato chave1:valor1, chave2:valor2: ')
                            
        novos_pares_lista = novos_pares.split(',')
        novos_dados = {}

        for par in novos_pares_lista:
            chave, valor = par.split(':')
            novos_dados[chave] = valor
        dicionario.update(novos_dados)
        print(f'Dicionário atualizado: {dicionario}')

    
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