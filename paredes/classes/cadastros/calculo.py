# a classe superficie é criada com o objetivo de ser a classe pai 
# das classes parede, teto e porta; o metódo principal saí daqui.

class Superficie:
    def __init__(self, nome='', area=0, tipo=''):
        self._nome = nome
        self._area = area
        self._tipo = tipo

    def calcular_tinta(self):
        """cria o nome do metódo e passa, ele ser
        reutilizado nas classes filhas."""
        pass

    # decorator
    @property
    def nome(self):
        return self._nome
    # decorator
    @nome.setter
    def nome(self, nome_tinta):
        self._nome = nome_tinta
    # decorator
    @property
    def area(self):
        return self._area
    # decorator
    @area.setter
    def area(self, area_tinta):
        self._area = area_tinta
    # decorator
    @property
    def tipo(self):
        return self._tipo
    # decorator
    @tipo.setter
    def tipo(self, tipo_tinta):
        self._tipo = tipo_tinta

# criação da classe para o tipo parede
class Parede(Superficie):
    def __init__(self, area):
        self._area = area
        
    def calcular_tinta(self):
        """esse metódo recebe o valor da area e divide pelo
        gasto padrão da superficie parede retorna ele"""
        gasto = self._area / 10
        return gasto
    
# criação da classe para o tipo teto
class Teto(Superficie):
    def __init__(self, area):
        self._area = area

    def calcular_tinta(self):
        """esse metódo recebe o valor da area e divide pelo
        gasto padrão da superficie teto retorna ele"""
        gasto = self._area / 8
        return gasto

# criação da classe para o tipo porta
class Porta(Superficie):
    def __init__(self, area):
        self._area = area

    def calcular_tinta(self):
        """esse metódo recebe o valor da area e divide pelo
        gasto padrão da superficie porta retorna ele"""
        gasto = self._area / 4
        return gasto
    
