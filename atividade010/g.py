# Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11. Depois mostre um menu com as seguintes operações:
# 1. Soma: 2. Subtração : 3. Produto : 4. Divisão : 5. Divisão inteira : 6. Resto da divisão.
# O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6. Em seguida, você criará funções que retornem os resultados das operações,
# imprimindo os resultados na tela.


import os


os.system('cls')

def receber_num():
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

    if x < 0 or x > 11:
        print('valor invalido.')
        return None
    elif  y < 0 or y > 11:
        print('valor invalido.')
        return None
    
    return x, y

def escolher_menu():
    
    print('Menu de operações.')
    print('1. Soma.')
    print('2. Subtração.')
    print('3. Multiplicação.')
    print('4. Divisão.')
    print('5. Divisão inteira.')
    print('6. Resto da divisão.')

    escolha = int(input('Escolha do 1 ao 6: '))
    if escolha < 1 or escolha > 6:
        print('Valor ínvalido.')
        return None

    return escolha

def operando_valores(x, y, escolha):
    if escolha == 1: 
        soma = x + y
        return soma
    elif escolha == 2:
        subtracao = x - y
        return subtracao
    elif escolha == 3:
        multiplicacao = x * y
        return multiplicacao
    elif escolha == 4:
        if y == 0:
            print('Erro por divisão com zero.')
            return None
        divisao = x / y
        return divisao
    elif escolha == 5:
        if y == 0:
            print('Erro por divisão com zero.')
            return None
        inteira = x // y
        return inteira
    elif escolha == 6:
        if y == 0:
            print('Erro por divisão com zero.')
            return None
        resto = x % y
        return resto




# main
x, y = receber_num()
escolha = escolher_menu()
resultado = operando_valores(x, y, escolha)
print(f'O resultado é {resultado}')