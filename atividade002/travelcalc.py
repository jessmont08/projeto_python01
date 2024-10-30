# A empresa "TravelCalc" está desenvolvendo um sistema de cálculo de preços de passagens de ônibus com base na distância da viagem. 
# Eles precisam de um programa que solicite ao usuário a distância a desejada e, em seguida, calcule o preço da passagem de acordo com as políticas da empresa.
#  Segundo essas políticas, viagens de até 200 km têm um custo de R$0,70 por km rodado, enquanto viagens acima dessa distância passam a custar R$0,40 por km rodado.


import os

os.system('cls')

print('-' * 90)
print('TRAVEL CALC.')
print('=' * 90)

distancia = float(input('DIGA A DISTÂNCIA DESEJADA: '))

print('.' * 90)

valor1 = distancia * 0.70
valor2 = distancia * 0.40

if distancia >= 200:
    print(f'Sua viagem custará {valor1} reais.')
else:
    print(f'Sua viagem custará {valor2} reais.')
print('_' * 90)



