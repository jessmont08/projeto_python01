import os

os.system('cls')

print('-' * 90)
print('ESTUDO DE CONDICIONAIS 1.2')
print('=' * 90)

# declaracoes
x = 10
y = 30
resposta = ''

print()
print('CONDICIONAIS SIMPLES')
print('=' * 90)

# condicionais
if y > x:
    resposta = f'{y} é maior que {x}'
else:
    resposta = f'{y} é menor que {x}'

print(resposta)
print('-' * 90)
print()


print('CONDICIONAIS ANINHADA')
print('=' * 90)

# declaracoes
a = (10 * 10)
b = 100
resposta = ''

# condicinais
if a > b:
    resposta = f'{a} é maior que {b}'
elif b > a:
    resposta = f'{a} é menor que {b}'
else:
    resposta = f'{a} é igual a {b}'


print(resposta)
print('-' * 90)
print()
