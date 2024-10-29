#A empresa "DataMax" está desenvolvendo um novo software de análise estatística e precisa de uma funcionalidade que permita aos usuários inserir três números e,
# em seguida, exibir na tela qual é o maior número, qual é o menor número ou se os números são todos iguais. Essa funcionalidade é crucial para os analistas 
# de dados da "DataMax" que trabalham com conjuntos de dados diversos e precisam rapidamente identificar as características básicas desses conjuntos,
# como a presença de outliers ou a uniformidade dos números.

import os


os.system('cls')

print('_' * 90)
print('DATA MAX')
print('=' * 90)

a = int(input('ENTRE COM O NUMÉRO: '))
b = int(input('ENTRE COM O NUMÉRO: '))
c = int(input('ENTRE COM O NUMÉRO: '))

print('.' * 90)

if a > b and a > c: 
    print(f'{a} é o maior valor.')
elif b > c and b > a:
    print(f'{b} é o maior valor.')
elif c > a and c > b:
    print(f'{c} é o maior valor.')
else: 
    print('Todos numéros tem o mesmo valor.')