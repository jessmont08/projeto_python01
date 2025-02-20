# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.

class Numero:
    def __init__(self, a):
        self._a = a

    def set_a(self, valor):
        self._a = valor

    def get_a(self):
            return self._a
    
    def antecessor(self):
        antecessor = self.get_a() - 1
        return antecessor
    
    def sucecessor(self):
        sucessor = self.get_a() + 1
        return sucessor
    
valor = int(input('Digite o valor que deseja ver: '))
calculo = Numero(0)
calculo.set_a(valor)

print(f'O antecessor é {calculo.antecessor()} e o sucessor é {calculo.sucecessor()}')