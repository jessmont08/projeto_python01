import os
import csv


class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo, agencia, tipo_conta):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.agencia = agencia
        self.tipo_conta = tipo_conta

def obter_conta_dados():
    numero_conta = int(input('Digite o número da contas: '))
    nome_titular = input('Digite o nome do titular: ')
    saldo = float(input('Digite o saldo inicial da contas: '))
    agencia = int(input('Digite a agência da contas: '))
    tipo_conta = input('Digite o tipo da contas: ')
    
    return ContaBancaria(numero_conta, nome_titular, saldo, agencia, tipo_conta)

contas = []


while True:
    conta = obter_conta_dados()
    contas.append({
        'numero_conta' : conta.numero_conta,
        'nome_titular' : conta.nome_titular,
        'saldo' : conta.saldo,
        'agencia' : conta.agencia,
        'tipo_conta' : conta.tipo_conta
        })

    continuar = input('Deseja adicionar mais contas? (s/n): ').lower()
    if continuar != 's':
        break

pasta = 'arquivo_csv/contas/'

os.makedirs(pasta, exist_ok=True)

arquivo = 'arquivo_csv/contas/contas.csv'

with open(arquivo, mode='w', newline='') as conta:
    fieldnames = ['numero_conta', 'nome_titular', 
                  'saldo', 'agencia', 'tipo_conta']
    
    writer = csv.DictWriter(conta, fieldnames= fieldnames, delimiter=';')

    writer.writeheader()
    for registro in contas:
        writer.writerow(registro)

print(f'As informações das contas foram salvas em {arquivo}')