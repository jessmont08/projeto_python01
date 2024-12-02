#atividade de sets feita em 02/12/2024, feita por jéssica da rocha monteiro
# da turma 392 do curso técnico de desenvolvimento de sistemas do senac.

# o sistema diz sobre um estoque de uma loja de rede que tem cinco fornecedores e um controle detalhado por
# problemas anteriores, o sistema tem como objetivo documentar o estoque.

print("=" * 90)
print("Velours d'Or")
print('-' * 90)
print("Controle Mensal.")
print('=' * 90)

mirage_couture = {"fleur_dress", "luna_shirt", "sarah_bag"}
ardor_noble = {"melias_necklace", "swan_diamond", "boos_earrings"}
maison_verite = {"looked_blush", "blinked_gloss", "maxima_lipstick"}
sapphire_rouge = {"j'adore_perfum", "goodgirl_perfum", "gardenia_perfum"}
opera_prime = {"loubotin", "alexander_mcqueen", "dolce&gabanna"}

estoque = mirage_couture.union(ardor_noble, maison_verite, sapphire_rouge, opera_prime)

print('=' * 90)
print(estoque)
print('-' * 90)


if "melias_necklace" in estoque:
    estoque.remove("melias_necklace")
    print("melias_necklace foi vendido.")
print('-' * 90)

print("Os pacotes da Opera Prime com novos sapatos chegou, adicione-os ao estoque.")

while True: 
    pacotes01 = str(input("Entre com os sapatos novos, clique 's' ao acabar: ")).lower().strip()
     
    if pacotes01 != 's':
        print("Adicionado.")
    else:
        print("Saída solicitada.")
        break

    estoque.add(pacotes01)
print(estoque)

if "luna_shirt" and "nike" in estoque:
    estoque.discard("nike") 
    estoque.discard("luna_shirt")
    print("Os sapatos da Nike e a blusa da Luna não estão no estoque.")

print('Queima de estoque! Houve um sold out da nossa marca.')
estoque.clear()
print(f'Nosso estoque atual é: {estoque}')

print('=' * 90)