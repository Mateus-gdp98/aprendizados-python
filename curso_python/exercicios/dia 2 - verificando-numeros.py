# Verificar se um número é positivo, negativo ou zero:

try:
    numero = float(input('Digige um número inteiro: '))

except ValueError:
    print('Atenção!!! Digite um número válido.')
    exit()
    

if numero < 0:
    print(f'O número {numero} é negativo.')
    
elif numero > 0:
    print(f'O número {numero} é positivo.')

else:
    print(f'O número {numero} é zerado.')