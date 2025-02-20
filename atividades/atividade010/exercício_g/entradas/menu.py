def escolher_menu():
    
    print('Menu de operações.')
    print('1. Soma.')
    print('2. Subtração.')
    print('3. Multiplicação.')
    print('4. Divisão.')
    print('5. Divisão inteira.')
    print('6. Resto da divisão.')

    escolha = int(input('Escolha do 1 ao 6: '))
    if escolha < 1 or escolha > 6:
        print('Valor ínvalido.')
        return None

    return escolha
