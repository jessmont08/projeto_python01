import os


os.system('cls')

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
        
def buscar_cadastro(cadastro): 
    procura = int(input('Digite o número de matrícula'
                    '\ndo aluno: '))
    
    if procura in cadastro:
        print(f'O nome do aluno é {cadastro[procura]["nome"]}.')
        print(f'O nome do aluno é {cadastro[procura]["data de nascimento"]}.')
        print(f'O nome do aluno é {procura}.')

    else:
        print('Aluno não cadastrado.')
    
print('Buscando cadastro! ')
buscar_cadastro(cadastro)

