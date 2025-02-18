from math import pi

# define a classe base forma com um metódo area 
# que não faz nada (é quase uma classe abstrata)

class Forma:
    def area(self):
        pass

# define a classe Circulo que herda de Forma
# O construtor __init__ inicializa o atributo raio

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    # define o metódo area para calcular a area do
    # circulo usando a formula pi * raio²

    def area(self):
        return pi * (self.raio ** 2)

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    # define o metódo area para calcular a area
    # do retangulo usando formula * largura
    def area(self):
        return self.largura * self.altura
    

# define a classe Quadrado que herda do retangulo
class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    # define usa função exibir_area que aceita um
    # objeto forma e imprime sua área
    # O metódo area é chamado no objeto

def exibir_area(forma):
    print(f'A aréa da forma é {forma.area()}')

# cria as instancias do circulo, rwtangulo e quadrado
circulo = Circulo(5)
retangulo = Retangulo(4, 6)
quadrado = Quadrado(5)

# chama a função exibir_area para cada instância 
# o metódo area apropriado é chamado para 
# cada objeto, mostrando polimorfismo

exibir_area(circulo)
exibir_area(retangulo)
exibir_area(quadrado)

