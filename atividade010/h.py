# Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir a média de altura  e peso de seus clientes.
# Faça um programa que pergunte a cada um dos clientes da academia seu código, nome, altura e peso. Após esse cadastramento, 
# seu programa deverá listar os dados dos clientes e a média. Para sair do programa o usuário deverá digitar o valor zero(0). 
# O número de clientes é indefinido. 

def cadastrar_clientes():
    academia = dict()
    while True:
        cliente = input('Digite o  nome do cliente ou 0'
                        '\npara sair: ')
        
        if cliente != '0':
            altura = float(input('Digite a altura: '))
            peso = float(input('Digite o peso: '))

        else:
            print('Saindo...')
            break

    academia['nome'] = cliente
    academia['altura'] = altura
    academia['peso'] = peso

    return academia

def listar_clientes(academia):
    for keys, values in academia.items():
        print('=' * 90)
        print(f'O nome do cliente é {keys}')
        print(f'O peso é {values["peso"]}')
        print(f'A altura é {values["altura"]}')
        print('=' * 90)

def calcular_media(academia):
    contagem = len(academia)
    soma_peso = sum(cliente["peso"] for cliente in academia.values())
    soma_altura = sum(cliente["altura"] for cliente in academia.values())

    media_peso = soma_peso / contagem
    media_altura = soma_altura / contagem

    return media_peso, media_altura

academia = cadastrar_clientes()
listar_clientes(academia)
media_peso, media_altura = calcular_media(academia)
