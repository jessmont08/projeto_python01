from cadastros.calculo import Parede, Teto, Porta
import os

class CadastrarExibir():
    def __init__(self):
        self.tintas = []

    def cadastrar(self):
        tipos_entrada = ['parede', 'teto', 'porta']
        while True:
            print('=' * 90)
            nome = input('Digite o nome da tinta (cor): ').lower().strip()
            tipo = input('Digite o tipo (parede, teto ou porta): ').lower().strip()
            if tipo not in tipos_entrada:
                print('Digite um tipo válido.')
                tipo = input('Digite o tipo (parede, teto ou porta): ').lower().strip()

            try:
                area = int(input('Digite a área da superfície (em metros quadrados): '))
            except ValueError:
                print('Digite um valor correto.')
                area = int(input('Digite a área da superfície (em metros quadrados): '))

            if tipo == 'parede':
                superficie = Parede(area)
            elif tipo == 'teto':
                superficie = Teto(area)
            elif tipo == 'porta':
                superficie = Porta(area)

            gastos = superficie.calcular_tinta()
            cadastros = {'nome': nome, 'area': area, 'tipo': tipo, 'gasto' : gastos}
            self.tintas.append(cadastros)
             
            print('-' * 90)
            saida = input('Deseja continuar? s ou n: ').lower().strip()
            if saida == 'n':
                break
            os.system('cls')

    def exibindo(self):
        for cadastros in self.tintas:
            print('=' * 90)
            print(f'Tinta: {cadastros["nome"]}')
            print(f'Area: {cadastros["area"]}')
            print(f'Tipo: {cadastros["tipo"]}')
            print(f'Gasto: {cadastros["gasto"]}')
        print('=' * 90)

    def filtrando(self):
        print('escolha qual tipo deseja ver. ')
        escolha_tipo = input('parede, teto ou porta: ').lower().strip()
        tipos_validos = ['parede', 'teto', 'porta']
        if escolha_tipo in tipos_validos:
                for cadastros in self.tintas:
                    if cadastros['tipo'] == escolha_tipo:
                        print('=' * 90)
                        print(f'Tinta: {cadastros["nome"]}')
                        print(f'Area: {cadastros["area"]}')
                        print(f'Tipo: {cadastros["tipo"]}')
                        print(f'Gasto: {cadastros["gasto"]}')
                print('-' * 90)
                print()

        else:
            print('Digite uma opção válida.')