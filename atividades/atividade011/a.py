# Faça um programa que peça 3 valores, depois calcule e imprima  a soma e a multiplicação desses valores. 

# cria a classe
class Calcular:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

# setters edita os valores
    def set_a(self, valor1):
        self._a = valor1
    
    def set_b(self, valor2):
        self._b = valor2

    def set_c(self, valor3):
        self._c = valor3

# getters pegam os valores para ver
    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b

    def get_c(self):
        return self._c

# metodo para multiplicar
    def multiplicar(self):
        multiplicacao = self._a * self._b * self._c
        return multiplicacao
    
# metodo para somar
    def somar(self):
        soma = self._a + self._b + self._c
        return soma

# entrada de dados
valor1 = int(input('Digite o 1°: '))
valor2 = int(input('Digite o 2°: '))
valor3 = int(input('Digite o 3°: '))

# chama a classe e adiciona os valores
contas =  Calcular(0, 0, 0)
contas.set_a(valor1)
contas.set_b(valor2)
contas.set_c(valor3)

# chamada de metodos
resultado_soma = contas.somar()
resultado_multiplicacao = contas.multiplicar()

print(resultado_multiplicacao, resultado_soma)