from escola.estudante import Estudante

def cadastrar_estudante():
    nome = input('Digite o nome do aluno: ')
    idade = int(input(f'Digite a idade do/a {nome}: '))

    estudante = Estudante(nome, idade)

    while True:
        try:
            nota = float(input(f'Digite as notas de {nome} (ou 0 para sair): '))
            if nota == 0:
                break
            estudante.adicionar_notas(nota)

        except ValueError:
            print('Por favor, digite uma nota válida.')

    return estudante