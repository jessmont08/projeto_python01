import os


os.system('cls')

# ao menos 4 elementos/funcoes, usuario insirar chave e valores, chaves devem ser unicas, no final deve ser exibido o dicionario em ordem no final


dicionario = dict()

for i in range(1, 5):
    chave = input(f'Digite a {i}º chave: ').strip().lower()
    valor = input(f'Digite o {i}º valor: ').strip().lower()
    dicionario[chave] = valor

print(dicionario)