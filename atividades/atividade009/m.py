import os
from datetime import datetime

os.system('cls')

registro = {}

for i in range(1, 3):
    destino = input('Digite o destino da viagem: ').lower().strip()
    duracao = input('Digite a duração prevista: ').lower().strip()
    data = input('Digite a data de partida: ')
    vagas = int(input('Digite o número de vagas disponíveis: '))

    data = datetime.strptime(data, '%d/%m/%Y')

    registro[destino] = {'Duração' : duracao, 'Data' : data,
                         'Vagas' : vagas}
    
while True: 
    print("-" * 30)
    alterar = input('Quer alterar algo? Digite s ou n: ').lower().strip()
    if alterar == 's': 
        alterando = input('Digite o destino que deseja alterar: ').lower().strip()
        if alterando in registro: 
            alteracao_em = input('Digite o que deseja alterar: ').capitalize()
            alteracao = input('Digite a alteração: ')
            if alteracao_em == 'Data':
                alteracao = datetime.strptime(alteracao, '%d/%m/%Y')
            registro[alterando][alteracao_em] = alteracao


    elif alterar =='n':
        print("-" * 30)
        print('Saindo...')
        break

    else:
        print('Digite s ou n.')


data_limitestr = '01/06/2025'
data_limite = datetime.strptime(data_limitestr, '%d/%m/%Y')
datas_longe = 0 
vagas_escassas = 0
for values in registro.values():
    if values['Vagas'] <= 10:
        vagas_escassas += 1
    if values['Data'] >= data_limite:
        datas_longe += 1

registro_ordenado = dict(sorted(registro.items(), key= lambda item:item[0]))

for keys, values in registro_ordenado.items():
    print("-" * 30)
    print(f'O destino é {keys.capitalize()}.')
    print(f'A data da viagem é {values["Data"].strftime("%d/%m/%Y")}.')
    print(f'A duração da viagem é {values["Duração"]}.')
    print(f'O número de vagas é {values["Vagas"]}')
    print("-" * 30)

print(f'Há {vagas_escassas} viagens com menos de dez vagas.')
print(f'Há {datas_longe} viagens marcadas para depois de 01/06/2025.')
print("-" * 30)