print(f'Agenda de contatos:\n')

def mostrar_contatos(contatos):
    for chave in contatos:
        print(f'Nome: {chave} | Telefone: {contatos[chave]}')
    print('-' * 90)
    
contatos = {
    'mateus': 123,
    'thays': 456,
    'laisa': 789
}
print(f'Atualmente você possui os contatos abaixo:\n')
mostrar_contatos(contatos)

try:
    acao = input('Deseja alterar algo? (S/N) -> ').upper()
    print('-' * 90)
    
    while acao != 'N':
        print('Escolha uma opção:\n')
        print('1- Adicionar;\n2- Ver;\n3- Apagar;\n4- Sair.')
        print('-' * 90)        
        opcao = int(input('Digite aqui a opção desejada: '))
        print('-' * 90)
        
        match opcao:
            case 1:
                nome = input('Digite o nome: ')
                tel = int(input('Digite o número: '))
                print('-' * 90)
                    
                if nome != '' and tel != '':
                    contatos[nome] = tel
                    print('Adicionado com sucesso!')
                    print('-' * 90)
                        
                else:
                    print('Digite algum valor')
                    print('-' * 90)
                    
            case 2:
                print('Lista de contatos atual:\n')
                mostrar_contatos(contatos)
                
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
                
    print('Agenda fechada. Até logo!')
    print('-' * 90)
    exit()
    
except ValueError:
    exit()





