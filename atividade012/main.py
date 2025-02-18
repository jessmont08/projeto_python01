 # usar um laço for para calcular o gasto de tinta e exibir os dados de cada superfície. 
# Também deve ser possível filtrar as superfícies por tipo. 


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



class Cadastro(Superficie):

    def __init__(self, nome, area, tipo):
        super().__init__(nome, area, tipo)

    def entrando(self):
        tintas = []
        while True:
            self._nome = input('Digite o nome da tinta (cor) para sair: ')
            self._area = int(input('Digite a area: '))
            self._tipo = input('Digite o tipo (parede, teto ou porta): ')
            saida = input('Deseja continuar? s ou n:')
            cadastros = {'nome': self._nome, 'area': self._area, 'tipo': self._tipo}

            tintas.append(cadastros)

            if saida == 'n':
                break

            

        return tintas







