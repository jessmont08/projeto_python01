# Crie um sistema para calcular os gastos com tinta ao pintar diferentes tipos de superfícies. 
# A classe base Superficie deve conter os atributos nome, area (em metros quadrados) e tipo de superfície.
# Ela deve ter um método calcular_tinta() que será sobrescrito nas subclasses. A classe Parede usa 1 litro de tinta para cobrir 10 m², 
# a classe Teto usa 1 litro para cobrir 8 m², e a classe Porta usa 1 litro para cobrir 4 m². O sistema deve permitir o cadastro de 
# múltiplas superfícies, armazená-las em uma lista, e usar um laço for para calcular o gasto de tinta e exibir os dados de cada superfície. 
# Também deve ser possível filtrar as superfícies por tipo. O objetivo é praticar o uso de listas, loops, condicionais e herança.


class Superficie:
    def __init__(self, nome, area, tipo):
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
    def __init__(self, nome, area, tipo):
        super().__init__(nome, area, tipo)

    def calcular_tinta(self):
        gasto = self._area / 10
        return gasto
    
class Teto(Superficie):
    def __init__(self, nome, area, tipo):
        super().__init__(nome, area, tipo)

    def calcular_tinta(self):
        gasto = self._area / 8
        return gasto
    
class Porta(Superficie):
    def __init__(self, nome, area, tipo):
        super().__init__(nome, area, tipo)

    def calcular_tinta(self):
        gasto = self._area / 4
        return gasto
    
