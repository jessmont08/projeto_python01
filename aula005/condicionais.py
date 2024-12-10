import os


os.system('cls')

print('-' * 80)
print('ESTUDO DE CONDICIONAIS')
print('=' * 80)

# entrada
valor = float(input('ENTRE COM O VALOR:'))
resposta = ''

# condicional
if valor % 2 == 0:
    resposta = f'O numéro {valor} é par'
else:
    resposta = f'O  numéro {valor} é ímpar'

print('-' * 60)
print('DEFINIÇÃO')
print('=' * 60)

print(resposta)
print('-' * 60)
