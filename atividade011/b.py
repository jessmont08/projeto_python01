# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.
from datetime import datetime

class Idade:
    def __init__(self, anodenascimento):
        self._anodenascimento = anodenascimento

    def set_anodenasimento(self, datadenascimento):
        self._c = datadenascimento

    def get_anodenascimento(self):
        return self._anodenascimento
    
    def calcular_idade(self):
        hoje = datetime.today()
        ano = hoje.year

        datadeaniversario = datetime.strptime(self._anodenascimento, "%d/%m/%Y")
        anoaniversario = datadeaniversario.year
        idade = ano - anoaniversario

        return idade

datadonascimento = input('Digite sua data de nascimento: ')
calculo = Idade(0)
calculo.set_anodenasimento(datadonascimento)
resposta = calculo.calcular_idade()
print(resposta)