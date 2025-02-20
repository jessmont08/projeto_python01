def exibir_resultados(estudantes):
    for estudante in estudantes:
        print('=' * 90)
        print(f'Nome: {estudante.nome}')
        print(f'Idade: {estudante.idade}')
        print(f'Média: {estudante.media():.2f}')
        print(f'Resultado: {estudante.resultado()}')
    print('=' * 90)