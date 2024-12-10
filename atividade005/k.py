# Crie um programa que pede que o usuário digite um nome ou uma frase,
#verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.


frase = str(input('Entre com a frase: ')).lower().replace(' ', '')
palindromo = frase[::-1]    

while (True):

        if (frase == palindromo):
          print(f'A frase {frase} é um palíndromo.')
          break

        else:
                print('.' * 90)
                print(f'A frase {frase} não é um palíndromo.')  
                break
        