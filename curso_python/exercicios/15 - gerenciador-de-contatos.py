contatos = {}
lista = []
    
print(f'Gerenciador de contatos')
print('-' * 90)
print('Menu inicial:\n')
print('1- Adicionar;\n2- Listar;\n3- Buscar;\n4- Remover;\n5- Sair;')
print('-' * 90)

try:
    acao = None
    while acao != 5:
        acao = int(input('Digite a opção desejada: '))
        print('-' * 90)
        match acao:
            case 1:
                nome = input('Digite o nome: ')
                tel = int(input('Digite o número: '))
                print('-' * 90)
                    
                if nome != '' and tel != '':
                    contatos[f'Nome: {nome}'] = f'Telefone: {tel}'
                    lista.append(contatos)
                    print('Adicionado com sucesso!')
                    print('-' * 90)
                    print(lista)
                    print('-' * 90)
                        
                else:
                    print('Digite algum valor')
                    print('-' * 90)
                    
            case 2:
                print('Lista de contatos atual:\n')

                
            case 3:                
                print('Escolha uma opção:\n')
                print('1- Excluir contato específico;\n2- Excluir todos;')
                print('-' * 90)        
                del_opcao = int(input('Digite aqui a opção desejada: '))
                print('-' * 90) 
                
                if del_opcao == 1:
                    
                    del_nome = input('Digite o nome para excluir: ')

                    if del_nome in contatos:
                        contatos.pop(del_nome)
                        print('\nExcluído com sucesso!')
                    else:
                        print('\nNome não encontrado.')
                else:
                    contatos.clear()
                    print('\nTodos os contatos apagados com sucesso!')

            case 4:
                print('Agenda fechada. Até logo!')
                exit()
    
    print('-' * 90)            
    print('Agenda fechada. Até logo!')
    print('-' * 90)
    exit()
    
except ValueError:
    exit()





