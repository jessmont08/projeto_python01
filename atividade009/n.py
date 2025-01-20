import os

os.system('cls')

loja = {}

for i in range(1, 3):

    nome = input('Digite o nome do produto: ')
    categoria = input('Digite a categoria do produto: ')
    preco = float(input('Digite o preço do produto: '))
    desconto = float(input('Digite o desconto do produto: '))

    loja[nome] = {'categoria': categoria, 'preço': preco, 'desconto': desconto}

while True: 
    alterar_preco = input('Deseja alterar o preço de algum produto?'
                          '\nDigite s ou n: ').strip().lower()
    
    if alterar_preco == 's':
        alterando = input('Digite o nome do produto que'
                          '\ndeseja alterar: ').strip().lower()
        
        if alterando in loja:
            alteracao = input('Digite a alteração: ')
            calculo_desc = alteracao - (alteracao * desconto / 100)
            loja[alterando]['preço'] = calculo_desc
        else:
            print('Esse produto não está cadastrado. ')

    elif alterar_preco == 'n':
        break

    else:
        print('Digite s ou n.')

baratos = 0
eletronicos = 0

for values in loja.items():
    if loja['preço'] >= 50:
        baratos += 1
    if loja['categoria'] == 'eletrônico':
        eletronicos += 1

for keys, values in loja.items():
    print(f'{keys}: {values}')
    
print(f'Há {baratos} itens com o preço abaixo de R$50.00 reais.')
print(f'Há {eletronicos} itens eletrônicos no estoque.')

