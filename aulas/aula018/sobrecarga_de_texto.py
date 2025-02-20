
class ClassePai:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def metodo_classes(self, a, b):
        pass

class ClasseFilha(ClassePai): # classe derivada
    def __init__(self, a, b):
        # metódo construtor
        self.a = a
        self.b = b

    # sobrecarga do método
    def metodo_classes(self):
        soma = self.a + self.b
        return soma

#programa principal
teste = ClasseFilha(1, 2)
teste.metodo_classes()