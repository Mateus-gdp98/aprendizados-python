print(f'Agenda de contatos:\n')
contatos = {'nome':'mateus', 'tel': 123}

print(f'Atualmente você possui os contatos abaixo:\n')

for chave in contatos:
    print(f'{chave}: {contatos[chave]}')
print('-' * 90)

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
                try:
                    nome = input('Digite o nome: ')
                    tel = int(input('Digite o número: '))
                    print('-' * 90)
                    
                    if nome != '' and tel != '':
                        contatos[nome] = tel
                        print('\nAdicionado com sucesso!')
                        print('-' * 90)
                        
                    else:
                        print('Digite algum valor')
                        print('-' * 90)
                
                except ValueError:
                    print('Digite algum valor')
                    print('-' * 90)
                    
            case 2:
                print('Lista de contatos atual:\n')
                for chave in contatos:
                    print(f'{chave}: {contatos[chave]}')
                print('-' * 90)
                
            case 3:
                ...

            case 4:
                print('Agenda fechada. Até logo!.')
                exit()
    
except:
    exit()





