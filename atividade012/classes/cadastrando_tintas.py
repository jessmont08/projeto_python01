from calculos import Parede, Teto, Porta

class CadastrarExibir():
    def __init__(self):
        self.tintas = []

    def cadastrar(self):
 
        while True:
            nome = input('Digite o nome da tinta (cor): ')
            tipo = input('Digite o tipo (parede, teto ou porta): ')
            area = int(input('Digite a área da superfície (em metros quadrados): '))

            if tipo == 'parede':
                superficie = Parede(area)
            elif tipo == 'teto':
                superficie = Teto(area)
            elif tipo == 'porta':
                superficie = Porta(area)

            gastos = superficie.calcular_tinta()
            
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

            escolha = input('Escolha: ')
            if escolha == '1': 
                for cadastros in self.tintas:
                    if cadastros['tipo'] == 'parede':
                        print(f'Tinta: {cadastros["nome"]}')
                        print(f'Area: {cadastros["area"]}')
                        print(f'Tipo: {cadastros["tipo"]}')
                        print(f'Gasto: {cadastros["gasto"]}')
            
            if escolha == '2': 
                for cadastros in self.tintas:
                    if cadastros['tipo'] == 'teto':
                        print(f'Tinta: {cadastros["nome"]}')
                        print(f'Area: {cadastros["area"]}')
                        print(f'Tipo: {cadastros["tipo"]}')
                        print(f'Gasto: {cadastros["gasto"]}')
                
            if escolha == '3': 
                for cadastros in self.tintas:
                    if cadastros['tipo'] == 'porta':
                        print(f'Tinta: {cadastros["nome"]}')
                        print(f'Area: {cadastros["area"]}')
                        print(f'Tipo: {cadastros["tipo"]}')
                        print(f'Gasto: {cadastros["gasto"]}')
            
            if escolha == '4':
                print('SAIDA SOLICITADA.')
                break             

     
