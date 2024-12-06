import os


os.system('cls')

compras = {}
pessoas = {}
cores = {}
elementos = dict()
numeros = dict()

# atribuindo valores
compras['id'] = 1
compras['item'] = 'caderno'
compras['valor'] = 10.80

pessoas['id'] = '0010'
pessoas['nome'] = 'maddie'
pessoas['endereço'] = 'nicolau lammoglia'
pessoas['numero'] = '0221b'
pessoas['cidade'] = 'michigan'
pessoas['país'] = 'inglaterra'

cores['red'] = 'vermelho'
cores['green'] = 'verde'
cores['blue'] = 'azul'

elementos['Pb'] = 'chumbo'
elementos['Au'] = 'ouro'
elementos['N'] = 'nitrogênio'

numeros[1] = 100
numeros[2] = 200
numeros[3] = 300

# saída simples

print(f'compras ; {compras}')
print(f'detetives ; {compras}')
print(f'cor rgb ; {cores}')
print(f'tabela períodica; {elementos}')
print(f'listagem de números ; {numeros}')
