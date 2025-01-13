import os

os.system('cls')

cadastro = {}

for i in range(1, 3):
    nome = str(input('Digite o nome do aluno: '))
    idade = int(input('Digite a idade do aluno: '))
    numero_matricula = int(input('Digite o número de matrícula: '))

    cadastro[numero_matricula] = {'nome': nome, 'idade': idade}

print(cadastro)

while True:
    alteracao = str(input('Deseja alterar algo? Digite s ou n: '))

    if alteracao == 's':
        aluno_alterado = int(input('Digite o número da matrícula do'
                            '\naluno que deseja alterar: '))
        
        if aluno_alterado in cadastro:
            item_alterado = input('Digite o que quer alterar:')
        else:
            print('Esse número não está cadastrado.')

            if item_alterado in cadastro[aluno_alterado]:
                novo_item = input('Digite a alteração: ')
                if item_alterado == idade:
                    novo_item = int(idade)
                
                    cadastro[aluno_alterado][item_alterado] = novo_item


    elif alteracao == 'n':
        break

    else:                  
        print('Digite s ou n.')