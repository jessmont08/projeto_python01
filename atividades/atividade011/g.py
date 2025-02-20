# Faça um programa que converta metros em centímetros e milímetros.

class Metros:
    def __init__(self, a):
        self._a = a

    def set_a(self, metros):
        self._a = metros

    def get_a(self):
        return self._a
    
    def converter_centimetros(self):
        centrimetros = self.get_a() * 100
        return centrimetros
    
    def converter_milimetros(self):
        milimetros = self.get_a()* 1000
        return milimetros
    
metros = int(input('Digite a quantidade de metros: '))
medida = Metros(0)
medida.set_a(metros)

print(f'A conversão de {medida.get_a()} para centrímetros'
      f' é {medida.converter_centimetros()}')

print(f'A conversão de {medida.get_a()} para milímetros'
      f' é {medida.converter_milimetros()}')