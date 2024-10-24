import os

os.system('cls')

print('-' * 90)
print('OPERACÕES BÁSICAS')
print('=' * 90)     

print()

print('SOMA')
print()
print('-' * 30)

primeiro_valor = float(input('Entre com o 1° valor: '))
segundo_valor = float(input('Entre com o 2° valor: '))
print('-' * 30)
print()

print('SUBTRAÇÃO')
print()
print('-' * 30)

minuendo = float(input('Entre com o 1° valor: '))
subtraendo = float(input('Entre com o 2° valor: '))

print('-' * 30)
print()

print('MULTIPLICAÇÃO')
print()
print('-' * 30)

multiplicando = float(input('Entre com o 1° valor: '))
multiplicador = float(input('Entre com o 2° valor: '))

print('-' * 30)
print() 

print('DIVISÃO')
print()
print('-' * 30)

dividendo = float(input('Entre com 1° valor: '))
divisor = float(input('Entre com o 2° valor: '))

print('-' * 30)
print()
print('RAIZ QUADRADA')
print()
print('-' * 30)

raiz = float(input('Entre com valor da raiz: '))

print('-' * 30)
print()
print('RAIZ CUBÍCA')
print()
print('-' * 30)

raiz3 = float(input('Entre com valor da raiz: '))

soma = primeiro_valor + segundo_valor
subtração = minuendo - subtraendo
multiplição = multiplicando * multiplicador
divisão = dividendo / divisor
raiz_quadrada = raiz ** (1/2)
raiz_cubica = raiz3 ** (1/3)

print('-' * 30)
print()
print('RESULTADOS')
print()
print('=' * 30)
print()

print(f'A soma de {primeiro_valor} + {segundo_valor} é = {soma}')
print(f'A subtação de {minuendo} - {subtraendo} é = {subtração}')
print(f'A multiplicação de {multiplicando} * {multiplicador} é = {multiplição}')
print(f'A divisão de {dividendo} / {divisor} é = {divisão}')
print(f'A raiz de {raiz} é = {raiz_quadrada} ')
print(f'A raiz cubica de {raiz3} é = {raiz_cubica} ')
print()