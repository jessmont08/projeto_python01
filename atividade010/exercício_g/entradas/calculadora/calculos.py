def operando_valores(x, y, escolha):
    if escolha == 1: 
        soma = x + y
        return soma
    elif escolha == 2:
        subtracao = x - y
        return subtracao
    elif escolha == 3:
        multiplicacao = x * y
        return multiplicacao
    elif escolha == 4:
        if y == 0:
            print('Erro por divisão com zero.')
            return None
        divisao = x / y
        return divisao
    elif escolha == 5:
        if y == 0:
            print('Erro por divisão com zero.')
            return None
        inteira = x // y
        return inteira
    elif escolha == 6:
        if y == 0:
            print('Erro por divisão com zero.')
            return None
        resto = x % y
        return resto