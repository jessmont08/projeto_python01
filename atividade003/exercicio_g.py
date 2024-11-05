import os

os.system('cls')

import random

print('-' * 90) 
print('ESCOLHA DO USUÁRIO') 
print ('.' * 90) 

valor = int(input('Entre com o valor: '))
numero = random.randint(0, 5)

if numero == valor:
  print(f'O {valor} o valor está correto, usuário.')
else:
  print(f'O {valor} está errado, tente novamente.')

print('.' * 90) 
print() 
