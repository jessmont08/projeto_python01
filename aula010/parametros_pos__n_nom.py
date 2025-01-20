import os


os.system('cls')

def dados_paciente(nome= 'coly', nascimento= '2000', peso= '46', 
                   altura= '1.69'):
    
    print(f'Bem-vindo ao sistema Senac, {nome}')
    print(f'O nascimento da {nome} é {nascimento}.')
    print(f'O peso da {nome} é {peso}KG.')
    print(f'A altura da {nome} é {altura}')
    print('=' * 90)

def posicional_nomeado(nascimento, nome= 'coly'):
    print(f'Bem vindo ao sistema Senac, {nome}')
    print(f'O nascimento da {nome} é {nascimento}.')
    print('=' * 90)

def nomeado_posicional(nome= 'coly', nascimento): # nao funciona!!
    print(f'Bem vindo ao sistema Senac, {nome}')
    print(f'O nascimento da {nome} é {nascimento}.')
    print('=' * 90)

dados_paciente


dados_paciente(nome= 'isis', nascimento= '1985', peso= '46', altura= '1..69')
dados_paciente(nascimento= '2008', nome= 'ágata', peso= '46', altura= '1.58')
dados_paciente(altura= '1.66', nome= 'bia', peso= '46', nascimento= '2008')
