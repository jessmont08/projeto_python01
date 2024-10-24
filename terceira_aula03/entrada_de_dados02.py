# importa bibliotecas
import os

import datetime

# puxar comando da biblioteca
os.system('cls')

 # titulo do sistema
print('-' * 80)
print('CADASTRO DE ENDEREÇO')
print('=' * 80)

# pedido de entrada do usuario
nome = input('entre com seu nome: ')
idade = input('entre com sua idade: ')
cpf = input('entre com seu CPF: ')

# pedido de f string 
nascimento = int(input ('entre com seu ano de nascimento: '))
estado = str(input('entre com seu estado:'))
cidade = str(input('entre com sua cidade: '))
bairro = str(input('entre com seu bairro: '))
rua = str (input('entre com sua rua: '))
numero = int (input('entre com o numero da sua casa: '))
cep = int(input('entre com seu cep: '))

# puxar comando da biblioteca
ano_atual = datetime.datetime.now ( ).year
idade = int(ano_atual) - nascimento

# titulo da saida de dados
print('-' * 80)
print('SAIDA DE DADOS')
print('=' * 80)

# saida de dados
print('N0ME: ' , nome)
print('IDADE: ' , idade)
print('CPF: ' , cpf) 

# saida das  f string
print(f'{nome}, você tem {idade} anos <3')
print(f'CEP: {cep}')
print(f'ESTADO: {estado}')
print(f'CIDADE: {cidade}')
print(f'BAIRRO: {bairro}')
print(f'RUA: {rua}')
print(f'CEP: {cep}')

print('=' * 50)