from escola.cadastro.cadastro import estudante

def cadastrar_estudante():
    nome = input('Digite o nome do aluno: ')
    idade = int(input(f'Digite a idade do/a {nome}: '))

    estudante = estudante(nome, idade)

    while True:
        try:
            nota = float(input(f'Digite as notas de {nome} (ou 0 para sair): '))
            if nota == 0:
                break
            estudante.adicionar_nota(nota)

        except ValueError:
            print('Por favor, digite uma nota válida.')

    return estudante