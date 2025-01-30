try: 
    resultado = 10/0
    arquivo = open('arquivo_inexistente.txt', 'r')
except Exception:
    # captura as exceções, mas não faz nada com elas.
    pass

print('O programa continua. ')

# solução 
