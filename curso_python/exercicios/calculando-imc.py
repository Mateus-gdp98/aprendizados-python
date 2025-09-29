peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = round(peso / (altura*altura), 2)

imc_min_saudavel = 18.5
imc_max_saudavel = 25

peso_min = round(imc_min_saudavel * (altura*altura), 0)
peso_max = round(imc_max_saudavel * (altura*altura), 0)

try:  
    if imc < 16:
        print(f'Imc de {imc} -> Magreza grave.')
        print(f'Seu peso mínimo ideal é {peso_min} e o máximo é {peso_max}. \n')
        print('Procure aumentar seu peso com massa boa.')
        
        
    elif imc >= 16 and imc < 17:        
        print(f'Imc de {imc} -> Magreza moderada.')
        print(f'Seu peso mínimo ideal é {peso_min} e o máximo é {peso_max}. \n')
        print('Procure aumentar seu peso com massa boa.')
        
    elif imc >= 17 and imc < 18.5:        
        print(f'Imc de {imc} -> Magreza leve.')
        print(f'Seu peso mínimo ideal é {peso_min} e o máximo é {peso_max}. \n')
        print('Procure aumentar seu peso com massa boa.')
        
    elif imc >= 18.5 and imc < 25:        
        print(f'Imc de {imc} -> Saudável.')
        print(f'Seu peso mínimo ideal é {peso_min} e o máximo é {peso_max}. \n')
        print(f'Parabéns.')
        
    elif imc >= 25 and imc < 30:        
        print(f'Imc de {imc} -> Sobrepeso.')
        print(f'Seu peso mínimo ideal é {peso_min} e o máximo é {peso_max}. \n')
        print('Procure diminuir o percentual de mass ruim e aumentar a massa boa.')
        
    elif imc >= 30 and imc < 35:        
        print(f'Imc de {imc} -> Obesidade grau I.')        
        print(f'Seu peso mínimo ideal é {peso_min} e o máximo é {peso_max}. \n')
        print('Procure diminuir o percentual de massa má e aumentar a massa boa.')

    elif imc >= 35 and imc < 40:        
        print(f'Imc de {imc} -> Obesidade grau II.') 
        print(f'Seu peso mínimo ideal é {peso_min} e o máximo é {peso_max}. \n')
        print('Procure diminuir o percentual de massa má e aumentar a massa boa.')

    elif imc >40:
        print(f'Imc de {imc} -> Obesidade grau III.') 
        print(f'Seu peso mínimo ideal é {peso_min} e o máximo é {peso_max}. \n')
        print('Procure diminuir o percentual de massa má e aumentar a massa boa.')

except:
    print('Digite os valores corretamente.')
    
    