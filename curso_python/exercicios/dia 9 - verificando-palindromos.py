#função que verifica se palavra é palíndromo

print('Tente escrever uma palavra palíndromo 🕹️')
print('-' * 60)

palavra = input("Qual palavra deseja verificar? ").lower()
print('-' * 60)

if not palavra.isalpha():
    print("Atenção!!! Digite apenas letras, nada de números. ❌")
    print('-' * 60)
    exit()

def palindromos(p):
    if p == p[::-1]:
        return f'Vitória 🎉: A palavra "{p}" é palíndromo.'
    
    else:
        return f'Derrota 😔: A palavra "{p}" não é palíndromo.'

print(palindromos(palavra))
print('-' * 60)