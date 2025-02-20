# Você está desenvolvendo um programa para determinar se três segmentos podem formar um triângulo.
#  Para isso, o programa precisa receber as medidas dos três segmentos e compará-las entre si.
#  A resposta resultante dessa comparação deve indicar se os segmentos fornecidos podem formar um triângulo ou não.

import os

os.system('cls')

print('-' * 90)
print('TRIÂNGULOS.')
print('=' * 90)

a = float(input('ENTRE COM O VALOR 1: '))
b = float(input('ENTRE COM O VALOR 2: '))
c = float(input('ENTRE COM O VALOR 3: '))

if (a + b > c and b + c > a and a + c > b):
    print('Sim, é possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')

print('.' * 90)
print()