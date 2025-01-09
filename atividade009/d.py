import os

os.system('cls')

# tem a necessidade da criação de uma lisya
vinhos = {}

for i in range(1, 3):
    marca = str(input('Entre com a marca do vinho: '))
    tipo = str(input('Entre com o tipo do vinho: '))
    teor_alcoolico = float(input('Entre com o teor alcoolico: '))
    safra = int(input('Entre com o ano de safra: '))

    vinhos[marca] = {'Tipo': tipo, 'Teor Alcoolico': teor_alcoolico, 'Safra': safra}

print('Os vinhos no adega são: ')
for keys, values in vinhos.items():
    print(f'A marca do vinho é {keys}')
    print(f'')