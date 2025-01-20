import os

os.system('cls')

filmes = dict()

for i in range(1, 2):
    titulo = input('Entre com título do filme: ')
    genero = input('Entre com o genero do filme: ')
    duracao = input('Entre com a duração(xx:xx:xx): ')
    classificacao_indica = input('Entre com a classificação indicativa: ')

    filmes[titulo] = {'genero': genero, 'duração': duracao,
                      'classificação indicativa': classificacao_indica}

while True:
    alterar = input('Deseja alterar algo? Digite s ou n: ')

    if alterar == 's':
        alterando_filme = input('Digite o título do filme que'
                                '\nquer alterar: ')
        if alterando_filme in filmes:
            alterando = input('Digite o que quer alterar'
                              '\n(título, genero, duração e etc)')
            if alterando in filmes[alterando_filme]:
                alteracao = input('Digite a alteração: ')

                filmes[alterando_filme][alterando] = alteracao

    elif alterar == 'n':
        break

    else:
        print('Digite s ou n.')

filmes_ordenados = dict(sorted(filmes.items(), key= lambda item:item[0]))

filmes_longos = 0
for values in filmes.values():
    separador = values['duração'].split(':')
    horas = int(separador[0])

    if horas[0] >= 2:
        filmes_longos += 1

print(f'{filmes_longos} são maiores que duas horas.')

filmes_livres = 0
for keys, values in filmes.items():
    if values['classificação indicativa'] == 'livre':
        filmes_livres += 1

print(f'Há {filmes_livres} com a indicação "livre".')