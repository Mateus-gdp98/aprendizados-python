#imprimir números de 1 a 50, pares e ímpares.

numero = 0
while numero < 50:
    numero += 1
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
        