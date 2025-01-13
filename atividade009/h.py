import os

os.system('cls')

biblioteca = {}

for i in range(1, 3):
    titulo = str(input('Digite o nome do livro: '))
    autor = str(input('Digite o nome do autor: '))
    lancado_em = int(input('Digite o ano de lançamento: '))
    num_pag = int(input('Digite quantas páginas tem o livro: '))

    biblioteca[titulo] = {'autor': autor, 'ano de lançamento:': lancado_em,
                          'contagem de páginas: ': num_pag}
    
while True:
    alteracao = str(input('Quer editar alguma informação'
                          '\n já cadastrada? Digite s ou n: '))
    
    if alteracao == 's':
        livro_alterado = str(input('Digite o título do livro'
                                   '\n que deseja alterar: '))
        
        if livro_alterado in biblioteca:
            alterando = str(input('Digite o que deseja alterar (titulo,'
                                  '\n autor e etc): '))
        if alterando in biblioteca[livro_alterado]:
            novo_item = str(input('Digite a alteração: '))
             
            biblioteca[livro_alterado][alterando] = novo_item

    elif alteracao == 'n':
        break

    else:
        print('Digite s ou n.')

print(biblioteca)