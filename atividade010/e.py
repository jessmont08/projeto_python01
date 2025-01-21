import os


os.system('cls')

def calcular_imc(altura, peso):
    imc = peso / (altura ** 2) 

    return imc

altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))

imc =  calcular_imc(altura, peso)
print(f'O peso e a altura resultam no imc: {imc:.2f}')