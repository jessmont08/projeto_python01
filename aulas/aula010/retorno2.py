import os

os.system('cls')

# definindo funcao

def calcular_vm_media(espaco, tempo, espaco_unidade, tempo_unidade):
    
    # convrtendo para km 
    if espaco_unidade == 'metros':
        espaco / 1000 

    # converte minutos para horas
    if tempo_unidade == 'minutos':
        tempo / 60

    vm = espaco / tempo
    return vm

espaco = float(input('Digite a distância percorrida: '))
espaco_unidade = input('A velocidade é em km ou metros? ').lower()
tempo = float(input('Digite o tempo gasto: '))
tempo_unidade = input('O tempo é em horas ou em minutos? ').lower()

vm = calcular_vm_media(espaco, tempo, espaco_unidade, tempo_unidade)

print(f'A velocidade média é {vm:.2f} {espaco_unidade}/{tempo_unidade}.')