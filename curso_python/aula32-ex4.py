"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""

while True:
    hora_digitada = input("Digite a hora atual, no seguinte formato 'HH:MM': ")
    
    try:
        hora = int(hora_digitada[:2:])
        minuto = int(hora_digitada[-2::])
        
        if hora < 12 and minuto <= 59:
            print(f'Bom dia, a hora atual é {hora_digitada}')
            
        elif hora >= 12 and hora < 18 and minuto <= 59:
            print(f'Boa tarde, a hora atual é {hora_digitada}')
        
        elif hora == None or minuto == None:
            print('Hora inválida')
            
        elif hora > 23 or minuto > 60:
            print('Hora inválida')
        
        else:
            print(f'Boa noite, a hora atual é {hora_digitada}')
        
        break  # só sai do loop se não cair no except

    except:
        print(f'{hora_digitada} não é uma hora válida, tente novamente.')
