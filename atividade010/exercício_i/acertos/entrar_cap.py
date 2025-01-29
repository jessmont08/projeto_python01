
        
def acertar_capitais(capitais):
    acertos = 0
    for keys, values in capitais.items():
        respostas = input(f'Digite a capital do estado {keys}: ').lower()
        print('-' * 90)
        if values != respostas:
            print(f'Errado! A resposta é {values}. Tente de novo!')
            break
        else:
            print('Correto! Continue.')
            acertos += 1

    return respostas, acertos
