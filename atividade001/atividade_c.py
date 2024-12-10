# Elabore um programa que receba quatro notas de um aluno e calcule a média dessas notas.

import os

os.system('cls')

print('-' * 90)
print('CALCULAR MÉDIA DOS ALUNOS')
print('=' * 90)

nota1 = float(input('ENTRE COM A NOTA 1: '))
nota2 = float(input('ENTRE COM A NOTA 2: '))
nota3 = float(input('ENTRE COM A NOTA 3: '))
nota4 = float(input('ENTRE COM A NOTA 4: '))

soma = nota1 + nota2 + nota3 + nota4
media = (nota1 + nota2 + nota3 + nota4) / 4

print()
print('-' * 90)
print('VALOR SOLICITADO')
print('=' * 90)

print(f'A soma das notas é {soma}')
print(f'A média das notas é {media}')
print()