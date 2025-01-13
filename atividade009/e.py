import os

os.system('cls')

cadastro = {}

for i in range(1, 4):
    nome = str(input('Digite o nome do aluno: '))
    idade =(input('Digite a data de nascimento do aluno: '))
    numero_matricula = int(input('Digite o número de matrícula: '))

    cadastro[numero_matricula] = {'nome': nome, 'data de nascimento': idade}

print(cadastro)

while True:
    alteracao = str(input('Deseja alterar algo? Digite s ou n: ')).strip().lower()
        

    if alteracao == 's':
        aluno_alterado = int(input('Digite o número da matrícula do'
                            '\naluno que deseja alterar: '))
        
        
        if aluno_alterado in cadastro:
            item_alterado = input('Digite o que quer alterar:').strip().lower()
        
            if item_alterado in cadastro[aluno_alterado]:
                novo_item = input('Digite a alteração: ').strip().lower()
        
                if item_alterado == idade:
                    novo_item = int(idade)
                
                cadastro[aluno_alterado][item_alterado] = novo_item

            else:
                print('Esse número não está cadastrado.')

    elif alteracao == 'n':
        break

    else:                  
        print('Digite s ou n.')

print('Os alunos cadastrados são: ')

for keys, values in cadastro.items():
    print(f'O número de matricula é {keys}')
    print(f'O nome do aluno é {values["nome"]}')
    print(f'A data de nascimento do aluno é {values["data de nascimento"]}')

alunos_2000 = 0
for dados in cadastro.values():
    cont_idade = dados["data de nascimento"].split('/')
    ano_nasc = int(cont_idade[2])

    if ano_nasc >= 2000:
        alunos_2000 += 1

print(f'Há {alunos_2000} nascidos após 2000.')

matricula_impar = 0
for matricula in cadastro:
    if matricula % 2 != 0:
        matricula_impar += 1
print(f'{matricula_impar} matrículas são ímpares.')
