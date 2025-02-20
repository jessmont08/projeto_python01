# Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11. Depois mostre um menu com as seguintes operações:
# 1. Soma: 2. Subtração : 3. Produto : 4. Divisão : 5. Divisão inteira : 6. Resto da divisão.
# O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6. Em seguida, você criará funções que retornem os resultados das operações,
# imprimindo os resultados na tela.


import os
os.system('cls')

from entradas.receber import receber_num
from entradas.menu import escolher_menu
from entradas.calculadora.calculos import operando_valores

# main
x, y = receber_num()
escolha = escolher_menu()
resultado = operando_valores(x, y, escolha)
print(f'O resultado é {resultado}')