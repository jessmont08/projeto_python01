def buscar_cadastro(cadastro): 
    procura = int(input('Digite o número de matrícula'
                    '\ndo aluno: '))
    
    if procura in cadastro:
        print(f'O nome do aluno é {cadastro[procura]["nome"]}.')
        print(f'O nome do aluno é {cadastro[procura]["data de nascimento"]}.')
        print(f'O nome do aluno é {procura}.')

    else:
        print('Aluno não cadastrado.')