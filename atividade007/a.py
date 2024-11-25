
# Mostre a quantidade de notas que foram lidas.
# Exiba todas as notas na ordem em que foram informadas.
# Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# Calcule e mostre a soma das notas.
# Calcule e mostre a média das notas.

while (True):

    lista = [ ]

    print('Digite "s" para sair.')
    notas = str(input('Entre com as notas: '))

    if notas != "s":
        print(f'Digite a proxíma.')
    else:
        break
    
    lista.append(notas)

