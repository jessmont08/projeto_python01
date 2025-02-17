import math
import os


class Triangulo:
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2

class TrianguloRetangulo(Triangulo):
    def calcular_hipotenusa(self):
        resultado = math.sqrt(pow(self.cateto1, 2) + pow(self.cateto2, 2))
        return resultado
    
while True:
    os.system('cls')
    cateto1 = float(input('Entre com o cateto a: '))
    cateto2 = float(input('Entre com o cateto b:'))

    if cateto1 == 0 or cateto2 == 0:
        print('Fim do programa.')
        break

    else:
        triangulo_retangulo = TrianguloRetangulo(cateto1, cateto2)
        hipotenusa = triangulo_retangulo.calcular_hipotenusa()

        os.system('cls')

    print(f'O triâgulo retângulo de lado = {cateto1} e')
    print(f'de lado 2 = {cateto2} é igual a {hipotenusa:.2f} aproximadamente!')
    input('Pressione enter para retornar.')