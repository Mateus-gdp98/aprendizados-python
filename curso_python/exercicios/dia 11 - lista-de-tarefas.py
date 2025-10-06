print('Criando uma lista de tarefas:')
print('-' * 90)
print('Digite as tarefas desejadas:\n')

try:
    lista = [input('1ª tarefa: '), input('2ª tarefa: '), input('3ª tarefa: '), input('4ª tarefa: '), input('5ª tarefa: ')]
    print('-' * 90)
except:
    print('Digite um texto válido.')
    
print('Resumo da lista:')
    
item = 0

for tarefa in lista:
    item += 1
    print(f'{item}ª - {tarefa}')
    
print('-' * 90)
print('Editando a lista:\n')
print('Digite 1 para adicionar itens a lista;')
print('Digite 2 para remover itens a lista;')
print('Digite 3 para sair;\n')


opcao = int(input('Opção escolhida: '))
print('-' * 90)

try:
    item = 0
    match opcao:
        
        case 1:
            adicao = input('Digite o item para incluir: ')
            print('-' * 90)
            print('Lista atualizada\n')
            lista.append(adicao)
                       
            for tarefa in lista:
                item += 1
                print(f'{item}ª - {tarefa}')
            
        case 2:
            remover = input('Digite o item para excluir: ')
            print('-' * 90)
            print('Lista atualizada\n')
            lista.remove(remover)
            
            for tarefa in lista:
                item += 1
                print(f'{item}ª - {tarefa}')
        
        case 3:
            print('Lista fechada.\n')
               
except ValueError:
    print('Digite uma opção válida.')
