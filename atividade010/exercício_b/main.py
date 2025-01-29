import os

from cadastro.cadastrando import cadastrar_aluno
from cadastro.exibindo.exibir import exibir_aluno

os.system('cls')

resultado = cadastrar_aluno()
exibir_aluno(resultado)

