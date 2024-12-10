import os


os.system('cls')

# INDICES IGUAIS SÓ EXIBIRÃO UM ITEM
dicionario1 = {'nome': 'jane' , 'nome': 'john'}

# POSSO TER UMA TUPLA COMO INDICE E UMA LISTA COMO  VALOR
dicionario2 = {(1, 2) : [1, 2]}

# MAS NÃO POSSO TER UMA LISTA COMO INDICE E UMA TUPLA COMO VALOR
dicionario3 = {[1, 2] : (1, 2)}

print(dicionario1)
print(dicionario2)

