import os


os.system('cls')

contador = 0

while (contador <= 10):

    contador += 1

    if (contador % 2 == 0):
       continue    
    print(f'Contador = {contador}')

else:
    print('Ao acabar do while, fim do programa.')

print('=' * 90)
print('Fim do programa.')
print('.' * 90)

print()