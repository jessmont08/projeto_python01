# Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.

class Media:
    def __init__(self, nota1, nota2, nota3, nota4):
        self._nota1 = nota1
        self._nota2 = nota2
        self._nota3 = nota3
        self._nota4 = nota4

    def set_nota1(self, nota1):
        self._nota1 = nota1

    def set_nota2(self, nota2):
        self._nota2 = nota2

    def set_nota3(self, nota3):
        self._nota3 = nota3
    
    def set_nota4(self, nota4):
        self._nota4 = nota4
    
    def get_nota1(self):
        return self._nota1
    
    def get_nota2(self):
        return self._nota2

    def get_nota3(self):
        return self._nota3
    
    def get_nota4(self):
        return self._nota4
    
    def calcular_media(self):
        media = (self.get_nota1() + self.get_nota2() +
                 self.get_nota3() + self.get_nota4()) / 4
        return media
    
nota1 = int(input(f'Digite a 1° nota: '))
nota2 = int(input(f'Digite a 2° nota: '))
nota3 = int(input(f'Digite a 3° nota: '))
nota4 = int(input(f'Digite a 4° nota: '))

calculo = Media(0, 0, 0, 0)
calculo.set_nota1(nota1)
calculo.set_nota2(nota2)
calculo.set_nota3(nota3)
calculo.set_nota4(nota4)

resultado = calculo.calcular_media()
print(f'{resultado}')
    
