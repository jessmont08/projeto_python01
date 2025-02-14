# Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.

class DobroTriplo:
    def __init__(self, a):
        self._a = a

    def set_a(self, valor):
        self.set_a = valor

    def get_a(self):
        return self._a
    
    def operando_dobro(self):
        dobro = self.get_a() * 2
        return dobro
    
    def operando_triplo(self):
        dobro = self.get_a() * 3
        return dobro
    
    
valor = int(input('Digite o valor: '))

calculo = DobroTriplo(valor)

print(f'O dobro de {calculo.get_a()} é {calculo.operando_dobro()}'
      f' e o triplo é {calculo.operando_triplo()}')