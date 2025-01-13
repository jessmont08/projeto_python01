import os

os.system('cls')

armazenamento = {}

for i in range(1, 6):
    ferramentas = str(input('Digite o nome da ferramenta: '))
    descricao = str(input('Digite o material da ferramenta: '))

    # manda pro armazenamento
    armazenamento[ferramentas] = descricao

print(armazenamento)

while True:
    alteracao = str(input('Deseja alterar alguma descrição? Digite s ou n: ')).strip().lower()

    if alteracao == 's':
        valor_alterado = str(input('Digite a descrição a ser alterada: '))
        if valor_alterado in armazenamento:
            novo_valor = input('Digite a nova descrição: ')

            armazenamento[ferramentas] = novo_valor

        else:
            print("Não existe essa descrição.")
        
    elif alteracao == 'n':
        print('Nenhuma alteração.')
        break

    else:
        print('Digite s ou n.')

# conta quantos pares tem no armazenamento.
valor_atual = len(armazenamento)

print(f'No dicionário tem atualmente {valor_atual} itens.')

# mostra os valores, sem as chaves.
for descricao in armazenamento.values():
    print(f'As descrições atuais são: {descricao}')

# se fosse utilizado somente o armazenamento sem items apareceria somente as chaves.
armazenamento_ordenado = sorted(armazenamento.items())
print(f'O armazenamento ordenado é {armazenamento_ordenado}. ')

# split tem a função de separar os nomes em dois e len conta quantos teve.
# se o contador estiver dentro da iteracao ele sempre vai voltar pro zero e nunca vai somar.

relatorio = 0
for ferramentas in armazenamento: 
    quantidade = ferramentas.split()
    contagem = len(quantidade)

    if contagem >= 2:
        relatorio += 1

print(f'Há {relatorio} ferramenta/s que contêm mais de uma palavra no nome.')