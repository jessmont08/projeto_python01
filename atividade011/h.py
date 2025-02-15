# Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.
class Tabuada:
    def __init__(self, inteiro):
        self._inteiro = inteiro

    def set_inteiro(self, numero):
        self._inteiro = numero

    def get_inteiro(self):
        return self._inteiro
    
    def calcular_tabuada(self):
        for x in range(11):
            multiplicacao = int(self.get_inteiro()) * x
            print(f'{self.get_inteiro()} x {x} = {multiplicacao}')

numero = input('Digite o valor: ')
calculos = Tabuada(numero)

calculos.calcular_tabuada()