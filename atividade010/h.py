# Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir a média de altura  e peso de seus clientes.
# Faça um programa que pergunte a cada um dos clientes da academia seu código, nome, altura e peso. Após esse cadastramento, 
# seu programa deverá listar os dados dos clientes e a média. Para sair do programa o usuário deverá digitar o valor zero(0). 
# O número de clientes é indefinido. 

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

def calcular_media(academia):
    if not academia:
        return 0, 0

    contagem = len(academia)
    soma_peso = sum(cliente["peso"] for cliente in academia.values())
    soma_altura = sum(cliente["altura"] for cliente in academia.values())

    media_peso = soma_peso / contagem
    media_altura = soma_altura / contagem

    return media_peso, media_altura

def listar_clientes(academia):
    for keys, values in academia.items():
        print('=' * 90)
        print(f'O nome do cliente é {keys}')
        print(f'O peso é {values["peso"]}kg.')
        print(f'A altura é {values["altura"]}m.')
        print('=' * 90)

academia = cadastrar_clientes()
media_peso, media_altura = calcular_media(academia)
listar_clientes(academia)

print('=' * 90)
print(f'A média dos clientes de altura é'
      f'\né {media_altura}m.')
print(f'A média dos clientes de peso é'
      f'\né {media_peso}kg.')
print('=' * 90)