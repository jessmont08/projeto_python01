import os


os.system('cls')

# entrada pelo usuario
nome = str(input('ENTRE COM SEU NOME: '))

# declaração
nome1 = 'maria fernanda'
valor1 = 23
valor2 = 1

#processamento
divisao = valor1 / valor2

# saida
print(f'o nome do usuário é {nome}')
print(f'A soma do {valor2} / {valor1} é igual a {divisao}')

#condiconais

a = 50
b = 40
c = 30

if a and b > c:
    print(f'{c} é menor que a soma dos dois primeiros valores.')
elif c and b > a:
    print(f'{a} é menor que a soma dois outros valores')
else:
    print('todos os valores são menores que a soma dos outros.')

