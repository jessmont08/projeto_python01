import os


os.system('cls')


def empacotar(*lista_numeros):
    print(f'Empacotados: {lista_numeros}')
    for i in lista_numeros:
        print(f'Empacotado: {i}')

empacotar(1, 2, 3, 4, 5)

def desempacotar(a, b, c, d, e):
    print('Desempacotar: ')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'd = {d}')
    print(f'e = {e}')

listar_numeros = [1, 2, 3, 4, 5]
desempacotar(*listar_numeros)

def empacotar_dicioario(*dados_dicionario): 
    print(f'Dados do dicionário: {dados_dicionario}')
    for k, v in dados_dicionario.items():
        print(f'Chave: {k}, valor: {v}')

print('-' * 90)
print('- Dicionário.')
empacotar_dicioario(nome= 'juninho', idade= 70, peso= 70.5)
def desempacotar_dicionario(nome, peso, idade):
    print(f'Nome = {nome}.')
    print(f'Peso = {peso}.')
    print(f'Idade = {idade}.')

dicionario = dict(nome = 'Maria', idade = 70, peso = 70.5)
desempacotar(**dicionario)
print()