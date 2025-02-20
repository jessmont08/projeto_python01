import os
from datetime import datetime

os.system('cls')

eventos = {}

for i in range(1, 3):
    nomes = input('Digite o nome do evento: ')
    data = input('Digite a data que irá ocorrer: ')
    local = input('Digite a localização: ')
    participantes = []

    data = datetime.strptime(data, '%d/%m/%Y')
    eventos[nomes] = {'data': data, 'local': local, 'participantes': participantes}

while True:
    adicionar = input('Deseja adicionar participantes?'
                      '\n Digite s ou n: ')

    if adicionar == 's': 
        evento_participante = input('Digite o nome do evento'
                                    '\nque deseja adicionar participantes: ')
        
        if evento_participante in eventos: 
            participante = input('Digite o nome do participante: ')
            email = input('Entre com o email dele: ')
            eventos[evento_participante]['participantes'].append({
                "email": email, "membro": participante})
        
    elif adicionar == 'n':
        print('Saindo do adicionar membros')
        break

    else:
        print('Digite s ou n.')

for chaves, valores in eventos.items():
    print(f'O nome do evento é {chaves}.')
    print(f'A data do evento é {valores["data"].strftime("%d/%m/%Y")}')
    print(f'A local do evento é {valores["local"]}')
    print(f'Os participantes do evento são:')
    for participante in valores['participantes']:
        print(f'* Nome: {participante["membro"]}, * Email: {participante["email"]}')
        
data_str2 = '01/01/2025'
data_2 = datetime.strptime(data_str2, '%d/%m/%Y')

contagem = 0

for values in eventos.values():
    if values['data'] >= data_2:
        contagem += 1

print(f'Há {contagem} eventos marcados depois de 01/01/2025.')