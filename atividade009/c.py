import os

os.system('cls')

dicionario = {}

for i in range(1, 4):
    ferramentas = str(input('Digite o nome da ferramenta: '))
    descricao = str(input('Digite o material da ferramenta: '))
    dicionario[ferramentas] = descricao

print(dicionario)

while True:
    alteracao = str(input('Deseja alterar alguma descrição? Digite s ou n: ')).strip().lower()

    if alteracao == 's':
        valor_alterado = str(input('Digite a descrição a ser alterada: '))
        novo_valor = input('Digite a nova descrição: ')

        # troca somente o valor que foi colocado em valor alterado.
        dicionario[ferramentas] = novo_valor

    elif alteracao == 'n':
        print('Nenhuma alteração.')
        break

    else:
        print('Digite s ou n.')

# conta quantos pares tem no dicionario.
valor_atual = len(dicionario)

print(f'No dicionário tem atualmente {valor_atual} itens.')

# mostra os valores, sem as chaves.
descricao = dicionario.values()
print(f'As descrições atuais são: {descricao}')

# se fosse utilizado somente o dicionario sem items apareceria somente as chaves.
dicionario_ordenado = sorted(dicionario)
print(f'O armazenamento ordenado é {dicionario_ordenado}. ')

# preciso terminar
# split tem a função de separar os nomes em dois e len conta quantos teve.
# se o contador estiver dentro da iteracao ele sempre vai voltar pro zero

relatorio = 0
for ferramentas in dicionario: 
    quantidade = ferramentas.split()
    contagem = len(quantidade)

    if contagem >= 2:
        relatorio += 1

print(f'Há {relatorio} ferramenta/s que contêm mais de uma palavra no nome.')