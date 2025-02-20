import os

os.system('cls')

vinhos = {}

for i in range(1, 3):
    numeracao = str(input('Entre com o numéro do vinho: '))
    tipo = str(input('Entre com o tipo do vinho: '))
    teor_alcoolico = float(input('Entre com o teor alcoolico: '))
    safra = int(input('Entre com o ano de safra: '))

# numeracao é definida como a chave principal
    vinhos[numeracao] = {'tipo': tipo, 'teor alcoolico': teor_alcoolico, 'safra': safra}

print('-' * 90)
print('Os vinhos no adega são: ')
print('=' * 90)

# sem o items nao consegue acessar o dict
for keys, values in vinhos.items():
    print(f'O número do vinho é {keys}')
    # chaves com letra maiuscula sao diferentes das minusculas
    print(f'O tipo do vinho é {values["tipo"]}')
    print(f'O teor alcoólico do vinho é {values["teor alcoolico"]}')
    print(f'A safra é de {values["safra"]}')
    print('=' * 90)

while True:
    alteracao = input('Quer alterar algo? Digite s ou n: ').strip().lower()

    if alteracao == 's':
        item_alterado = input('Digite o número do vinho'
                              '\nque deseja alterar: ')
        

        if item_alterado in vinhos:
            subitem_alterado = input('Digite o que quer alterar: ').strip().lower()

            #  verifica se a numeração do vinho tem o valor e/ou chave do subitem alterado
            if subitem_alterado in vinhos[item_alterado]:
                atualizacao = input('Digite a alteração: ')

                # faz o casting da nova informacao
                if subitem_alterado == 'teor alcoolico':
                    atualizacao = float(atualizacao)
                if subitem_alterado == 'safra':
                    atualizacao = int(atualizacao)
                    
                # entra primeiro na chave principal e depois na chave e/ou que deseja alterar
                vinhos[item_alterado][subitem_alterado] = atualizacao


        else:
            print('Esse item não está na adega!')

    elif alteracao == 'n':
        break

    else:
        print('Digite s ou n.')

print(f'O sistema atualizado é: ')
print(vinhos)

# o contador sempre deve estar fora porque se nao reconta
alcool_alto = 0
safra_nova = 0

# items tem a funcao de ser possivel acessar os valores, sem ele, da erro porque nao consegue acessar os valores
for keys, values in vinhos.items(): 
    if values["teor alcoolico"] >= 12:
        alcool_alto += 1

print(f'Há {alcool_alto} vinhos com o teor'
      '\nalcoólico maior que 12%' )


for keys, values in vinhos.items():
    if values["safra"] >= 2015:
        safra_nova += 1

print(f'Há {safra_nova} vinhos com a safra' 
      '\nfeita depois de 2015.' )

# o sorted tem a função de ordenar e ai abre o key para acessar a chave, os item um tema funcao de acessar cada par e o segundo mostra a chave que
# que vai ser usada no sorted, nesse caso, a numeracao
vinhos_ordenados = sorted(vinhos.items(), key= lambda item: item[0])

print('Os vinhos na adega são: ')

for vinhos in vinhos_ordenados:
    print(vinhos)