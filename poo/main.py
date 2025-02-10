import os
from calculos.operacoes import OperacoesBasicas


def escolher_menu():
    print('=' * 90)
    print('1. Soma.'
            '\n2. Subtração.'
            '\n3. Produto.'
            '\n4. Divisão.'
            '\n5. Resto.'
            '\n6. Inteira.')
       
os.system('cls')

escolher_menu()
print('-' * 90)
escolha = int(input('Digite a operação que deseja realizar: '))
print('=' * 90)
if 1 <= escolha <= 6:
    print('Escolha os valores.')
    print('-' * 90)
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    print('=' * 90)
else:
    print('Escolha ínvalida.')
    print('=' * 90)

if escolha == 1:
    calculos = OperacoesBasicas(a, b)
    resultado = calculos.somar()
    print(resultado)
    print('=' * 90)

if escolha == 2:
    calculos = OperacoesBasicas(a, b)
    resultado = calculos.subttracao()
    print(resultado)
    print('=' * 90)

if escolha == 3:
    calculos = OperacoesBasicas(a, b)
    resultado = calculos.produto()
    print(resultado)
    print('=' * 90)

if escolha == 4:
    calculos = OperacoesBasicas(a, b)
    resultado = calculos.divisao()
    print(resultado)
    print('=' * 90)

if escolha == 5:
    calculos = OperacoesBasicas(a, b)
    resultado = calculos.resto()
    print(resultado)
    print('=' * 90)

if escolha == 6:
    calculos = OperacoesBasicas(a, b)
    resultado = calculos.inteira()
    print(resultado)
    print('=' * 90)


        

