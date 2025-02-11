class OperacoesBasicas():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def somar(self):
        return self.a + self.b
    
    def subtracao(self):
        return self.a + self.b
    
    def produto(self):
        return self.a * self.b
    
    def divisao(self):
        if self.b != 0:
           return self.a / self.b
        else:
            print('Erro: divisão por 0.')
    
    def resto(self):    
        if self.b != 0:
            return self.a % self.b
        else:
           print('Erro: divisão por 0.')
    
    def inteira(self):
        if self.b != 0:
            return self.a // self.b
        else:
           print('Erro: divisão por 0.')


