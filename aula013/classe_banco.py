import os


class Banco():
    def __init__(self, nome= '', agencia=0, conta=0, cpf=0, 
                 conta_corrente=0, poupanca=0):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.cpf = cpf
        self.conta_corrente = conta_corrente
        self.poupanca = poupanca

    
    def deposito(self, valor):
        escolha = input(
            'Conta corrente (cc) ou Poupança (po)'
        ).lower().strip()

        if escolha == 'cc':
            print(f'Valor do depósito: (+)R${valor}')
            print(f'Saldo anterior (cc): R${self.conta_corrente}')
            self.conta_corrente += valor
            print(f'\tSaldo atual na Conta Corrente: R${self.conta_corrente}')
            print('=' * 90)
        
        elif escolha == 'po':
            print(f'\nValor do deposito: (+)R{valor}. ')
            print(f'\Saldo anterior na Poupança: R${self.poupanca}.')
            self.poupanca += valor
            print(f'\tSaldo atual na Poupança: R${self.poupanca}')
            print('=' * 90)

        else:
            print('Opção ínvalida.')

    def saque(self, valor):
        escolha = input(
            'Conta corrente (cc) ou Poupança (po)'
        ).lower().strip()

        if escolha == 'cc':
            print(f'Valor sacado: (-)R${valor}')
            print(f'Saldo anterior (cc): R${self.conta_corrente}')
            self.conta_corrente -= valor
            print(f'\tSaldo atual na Conta Corrente: R${self.conta_corrente}')
            print('=' * 90)

        elif escolha == 'po':
            print(f'\nValor sacado: (+)R{valor}. ')
            print(f'\Saldo anterior na Poupança: R${self.poupanca}.')
            self.poupanca -= valor
            print(f'\tSaldo atual na Poupança: R${self.poupanca}')
            print('=' * 90)

        else:
            print('Opção ínvalida.')

os.system('cls')

print('Digite os dados para criar uma nova conta: ')
nome = input('Nome: ')
agencia = int(input('Agência: '))
conta = int(input('Número da conta:'))
cpf = int(input('CPF: '))
conta_corrente = float(input('Saldo inicial na conta corrente: '))
poupanca = float(input('Saldo inicial na poupança: '))

correntista = Banco(nome, agencia, conta, cpf, conta_corrente, poupanca)

print('=' * 90)
print('Movimentação Bancária.')
print('=' * 90)

opcao = input('Depósito ou saque (D/S)? ').upper().strip()

if opcao == 'D':
    valor = float(input('Digite o quanto deseja depositar: '))
    correntista.deposito

elif opcao == 'S':
    valor = float(input('Digite o quanto deseja sacar: '))
    correntista.saque

else:
    print('Opção ínvalida.')
