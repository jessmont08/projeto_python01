# Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir a média de altura  e peso de seus clientes.
# Faça um programa que pergunte a cada um dos clientes da academia seu código, nome, altura e peso. Após esse cadastramento, 
# seu programa deverá listar os dados dos clientes e a média. Para sair do programa o usuário deverá digitar o valor zero(0). 
# O número de clientes é indefinido. 

import os

from cadastro.cadastrando import cadastrar_clientes
from cadastro.exibir_media.listar import listar_clientes
from cadastro.exibir_media.media import calcular_media

academia = cadastrar_clientes()
media_peso, media_altura = calcular_media(academia)
listar_clientes(academia)

print('=' * 90)
print(f'A média dos clientes de altura é'
      f'\né {media_altura}m.')
print(f'A média dos clientes de peso é'
      f'\né {media_peso}kg.')
print('=' * 90)