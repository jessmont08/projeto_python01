# A empresa "SalaryBoost" está implementando um sistema automatizado para calcular os aumentos salariais de seus funcionários com base em critérios
#  específicos. Eles precisam de um programa que receba como entrada o salário atual de um funcionário e, em seguida, 
# calcule o novo salário com base em determinadas condições. Essas condições incluem um aumento de 5% caso o salário atual
#  seja superior a R$1500,00, e um aumento de 10% caso o salário atual seja inferior a R$1000,00. Além disso, o programa deve garantir
#  que o salário informado não seja igual a zero ou negativo, pois isso não seria válido.

import os


os.system('cls')

print('-' * 90)
print('SALAARY BOOST.')
print('=' * 90)

salario = float(input('ENTRE COM SEU SALÁRIO: '))
novo_valor1 = salario + (salario * 10 / 100)
novo_valor2 = salario + (salario * 5 / 100)


if salario >= 1500:
    print(f'O novo salário será de {novo_valor2}')
elif salario >= 1000:
    print(f'O novo salário será de {novo_valor1}')
elif salario <= 0:
    print(f'valor incompativel.')