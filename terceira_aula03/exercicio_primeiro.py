import os

import datetime

os.system('cls')

print('-' * 90)
print('CADASTRO ESCOLAR')
print('=' * 90)

nome = str(input('Nome do aluno: '))
idade = int(input('Idade do aluno: '))
cpf = int(input('Cadastro fisíco do aluno: '))
responsavel = str(input('Nome do respónsavel: '))
instituicao = str(input('Instituição do aluno: '))
ano_que_o_aluno_entrou = int(input('Ano que o aluno iniciou os estudos: '))
simade = int(input('Simade do aluno: '))

ano_atual = datetime.datetime.now( ).year
ano_que_o_aluno_entrou = int(ano_atual) - ano_que_o_aluno_entrou

print('-' * 90)
print('SAIDA DE DADOS')
print('=' * 90)

print(f'{nome} você estuda há {ano_que_o_aluno_entrou} anos!')
print(f'IDADE: {idade}')
print(f'CPF: {cpf}')
print(f'NOME DO RESPONSAVEL: {responsavel}')
print(f'INSTITUIÇÃO: {instituicao}')
print(f'NUMÉRO SIMADE: {simade}')

print('-' * 90)
