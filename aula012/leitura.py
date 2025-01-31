import csv
import os

#nome do arquivo
arquivo = 'arquivos_csv/gravacao/alunas.csv'

# listar para armazenr os dados
lista = []

# abrindo arquivo csv para leitura
with open(arquivo, 'r') as arquivos_csv:
    # criando um leitor de CSV que lê o arquivo como dicionário
    leitura = csv.DictReader(arquivos_csv, delimiter=';')

    # Iterando sobre cada linha (registro) no arquivo csv e adicionando na lista
    for linha in leitura:
        lista.append(linha)
    
os.system('cls')
print('=' * 90)
print('nome\ttelefone\tcidade')
print('-' * 90)

# exibindo lista resultante 
for registro in lista:
    flag = 0
    for k, v in registro.items():
        print(v, end='\t')
        flag += 1
        if flag == 3:
            print()

print('-' * 90)