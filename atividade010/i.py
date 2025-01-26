# Faça um programa de perguntas e respostas sobre os estados e capitais brasileiras. O programa deverá exibir para o usuário o estado e perguntar qual a sua capital.
# Se o usuário errar a resposta, o programa será finalizado apresentando quantas perguntas estão corretas. 

import os

os.system('cls')

capitais = {'acre': 'rio branco',
    'alagoas': 'maceió',
    'amazonas': 'manaus',
    'bahia': 'salvador',
    'ceará': 'fortaleza',
    'distrito federal': 'brasilia',
    'espírito santo': 'vitória',
    'goiás': 'goiânia',
    'maranhão': 'são luis',
    'mato grosso': 'cuiabá',
    'mato grosso do sul': 'campo_grande',
    'minas gerais': 'belo horizonte',
    'pará': 'belém',
    'paraíba': 'joão pessoa',
    'paraná': 'curitiba',
    'pernambuco': 'recife',
    'piauí': 'teresina',
    'rio de janeiro': 'rio de janeiro',
    'rio grande do norte': 'natal',
    'rio grande do sul': 'porto alegre',
    'rondônia': 'porto velho',
    'roraima': 'boa vista',
    'santa catarina': 'florianópolis',
    'são paulo': 'são paulo',
    'sergipe': 'aracaju',
    'tocantins': 'palmas'}
        
def acertar_capitais(capitais):
    acertos = 0
    for keys, values in capitais.items():
        respostas = input(f'Digite a capital do estado {keys}: ').lower()
        print('-' * 90)
        if values != respostas:
            print(f'Errado! A resposta é {values}. Tente de novo!')
            break
        else:
            print('Correto! Continue.')
            acertos += 1

    return respostas, acertos

respostas, acertos = acertar_capitais(capitais)
print(f'A quantidade de acertos foi: {acertos}')
print('=' * 90)
print()