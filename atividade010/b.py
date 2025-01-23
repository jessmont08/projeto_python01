import os


os.system('cls')


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

# main
resultado = cadastrar_aluno()
exibir_aluno(resultado)