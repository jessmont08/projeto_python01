import os

# importar a biblioteca csv
import csv

# criando uma lista de dicts, cada dict é uma linha

lista = [{'nome': 'agatá', 'telefone': '(32)988-434454', 'cidade' : 'juiz de fora'},
         {'nome': 'bia', 'telefone': '(32)98843-4455', 'cidade' : 'juiz de fora'},
         {'nome': 'coly', 'telefone': '(32)98843-4456', 'cidade' : 'juiz de fora'},
         {'nome': 'isis', 'telefone': '(32)98843-4457', 'cidade' : 'juiz de fora'},
]

# caminho onde o arquivo csv será salvo 
pasta = 'arquivos_csv/gravacao'

# verifica se a pasta existe, se não existir, será criada
os.makedirs(pasta, exist_ok=True)

# nome para o arquivo csv gravar as informações
arquivo = 'arquivos_csv/gravacao/alunos.csv'

# caminho completo do arquivo csv 
caminho_arquivo = os.path.join(pasta, arquivo)

# abre o arquivo 'arquivo' no modo de escrita ('w')
# se o arquivo não existir, ele será criado; se existir será esvaziado
# newline = ' ': evita a adição de linhas em branco extras ao gravar o arquivo em algumas plataformas
# as arquivos_csv: atribui o objeto ao arquivo_csv para ser usado dentro do bloco with 
with open(arquivo, 'w', newline='') as arquivo_csv:

# campos = ['nome', 'telefone', 'cidade']: define a lista de nomes de campos
# (cabecalhos das colunas CSV)
    campos = ['nome', 'telefone', 'cidade']

    #writer = csv.DictWriter(arquivo_csv, fieldnames=campos):
    # Cria um objeto DictWriter que usará 'arquivo_csv' para gravar os campos.
    # fieldnames define a ordem dos campos no arquivo CSV.
    # delimiter=';': é o separador
    escrever = csv.DictWriter(arquivo_csv, fieldnames= campos, delimiter=';')

    # writer.writerheader(): Graa a liha de cabeçalho no
    # arquivo CSV usando os nomes de campos definidos em fieldnames.
    escrever.writeheader()

    # writer.writerows(lista): Grava todas as linhas da lista no arquivo CSV.
    # Cada dicionário em 'lista se torna uma linha no arquivo.
    escrever.writerows(lista)

os.system('cls')
# Exibe ua mensagem indicando que o arquio foi gravado com sucesso.
print(f'Arquivo {arquivo} gravado com sucesso!')