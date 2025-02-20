import os


os.system('cls')

dicionario = dict()

for i in range(1, 6):
    cor = input(f'Digite a {i}º cor desejada: ').strip().lower()
    descricao = input(f'Digite a descrição da cor {i}º: ').strip().lower()

    dicionario[cor] = descricao

print('=' * 90)
print(f'O dicionário atual é:\n {dicionario}')
print('.' * 90)
 
while True:
    escolha = input('Alterar alguma cor? Digite sim ou '
                    '\n"s" para sair: ').strip().lower()
    
    if escolha == 's': 
        break
    else:
        cor_alterada = input('Digite a cor que deseja alterar: ')
        if cor_alterada in dicionario:
            cor_nova = input('Digite a alteração: ')
            del dicionario[cor_alterada]
            dicionario[cor_alterada] = cor_nova

print('=' * 90)
print(f'O dicionário atual é:\n {dicionario}')
print('.' * 90)

while True:
    escolha2 = input('Deseja adicionar alguma cor? Digite sim ou'
                    '\n"s" para sair: ').strip().lower()
    
    if escolha == 's':
        break

    else:
        cores_entrada = input('Digite a cor que deseja adicionar'
                             '\ndesta forma: cor:descrição, cor2:descrição: ')
        cores_novas = cores_entrada.split(',')
        dicionario.update(cores_novas)


print('=' * 90)
print(f'O dicionário atual é:\n {dicionario}')
print('.' * 90)

dicionario_organizado = sorted(dicionario)
print(f'O alfabeto ordenado é {dicionario_organizado}')

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

for letra in alfabeto:
    num = 0
    for palavra in dicionario_organizado:
        if letra in palavra[0]:
            num =+ 1
        if num == 0:
            continue 

        else:
            print(f'Tem {num} cores com a letra {letra}')