try: 
    resultado = 10/0
except ZeroDivisionError:
    print('Erro por divisão por zero.')
else:
    print('Tudo ok! Divisão realizada com sucesso.')
finally: 
    print('Esse bloco é sempre executado.')