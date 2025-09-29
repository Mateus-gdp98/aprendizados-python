nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
num_caracteres = int(len(nome))

if nome and idade != False:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')
    
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome NÃO contém espaços.')
        
    print(f'Seu nome contém {num_caracteres} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}.')
    print(f'A última letra do seu nome é {nome[num_caracteres-1]}.')
        
else:
    print('Desculpe, você deixou campos vazios.')
