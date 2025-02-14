# Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.

class Divisao: 
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def set_a(self, valor1):
        self._a = valor1
    
    def set_b(self, valor2):
        self._b = valor2

    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b

    def dividir(self):
        divisao = self.get_a() / self.get_b()
        return divisao

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

calculo = Divisao(valor1, valor2)
resultado = calculo.dividir()
print(f'O resultado é {resultado:.4f}')