
def cadastrar_aluno():

    cadastro = {}

    while True: 
        escolha = input('Deseja adicionar alunos? Digite s/n: ')

        if escolha == 's':
            nome = input('Digite o nome: ')
            matricula = int(input('Digite o número de matrícula: '))
            data_nasc = input('Digite a data de nascimento (xx/xx/xx): ')

            cadastro[matricula] = {'nome': nome, 'data de nascimento': data_nasc}
            print('Aluno cadastrado.')

        elif escolha == 'n' :
            print('Saindo.')
            break

        else: 
            print('Digite s ou n.')

    return cadastro

cadastro = cadastrar_aluno()