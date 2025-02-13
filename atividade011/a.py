# Faça um programa que peça 3 valores, depois calcule e imprima  a soma e a multiplicação desses valores. 

class Calcular:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b

    def get_c(self):
        return self._c

    def get_a(self, value):
        self._a = value
    
    def get_b(self, value):
        self._b = value

    def get_c(self, value):
        self._c = value

    def multiplicar(self):
        multiplicacao = self._a * self._b * self._c
        return multiplicacao
    
    def somar(self):
        soma = self._a + self._b + self._c
        return soma

    def entrar_valores(self):
        valor1 = int(input('Digite o 1°: '))
        valor2 = int(input('Digite o 2°: '))
        valor3 = int(input('Digite o 3°: '))

        return valor1, valor2, valor3
    
calculos = Calcular
somando = calculos.somar(calculos.entrar_valores)
multiplicando = calculos.multiplicar(calculos.entrar_valores)

print(somando, multiplicando)