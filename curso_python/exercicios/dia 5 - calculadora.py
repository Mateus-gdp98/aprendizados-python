print('Calculadora 🔢\n')
print('1 -> Adição + \n2 -> Subtração - \n3 -> Multiplicação X \n4 -> Divisão ÷')
print('-' * 60)

try:
    operacao = int(input('Digite a operação desejada: '))
    print('-' * 60)
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    print('-' * 60)
    
except ValueError:
    print('Atenção!!! Digite uma opção válida.')
    exit()
      
if operacao in (1,2,3,4):    
    match operacao:
        
        case 1:
            res = float(num1 + num2)
            print(f'A soma de {num1} e {num2} é {res}')
            print('-' * 60)
        case 2:
            res = float(num1 - num2)
            print(f'A subtração de {num1} e {num2} é {res}')
            print('-' * 60)
        case 3:
            res = float(round(num1 * num2, 2))
            print(f'A multiplicação de {num1} e {num2} é {res}')
            print('-' * 60)
        case 4:
            if num2 == 0:
                print('Atenção!!! Impossível realizar divisão com divisor 0.')
                print('-' * 60)
                exit()
            else:
                res = float(round(num1 / num2, 2))
                print(f'A divisão de {num1} e {num2} é {res}')
                print('-' * 60)

else:
    print('Atenção!!! Digite um valor correto, para selecionar a operação.')
    print('-' * 60)
    exit()
