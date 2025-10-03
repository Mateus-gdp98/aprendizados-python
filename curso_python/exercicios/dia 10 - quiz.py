print('Quem quer ser um milionário 🤑')
print('-' * 90)

resposta1 = 'd'
resposta2 = 'c'
resposta3 = 'a'

#pergunta 1
print('1. Qual é a capital da Austrália?')
print('A. Perth \nB. Sydney \nC. Melbourne \nD. Canberra')
print('-' * 90)

#pergunta 2
print('2. O Monte Everest, a montanha mais alta do mundo, está localizado em qual cadeia de montanhas?')
print('A. Andes \nB. Alpes \nC. Himalaia \nD. Montanhas Rochosas')
print('-' * 90)

#pergunta 3
print('3. Qual é o único planeta do sistema solar que gira no sentido horário?')
print('A. Vênus \nB. Marte \nC. Júpiter \nD. Saturno')
print('-' * 90)

def questao1 (q):
    if q == resposta1:
        return f"Correto 🎉 \n{'-' *90}"
    else:
        return f"Incorreto 😔 \n{'-' *90}"

def questao2 (q):
    if q == resposta2:
        return f"Correto 🎉 \n{'-' *90}"
    else:
        return f"Incorreto 😔 \n{'-' *90}"

def questao3 (q):
    if q == resposta3:
        return f"Correto 🎉 \n{'-' *90}"
    else:
        return f"Incorreto 😔 \n{'-' *90}"
        

try:
    pergunta1 = input('1- Digite a alternativa correta: ').lower()
    print('-' * 90)
    print(questao1(pergunta1))
    
    pergunta2 = input('2- Digite a alternativa correta: ').lower()
    print('-' * 90)
    print(questao2(pergunta2))

    pergunta3 = input('3- Digite a alternativa correta: ').lower()
    print('-' * 90)
    print(questao3(pergunta3))
    
        
    if "Correto" in str(questao1(pergunta1)):
        cont1 = 1
    else:
        cont1 = 0
        
    if "Correto" in str(questao2(pergunta2)):
        cont2 = 1
    else:
        cont2 = 0
        
    if "Correto" in str(questao3(pergunta3)):
        cont3 = 1
    else:
        cont3 = 0

    print(f'Você teve um total de {cont1 + cont2 + cont3} acertos.')

    
except ValueError:
    print('Valor inválido.')
    print('-' * 90)
    exit()