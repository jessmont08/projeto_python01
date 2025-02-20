class MinhaClasse:
    def __init__(self, valor):
        self._atributo = valor

    @property
    def atributo(self):
        return self._atributo
    
    @atributo.setter
    def atributo(self, valor):
        self._atributo = valor

obj = MinhaClasse(10)
obj.atributo = 20
print(obj.atributo)