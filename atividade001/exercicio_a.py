import os

os.system('cls')

print('-' * 90)
print('ENTRADAS DO USUÁRIO')
print('=' * 90)

valor1 = float(input('Entre com o valor a ser calculado: '))
valor2 = float(input('Entre com o valor a ser calculado: '))
valor3 = float(input('Entre com  valor a ser calculado: '))

# processamento
soma = valor1 + valor2 + valor3
multiplicacao = valor1 * valor2 * valor3

print('-' * 30)
print()
print('RESULTADOS')
print()
print('=' * 30)
print()

print(f'Soma de {valor1} + {valor2} + {valor3} é = {soma}')
print(f'Multiplicação de {valor1} * {valor2} * {valor3} é = {multiplicacao}')
print()