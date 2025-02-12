class Paciente:
    def __init__(self, nome, idade, telefone, ala, numero, pressao_ocular, procedimento, problemas_clinicos):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.ala = ala
        self.numero = numero
        self.pressao_ocular = pressao_ocular
        self.procedimento = procedimento
        self.problemas_clinicos = problemas_clinicos

    def avaliacao(self):
        if self.procedimento == 'cirurgia refrativa':
            print('Formando um QA para cirugia refrativa.')
            if self.pressao_ocular > 21 and self.problemas_clinicos == 'sim':
                print('Fator de risco, necessário avaliação presencial.')

    def __str__(self):
        return (f'Paciente: {self.nome}, Idade: {self.idade}'
                f'\nTelefone: {self.telefone}, \nAla: {self.ala}'
                f'\nNumero: {self.numero}, \nPressao Ocular: {self.pressao_ocular}'
                f'\nProcedimento: {self.procedimento}, Problemas: {self.problemas_clinicos}')
        
    
