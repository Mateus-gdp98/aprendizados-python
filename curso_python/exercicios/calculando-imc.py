imc_min_saudavel = 18.5
imc_max_saudavel = 25

try:
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = round(peso / (altura*altura), 2)
    peso_min = round(imc_min_saudavel * (altura*altura), 0)
    peso_max = round(imc_max_saudavel * (altura*altura), 0)
    
except ValueError:
    print('Digite os valores corretamente.')
    exit()
        
if imc < 16:
    print(f'Imc de {imc} -> Magreza grave. \n')
    print('Procure aumentar seu peso com massa magra. \n')    
        
elif imc >= 16 and imc < 17:        
    print(f'Imc de {imc} -> Magreza moderada. \n')
    print('Procure aumentar seu peso com massa magra. \n')
        
elif imc >= 17 and imc < 18.5:        
    print(f'Imc de {imc} -> Magreza leve. \n')
    print('Procure aumentar seu peso com massa magra. \n')
        
elif imc >= 18.5 and imc < 25:        
    print(f'Imc de {imc} -> Saudável. \n')
    print(f'Parabéns. \n')
        
elif imc >= 25 and imc < 30:        
        print(f'Imc de {imc} -> Sobrepeso. \n')
        print('Procure diminuir o percentual de massa gorda e aumentar a massa magra.\n')
        
elif imc >= 30 and imc < 35:        
        print(f'Imc de {imc} -> Obesidade grau I.\n')        
        print('Procure diminuir o percentual de massa gorda e aumentar a massa magra.\n')

elif imc >= 35 and imc < 40:        
        print(f'Imc de {imc} -> Obesidade grau II.\n') 
        print('Procure diminuir o percentual de massa gorda e aumentar a massa magra.\n')

elif imc >= 40:
    print(f'Imc de {imc} -> Obesidade grau III. \n') 
    print('Procure diminuir o percentual de massa gorda e aumentar a massa magra. \n')

    
print(f'Seu peso mínimo ideal é {peso_min} e o máximo é {peso_max}.')