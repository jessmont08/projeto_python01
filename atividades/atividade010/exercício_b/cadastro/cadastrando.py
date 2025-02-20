def cadastrar_aluno():

    cadastro = {}
    
    while True:
        nome = input('Digite o nome ou s para sair: ')
        print('-' * 90 )

        if nome != 's':
            datadenascimento = input('Digite a data de nascimento: ')
            print('-' * 90 )
            matricula = int(input('Digite o número de matrícula: '))
            print('-' * 90 )
            cadastro[matricula] = ({'nome' : nome,
                                    'data de nascimento' : datadenascimento})
        else:
            print('Saindo...')
            break
         
    return cadastro