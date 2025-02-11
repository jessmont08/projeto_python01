def exibir_resultado(estudantes):
    for estudante in estudantes:
        print(f'\nnome: {estudante.nome}')
        print(f'Idade: {estudante.idade}')
        print(f'Média: {estudante.media():.2f}')
        print(f'Resultado: {estudante.resultado()}')