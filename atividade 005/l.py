# Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake).
# O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.

import os

os.system('cls')

nome = 'jessica rocha'
senha = 12345

while (True):
    nome1 = str(input('Nome: ')).lower()
    senha2 = int(input('Senha: '))

    if (nome1 != nome) or (senha != senha2):    
        print('Invalido.')
        continue
    else:
        print(f'Bem vindo ao sistema, {nome1}')
        break
         
    print()