lista = []
contatos = {}
    
print(f'Gerenciador de contatos')
print('-' * 90)
print('Menu inicial\n')

try:
    acao = None
    while acao != 5:
        print('1- Adicionar;\n2- Listar;\n3- Buscar;\n4- Remover;\n5- Sair;\n')
        acao = int(input('Digite a opção desejada: '))
        print('-' * 90)
        
        if acao == 1:
            nome = input('Digite o nome: ')
            tel = int(input('Digite o número: '))
            print('-' * 90)

            if nome != '' and tel != '':
                novo = {'nome': nome, 'telefone': tel}
                lista.append(novo)
                print('Adicionado com sucesso!')
                print('-' * 90)
            else:
                print('Digite algum valor')
                print('-' * 90)

            
        elif acao == 2:
            print('Lista de contatos atual:\n')
            print(lista)
            print('-' * 90)
                
        elif acao == 3:
            busca = input('Digite o nome do contato para busca: ')
            encontrado = False
            print('-' * 90)

            for contato in lista:
                if busca.lower() in contato['nome'].lower():
                    print(f"Nome: {contato['nome']} | Telefone: {contato['telefone']}")
                    encontrado = True
                    print('-' * 90)

            if not encontrado:
                print('Contato não encontrado.')
                print('-' * 90)

  
        elif acao == 4:               
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
                    print('-' * 90)
                else:
                    print('\nNome não encontrado.')
                    print('-' * 90)
            else:
                contatos.clear()
                print('\nTodos os contatos apagados com sucesso!')
                print('-' * 90)

        elif acao == 5:
                print('Agenda fechada. Até logo!')
                exit()
        
        else:
            print('Digite alguma opção válida.')
    
    print('-' * 90)            
    print('Agenda fechada. Até logo!')
    print('-' * 90)
    exit()
    
except ValueError:
    exit()





