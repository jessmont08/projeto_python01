from oftamologia.consultorio import Paciente
from oftamologia.cadastro import cadastrar_paciente

nome, idade, numero, telefone, ala, pressao_ocular, procedimento, problemas_clinicos = cadastrar_paciente()

paciente = Paciente(nome, idade, numero, telefone, ala, pressao_ocular, procedimento, problemas_clinicos)
paciente_cadastrado = cadastrar_paciente()

if paciente_cadastrado is not None:
    # Se o paciente foi cadastrado, chama o método avaliacao()
    paciente_cadastrado.avaliacao()
    print(paciente_cadastrado)  # Exibe os dados do paciente
else:
    print("Nenhum paciente foi cadastrado.")