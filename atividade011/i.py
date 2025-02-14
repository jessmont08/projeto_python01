# Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.
class Reais:
    def __init__(self, dinheiro):
        self._dinheiro = dinheiro

    def set_dinheiro(self, reais):
        self._dinheiro = reais

    def get_dinheiro(self):
        return self._dinheiro
    
    def converter_para_dolares(self):
        dolar = float(5.72)
        conversao = self.get_dinheiro() / dolar

        return conversao
    
reais = float(input('Digite o valor que quer converter: '))
dolares = Reais(reais)

print(f'{dolares.get_dinheiro()} é equivalente a {dolares.converter_para_dolares():.2f}')