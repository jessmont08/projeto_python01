def exibir_aluno(cadastro):
    if len(cadastro) ==  0:
        print('Nenhum aluno cadastrado.')
        print('-' * 90 )
        print()
    for chaves, valores in cadastro.items(): 
        print('=' * 90 )
        print(f'O número da matrícula é {chaves}')
        print(f'O nome do aluno é {valores["nome"]}')
        print(f'O nascimento do aluno é {valores["data de nascimento"]}')
        print('-' * 90 )
        print()