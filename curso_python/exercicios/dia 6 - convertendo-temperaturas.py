print('Conversor de temperatura 🌡️')
print('-' * 60)
print('F -> Fahrenheit/Celsius ou C -> Celsius/Fahrenheit')
print('-' * 60)

def conversor_1 (a):
    res = float(round((a * 1.8) + 32,2))
    return res

def conversor_2 (a):
    res = round(float((a - 32) / 1.8),2)
    return res


try:
    unidade_de_medida = input('Escolha a unidade de medida: ')
    print('-' * 60)
    temperatura = float(input('Qual a temperatura? '))

    match unidade_de_medida.upper():
        case 'C':
            print(f'A temperatura de {temperatura}° Celsius equivale a {conversor_1(temperatura)}° Fahrenheit.')
            print('-' * 60)
        
        case 'F':
            print(f'A temperatura de {temperatura}° Fahrenheit equivale a {conversor_2(temperatura)}° Celsius.')
            print('-' * 60)
        
        case _:
            print('Opção inválida, tente novamente.')
            print('-' * 60)
            exit()

except ValueError:
    print('-' * 60)
    print('Atenção!!! Digite um valor válido.')
    print('-' * 60)
    exit()
