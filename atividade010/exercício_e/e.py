import os
from receber_valores.alt_kg import calcular_imc

os.system('cls')

altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))


imc =  calcular_imc(altura, peso)
print(f'O peso e a altura resultam no imc: {imc:.2f}')