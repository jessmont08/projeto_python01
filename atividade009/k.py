import  os
from datetime import datetime
os.system('cls')

tarefas = dict()

for i in range(1, 2):
    nome = input('Digite o nome da tarefa: ').strip().lower()
    vencimento = input('Digite o vencimento da tarefa'
                           '\nno formato dd/mm/aaaa: ' )                     
    prioridade = input('Digite a prioridade da tarefa: ').strip().lower()

    tarefas[nome] = {'data de vencimento': vencimento,
                     'prioridade': prioridade}
    
while True:
    alterar = input('Deseja alterar algo? Digite s ou n:').strip().lower()

    if alterar == 's':
        alterando = input('Digite o nome da tarefa'
                          '\nque deseja alterar:').strip().lower()
        
        if alterando in tarefas:
            subitem = input('Digite o que quer alterar'
                            '\n(vencimento ou prioridade): ').strip().lower()
            alteracao = input('Digite a alteração: ')
            tarefas[alterando][subitem] = alteracao

        else:
            print('Essa tarefa não existe.')

    elif alterar == 'n':
        print('Sem alterações.')
        break

    else:
        print('Digite s ou n.')


hora = datetime.now()
data = hora.strftime('%d/%m/%Y')
print(data)

prioridade_alta = 0
for values in tarefas.values():
    if values['prioridade'] == 'alta':
        prioridade_alta += 1
print(f'Há atualmente {prioridade_alta} tarefas com a prioridade alta.')

if data.month == 12:
    proximo_mes = 1
    proximo_ano = data.year + 1

else:
    proximo_mes = data.month + 1
    proximo_ano = data.year 

vencimento_proximo = 0
for values in tarefas.values():
    data_venc_str = values['data de vencimento']
    data_venc = datetime.strptime(data_venc_str,'%d/%m/%Y')
    if data_venc.year == proximo_ano and data_venc.month == proximo_mes:
        vencimento_proximo += 1
print(f'Há atualmente {vencimento_proximo} tarefas com'
      '\no vencimento no proxímo mês.')