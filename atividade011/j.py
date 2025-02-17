# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.

class Retangulo:
    def __init__(self, a, b):
        self._a = a
        self._b =  b

    def set_a(self, comprimento):
        self._a = comprimento

    def set_b(self, largura):
        self._b = largura

    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b
    
    def calcular_perimetro(self):
        perimetro = 2 * (self.get_a() + self.get_b())
        return perimetro
    
comprimento = int(input('Digite o comprimento: '))
largura = int(input('Digite a largura: '))
calculo = Retangulo(0, 0)
calculo.set_a(comprimento)
calculo.set_b(largura)

print(f'O perímetro mede: {calculo.calcular_perimetro()}')