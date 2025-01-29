import os

def cadastrar_clientes():
    academia = dict()
    while True:
        cliente = input('Digite o  nome do cliente ou 0'
                        '\npara sair: ')
        
        if cliente != '0':
            altura = float(input('Digite a altura: '))
            peso = float(input('Digite o peso: '))
            codigo = int(input('Digite o código: '))

        else:
            print('Saindo...')
            break

        academia[codigo] = {'cliente' : cliente,
                            'altura': altura,
                            'peso': peso}

        os.system('cls')
    return academia