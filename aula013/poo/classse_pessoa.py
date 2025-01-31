import os

class Pessoa:
    def __init__(self, nome, cpf, nascimento, cep, cidade, estado):
        #inicializando atributos

        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.cep = cep
        self.cidade = cidade
        self.estado = estado

os.system('cls')
print('-' * 90)
nome = input('Digite o nome: ')
cpf = input('Digite o CPF: ')
nascimento = input('Digite a data de nascimento: ')
cep = input('Digite o CEP: ')
cidade = input('Digite a cidade: ')
estado = input('Digite o estado: ')

pessoa1 = Pessoa(nome, cpf, nascimento, cep, cidade, estado)

print('-' * 90)
print('\nInformações da pessoa: ')
print('=' * 90)
print(f'Nome: {pessoa1.nome}')
print(f'CPF: {pessoa1.cpf}')
print(f'Nascimento: {pessoa1.nascimento}')
print(f'CEP: {pessoa1.cep}')
print(f'Cidade: {pessoa1.cidade}')
print(f'Estado: {pessoa1.estado}')
print('=' * 90)