class Superficie:
    def __init__(self, nome='', area=0, tipo=''):
        self._nome = nome
        self._area = area
        self._tipo = tipo

    def calcular_tinta(self):
        pass

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome_tinta):
        self._nome = nome_tinta

    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, area_tinta):
        self._area = area_tinta

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo_tinta):
        self._tipo = tipo_tinta

class Parede(Superficie):
    def __init__(self, area):
        self._area = area
        
    def calcular_tinta(self):
        gasto = self._area / 10
        return gasto
    
class Teto(Superficie):
    def __init__(self, area):
        self._area = area

    def calcular_tinta(self):
        gasto = self._area / 8
        return gasto
    
class Porta(Superficie):
    def __init__(self, area):
        self._area = area

    def calcular_tinta(self):
        gasto = self._area / 4
        return gasto

