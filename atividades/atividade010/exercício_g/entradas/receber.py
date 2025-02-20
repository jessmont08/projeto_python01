def receber_num():
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

    if x < 0 or x > 11:
        print('valor invalido.')
        return None
    elif  y < 0 or y > 11:
        print('valor invalido.')
        return None
    
    return x, y