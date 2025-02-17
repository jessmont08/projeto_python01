import os

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        return 'isto está no metódo latir.'
    def miar(self):
        return 'isto está no metódo miar.'
    
class Cachorro(Animal):
    def latir(self):
        return f'{self.nome} está latindo!'

class Gato(Animal):
    def miar(self):
        return f'{self.nome} está miando.'

os.system('cls')
cao = Cachorro('rex')
gato = Gato('tobias')
print(cao.latir())
print(gato.miar())