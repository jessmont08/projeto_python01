# Crie um sistema para calcular os gastos com tinta ao pintar diferentes tipos de superfícies. 
# A classe base Superficie deve conter os atributos nome, area (em metros quadrados) e tipo de superfície.
# Ela deve ter um método calcular_tinta() que será sobrescrito nas subclasses. A classe Parede usa 1 litro de tinta para cobrir 10 m², 
# a classe Teto usa 1 litro para cobrir 8 m², e a classe Porta usa 1 litro para cobrir 4 m². O sistema deve permitir o cadastro de 
# múltiplas superfícies, armazená-las em uma lista, e usar um laço for para calcular o gasto de tinta e exibir os dados de cada superfície. 
# Também deve ser possível filtrar as superfícies por tipo. O objetivo é praticar o uso de listas, loops, condicionais e herança.


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

class CadastrarExibir():
    def __init__(self):
        self.tintas = []

    def cadastrar(self):
 
        while True:
            nome = input('Digite o nome da tinta (cor): ')
            tipo = input('Digite o tipo (parede, teto ou porta): ')
            area = int(input('Digite a área da superfície (em metros quadrados): '))

            if tipo == 'parede':
                Superficie = Parede(area)
            elif tipo == 'teto':
                Superficie = Teto(area)
            elif tipo == 'porta':
                Superficie = Porta(area)

            gastos = Superficie.calcular_tinta()
            
            saida = input('Deseja continuar? s ou n: ')
            if saida == 'n':
                break

            cadastros = {'nome': nome, 'area': area, 'tipo': tipo, 'gasto' : gastos}
            self.tintas.append(cadastros)

    def exibindo(self):
        for cadastros in self.tintas:
            print(f'Tinta: {cadastros["nome"]}')
            print(f'Area: {cadastros["area"]}')
            print(f'Tipo: {cadastros["tipo"]}')
            print(f'Gasto: {cadastros["gasto"]}')
    
    def filtrando(self):
        print('FILTRAR POR: ')
        print('1. Parede.')
        print('2. Teto.')
        print('3. Porta.')
        print('4. Sair.')

        while True:
            escolha = int(input('Escolha: '))
            if escolha == 1: 
                for cadastros in self.tintas:
                    if cadastros['tipo'] == 'parede':
                        print(f'Tinta: {cadastros["nome"]}')
                        print(f'Area: {cadastros["area"]}')
                        print(f'Tipo: {cadastros["tipo"]}')
                        print(f'Gasto: {cadastros["gasto"]}')
            
            if escolha == 2: 
                for cadastros in self.tintas:
                    if cadastros['tipo'] == 'teto':
                        print(f'Tinta: {cadastros["nome"]}')
                        print(f'Area: {cadastros["area"]}')
                        print(f'Tipo: {cadastros["tipo"]}')
                        print(f'Gasto: {cadastros["gasto"]}')
                
            if escolha == 3: 
                for cadastros in self.tintas:
                    if cadastros['tipo'] == 'porta':
                        print(f'Tinta: {cadastros["nome"]}')
                        print(f'Area: {cadastros["area"]}')
                        print(f'Tipo: {cadastros["tipo"]}')
                        print(f'Gasto: {cadastros["gasto"]}')
            
            if escolha == 4:
                print('SAIDA SOLICITADA.')
                break             



superficie1 = Superficie()
cadastro = CadastrarExibir()

cadastro.cadastrar()
cadastro.exibindo()
cadastro.filtrando()




        

        
