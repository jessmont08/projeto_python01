import os

os.system('cls')

informacoes = {'nome': 'john', 'idade' : '40', 'peso': '80',
               'altura' : '1.70'} 

while True:
    print('Menu de opções.')
    print('1. Mostrar todas as chaves e valores.')
    print('2. Alterar o valor de uma chave.')
    print('3. Excluir algum valor.')
    print('4. Exibir apenas nome e altura.')
    print('5. Sair.')

    opcao = input('Escolha de 1 a 5: ')

    if opcao == '1':
        for keys, values in informacoes:
            print(f'{keys}: {values}')

    if opcao == '2':
        alterar = input('Digite o que deseja alterar: ').strip().lower()
        if alterar in informacoes:
            alterando = input('Digite o novo valor: ')

            informacoes[alterar] = alterando

    if opcao == '3':
        deletar = input('Digite o valor que deseja excluir: ').strip().lower()
        if deletar in informacoes:
            del informacoes[deletar]

    if opcao == '4':
        print(informacoes['nome'])
        print(informacoes['altura'])

    if opcao == '5':
        print('Saindo...')
    break