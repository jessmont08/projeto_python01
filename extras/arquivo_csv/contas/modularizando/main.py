import os


from pacote.divisao import dividir
from pacote.somar import somar
from pacote.subpacote.multiplicacao import multiplicar

while True: 
    os.system('cls')

    a = input('Digite o primeiro valor: ')
    b = input('Digite o segundo valor: ')

    if not a.replace('.', '', 1).isdigit() or not b.replace('.', '', 1).isdigit():
        print('Por favor digite um número válido.') 
        continue

    a = float(a)
    b = float(b)

    resultado_soma = somar(a, b)
    resultado_dividir = dividir(a, b)
    resultado_multiplicar = multiplicar(a, b)

    print('=' * 90)
    print('CÁLCULOS!')
    print('-' * 90)
    print(f'O cálculo da soma: {resultado_soma}.')
    print(f'O cálculo da divisão: {resultado_dividir}.')
    print(f'O cálculo da multiplicação: {resultado_multiplicar}')
    print('=' * 90)

    sair = input('Deseja sair do programa? (s/n): ').lower().strip()


    if sair == 's':
        print('saindo.')
        break
