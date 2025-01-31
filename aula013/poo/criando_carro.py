import os

class Veiculo: 
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

os.system('cls')
print('-' * 90)
marca = input('Digite a marca do veiculo: ')
modelo = input('Digite o modelo do veiculo: ')
ano = input('Digite o ano do veiculo: ')
cor = input('Digite a cor do veiculo: ')

veiculo = Veiculo(marca, modelo, ano, cor)

print('-' * 90)
print('\nInformações do veículo.')
print('=' * 90)
print(f'A marca do veículo é: {veiculo.marca}')
print(f'O modelo do veículo é: {veiculo.modelo}')
print(f'O ano do veículo é {veiculo.ano}')
print(f'A cor do veículo é {veiculo.cor}') 
print('=' * 90)