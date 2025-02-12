


def cadastrar_paciente():
    while True: 

        nome = input('Digite o nome do paciente ou 0 para sair: ')
        
        
        if nome == '0':     
            print('Saída solicitada.')
            break
        
        else:
            idade = int(input(f'Digite a idade do paciente {nome}: '))
            numero = int(input('Digite o número da consulta: '))
            telefone = int(input('Digite o telefone do responsável: '))
            ala = input('Digite o ala do paciente: ')
            pressao_ocular = float(input('Digite a média da pressão'
                                            '\nocular do paciente: '))
            procedimento = input('Digite o procedimento que deseja fazer: ')
            problemas_clinicos = input('Possui diabetes ou hipertensão? (sim/não): ')

            return nome, idade, numero, telefone, ala, pressao_ocular, procedimento, problemas_clinicos



