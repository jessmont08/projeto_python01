import os

agenda = {'maddie' : '988434457',
          'margo' : '9984935815',
          'lia' : '984657588',
          'guel' : '9856475466',
          'annie' : '9865765988',
          'sophia' : '9896589878',
          'jess' : '9896678668'
}

while True:
    os.system('cls')

    print('-' * 90)
    print('\nAgenda de contatos: ')
    for nome, telefone in agenda.items():
        print(f'{nome} : {telefone}')
    print('=' * 90)

    if 'guel' in agenda:
        print('Verificando se o usuário Guel está na agenda.')
        print('Guel está na agenda.')
    else:
        print('Guel não está na agenda.')

    print()

    if 'annie' not in agenda:
        print('Verificando se "Annie" não está na agenda.')
        print('"Annie" não está na agenda.')

    else:
        print('"Annie" está na agenda.')

        print('-' * 90)
        print()

    print('Menu de opções.')
    print('1. Adicionar um contato.')
    print('2. Remover um contato.')
    print('3. Verificar um contato especifico.')
    print('4. Mostrar agenda.')
    print('5. Sair')

    opcao = input('Escolha uma opção.')

    if opcao == '1':
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        agenda[nome] = telefone
        print(f'Contato {nome} : {telefone} adicionado.')

    elif opcao == '2': 
        nome = input('Digite o nome que deseja remover: ')
        if nome in agenda: 
            del agenda[nome]
            print(f'O {nome} foi removido.')
        else:
            print('O contato não existe.')

    elif opcao == '3': 
        nome = input('Digite o contato  que deseja encontrar: ')

        if nome in agenda: 
            print(f'Contato existe: {nome}: {agenda[nome]}')
        else:
            print('O contato não foi encontrado.')

    elif opcao == '4':
        print('\nAgenda de contatos.')
        print(agenda)

    elif opcao == '5': 
        print('Saindo...')
        break

    else:
        print('Opção ínvalida.')

    input('Pressione enter para continuar...')