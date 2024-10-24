import os

os.system('cls')

print('-' * 30)
print('MÉDIA DE NOTAS')

nota_1 = float(input('Adicione a nota 01 do aluno: '))
nota_2 = float(input('Adicione a nota 02 do aluno: '))
nota_3 = float(input('Adicione a nota 03 do aluno: '))
nota_4 = float(input('Adicione a nota 04 do aluno: '))

soma = nota_1 + nota_2 + nota_3 + nota_4
media = nota_1 + nota_2 + nota_3 + nota_4 / 4
media_correta = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print('-' * 30)
print('SOMATÓRIO')
print('-' * 30)

print(f'NOTA 1: {nota_1} / NOTA 2: {nota_2} '
      f'NOTA 3: {nota_3}'/ nota_4: {nota_4}')