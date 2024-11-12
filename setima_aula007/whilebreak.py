import os
os.system('cls')




while (True):
    nome = str(input('Digite o nome ou x para sair: ')).lower()

    if (nome != 'x'):
        print('Continue a digitar.')
    else: 
        print('=' * 90)
        print('Você solicitou a saída.')
        break

print('.' * 90)
print()
