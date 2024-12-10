import os


os.system('cls')

soma = 0

for var_iteradora in range(0,4):
    numero = int(input(f'{var_iteradora + 1}ª numéro: '))
                 
if (numero % 2 == 0):
    print(F'O número {numero} é par.')
else:
    print(f'O numéro {numero} é impar')