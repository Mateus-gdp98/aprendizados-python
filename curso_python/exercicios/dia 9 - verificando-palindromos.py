#função que verifica se palavra é palíndromo


try:
    palavra = input('Qual palavra deseja verificar? ')

    def palindromos(a):
        a = palavra.lower()[::-1]
        if a == palavra:
            return print(f'A palavra {a} é uma palindromo.')
        else:
            print('Não é palindromo.')
            exit()
    
except ValueError:
    print('Digite um texto.')
    

print(palindromos(palavra.lower()))