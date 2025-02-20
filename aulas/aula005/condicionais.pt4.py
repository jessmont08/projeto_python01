import os


os.system('cls')

# declaracoes
x = 10
y = 5
j = 'mary'

print('-' * 90)
print('VERDADEIRO OU FALSO')
print('=' * 90)

# (and) Verdadeiro

print('E (and) Verdadeiro.')
if (x > 5 and y != j):
    print('Verdadeiro: Bloco executado.')
else: print('Falso: bloco executado.')

print('.' * 90)

# E (and) falso / a > 5 b == c
print('E (and) falso.')
if (x > 5 and y == j):
    print('Verdadeiro: bloco executado.')
else:
    print('Falso: bloco executado.')

print('.' * 90)

# OU (or) Verdadeiro / a > 5 == c
print('OU (or) Verdadeiro.')
if (x > 5 or y == j):
    print('Verdadeiro: bloco executado.')
else: 
    print('Falso: bloco executado.')

print('.' * 90)

 # OU (or) falso / a < 5 c == jane
print('Ou (or) False.')
if (x > 5 or j == 'jane'):
    print('Verdadeiro: bloco executado.')
else: 
    print('Falso: bloco executado.')

print('.' * 90)
print()