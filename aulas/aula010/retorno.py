import os


os.system('cls')

# definindo uma func
def calcular_velocidade_media(distancia, tempo): 
    #vm = deltaV / deltaT
    velocidade_media = distancia / tempo
    return velocidade_media

distancia = float(input('Digite a distância percorrida (em km): '))
tempo = float(input('Digite o tempo gasto (em horas): '))

velocidade = calcular_velocidade_media(distancia, tempo)

print(f'A velocidade média é: {velocidade:.2f}km/h.')