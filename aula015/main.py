import os
from escola.cadastro.cadastro import cadastrar_estudante
from escola.resultado import exibir_resultados

def main():
    os.system('cls')
    print('Cadastro de alunos.')
    print('-' * 90)

    estudantes = []

    while True:
        estudante = cadastrar_estudante
        estudante.append(estudante)

        continuar = input('Deseja cadastrar outro estudante? (s/n):')
        if continuar != 's':
            break

        exibir_resultados(estudantes)
    
if __name__ == '__main__':
    main()
