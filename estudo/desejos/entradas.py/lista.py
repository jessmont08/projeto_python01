class ListaDoCarrinho:
    def __init__(self):
        # inicia com uma lista
        self.lista = []


    def adicionar_item(self):
        self.lista = []
        
        # entrada dos dados
        while True:
            # o dicionario fica dentro para que toda vez q um novo item seja colocado
            # ele seja colocado denro do dcionario de novo
            desejos = {}
            nome = input('Nome do produto: ')
            marca = input('Marca do produto: ')
            preco = float(input('Digite o preço: '))
            quantidade = int(input('Digite a quantidade: '))    
            escolha = input('Deseja adicionar mais? (s/n): ')
             
            # colocando dentro do dicionario
            desejos['nome'] = nome
            desejos['marca'] = marca
            desejos['preco'] = preco
            desejos['quantidade'] = quantidade

            # cria uma copia rasa do dict e coloca ele na lista
            self.lista.append(desejos.copy())

            if escolha != 's':
                break

        return self.lista

# cria objeto
carrinho = ListaDoCarrinho()
# busca a funcao denro do objeo da classe
ava = carrinho.adicionar_item()
 
print(ava)