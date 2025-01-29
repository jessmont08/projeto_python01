def calcular_media(academia):
    if not academia:
        return 0, 0

    contagem = len(academia)
    soma_peso = sum(cliente["peso"] for cliente in academia.values())
    soma_altura = sum(cliente["altura"] for cliente in academia.values())

    media_peso = soma_peso / contagem
    media_altura = soma_altura / contagem

    return media_peso, media_altura