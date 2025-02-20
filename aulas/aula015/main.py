import os
from escola.estudante import Estudante
from escola.resultado import exibir_resultados
from escola.cadastro import cadastrar_estudante

def main():
    os.system('cls')
    print('Cadastro de alunos.')
    print('-' * 90)

    estudantes = []

    while True:
        estudante = cadastrar_estudante()
        estudantes.append(estudante)

        continuar = input('Deseja cadastrar outro estudante? (s/n):')
        if continuar != 's':
            break

    exibir_resultados(estudantes)
    
if __name__ == '__main__':
    main()
