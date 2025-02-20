from cadastros.calculo import Parede, Teto, Porta
import os

# cria a classe de exibição
class CadastrarExibir():
    def __init__(self):
        self.tintas = [] # declara a lista do enunciado

    def cadastrar(self):

        """método que solicita os valores para o usuário
        e adiciona ao dicionario; também garante que as entradas
        sejam corretas com validações."""

        tipos_entrada = ['parede', 'teto', 'porta'] # lista para validação de tipos

        # loop para a entrada de quantas superficies
        # o usuário querer
        while True:
            print('=' * 90)
            nome = input('Digite o nome da tinta (cor): ').lower().strip()
            tipo = input('Digite o tipo (parede, teto ou porta): ').lower().strip()
            if tipo not in tipos_entrada: # se o usuário digitar um tipo não cadastrado, é solicitado um novo valor
                print('Digite um tipo válido.')
                tipo = input('Digite o tipo (parede, teto ou porta): ').lower().strip()
            
            # evita quebra de codigo por erro de entrada
            try:
                area = int(input('Digite a área da superfície (em metros quadrados): '))
            except ValueError:
                print('Digite um valor correto.')
                area = int(input('Digite a área da superfície (em metros quadrados): '))

            # de acordo com o tipo, as subclasses são puxadas.
            if tipo == 'parede':
                superficie = Parede(area)
            elif tipo == 'teto':
                superficie = Teto(area)
            elif tipo == 'porta':
                superficie = Porta(area)

            gastos = superficie.calcular_tinta() # metodo
            cadastros = {'nome': nome, 'area': area, 'tipo': tipo, 'gasto' : gastos} # dicionari0
            self.tintas.append(cadastros) # adiciona o dicionario na lista
             
            print('-' * 90)
            saida = input('Deseja continuar? s ou n: ').lower().strip()
            if saida == 'n':
                break
            os.system('cls')

    def exibindo(self):
        """método que exibe todas as superficies 
        que o usuário colocou"""
        for cadastros in self.tintas:
            print('=' * 90)
            print(f'Tinta: {cadastros["nome"]}')
            print(f'Area: {cadastros["area"]}')
            print(f'Tipo: {cadastros["tipo"]}')
            print(f'Gasto: {cadastros["gasto"]}')
        print('=' * 90)

    def filtrando(self):
        """método que filtra um único tipo superficie 
        de acordo com a escolha do usuário"""

        print('escolha qual tipo deseja ver. ')
        escolha_tipo = input('parede, teto ou porta: ').lower().strip()
        tipos_validos = ['parede', 'teto', 'porta']
        if escolha_tipo in tipos_validos: # garante que o tipo exista na lista
                for cadastros in self.tintas: # entra no dicionario da lista e faz uma varredura
                    if cadastros['tipo'] == escolha_tipo: # de acordo com o tipo, printa somente ele
                        print('=' * 90)
                        print(f'Tinta: {cadastros["nome"]}')
                        print(f'Area: {cadastros["area"]}')
                        print(f'Tipo: {cadastros["tipo"]}')
                        print(f'Gasto: {cadastros["gasto"]}')
                print('-' * 90)
                print()

        else:
            print('Digite uma opção válida.')