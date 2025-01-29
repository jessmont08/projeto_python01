def listar_clientes(academia):
    for keys, values in academia.items():
        print('=' * 90)
        print(f'O nome do cliente é {keys}')
        print(f'O peso é {values["peso"]}kg.')
        print(f'A altura é {values["altura"]}m.')
        print('=' * 90)