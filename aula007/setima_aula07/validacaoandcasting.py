import os


os.system('cls')


soma = 0

for var_iteradora in range (0, 5):

    numero = input('Entre com um número[0 - 5]: ')
    if (not(numero.isnumeric())):
        print(f'O número {numero} é inválido.')
    else:
       numero = int(numero)   

    if (numero >= 0 and numero <= 5): 
      print(f'O número está dentro do intervalo.')
    else:
        print('Entrada inválida')

print()