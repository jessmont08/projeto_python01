# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra.
# Caso a letra seja o “f" finalize a aplicação. Do contrário, imprima novamente a
# mesma frase até que o caractere “f" seja digitado.


while (True):
    letra = str(input('Digite uma letra: ')).lower()

    
    if (letra != 'f'):
        print('Estou em looping.')
    
    else:
        print('Você solicitou a saída.')
        break

    