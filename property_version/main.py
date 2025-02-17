class Soma:
    def __init__(self, a=0, b=0):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, b):
        self._b = b

    def somar(self):
        return self._a +  self._b
    
soma = Soma()
soma.a = 29
soma.b = 21
print(soma.somar())