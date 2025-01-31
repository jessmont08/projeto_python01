import os
import csv

os.system('cls')

arquivo = 'arquivos_csv/gravacao/alunas.csv'
nome_para_apagar = input('Digite o nome que deseja apagar: ')

# lendo os dados do arquivo
with open(arquivo, 'r') as arquivos_csv:
    leitura = csv.DictReader(arquivos_csv, delimiter=';')
    cadastro = list(leitura)

# vrifica se o nome eiste e apagando o registro
apagado = False
novo_cadastro = [registro for registro in cadastro \
                 if registro['nome'] != nome_para_apagar ]

if len(novo_cadastro) > len(cadastro):
    apagado = True

# reescrevendo com os dados atualizados 
    with open(arquivo, 'w', newline= '') as arquivo_csv:
        campos = ['nome', 'telefone', 'cidade']
        escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')

        escrever.writeheader()
        escrever.writerows(novo_cadastro)

print('=' * 90)
if apagado:
    print(f'Registro com nome {nome_para_apagar} apagado com sucesso.')
else:
    print(F'Registro com o nome {nome_para_apagar} não encontrado.')
print('-' * 90)