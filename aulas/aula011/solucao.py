try: 
    resultado = 10/0
    arquivo = open('arquivo_inexistente.txt', 'r')
except ZeroDivisionError: 
    print('ERRO! Divisão por zero.')
except FileNotFoundError:
    print('Erro! Arquivo não-encontrado.')
except Exception as e:
    print(f'Erro não esperado: {e}')

print('Continua a execucão do programa.')