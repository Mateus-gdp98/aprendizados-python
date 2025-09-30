'''
O programa escolhe um número secreto, aleatório.
O jogador precisa tentar adivinhar esse número digitando palpites.
A cada tentativa, o programa dá uma dica:
Se o palpite for menor que o número secreto → mostra "Tente um número maior".
Se o palpite for maior → mostra "Tente um número menor".
O jogo continua em um loop até o jogador acertar.
Quando acerta, o programa mostra uma mensagem de vitória e pode informar também quantas tentativas foram necessárias.
'''
import random

numero = random.randint(1,10)
contador = 5

while contador >= 1:
    print('JOGO DE ADIVINHA 🕹️')
    print(f'Atenção!!! Você tem {contador} chances restantes.')
    numero_digitado = int(input('Tente acertar o número que estou pensando entre 1 e 10: '))
    print('-' * 60)
        
    if numero_digitado > 10 or numero_digitado < 1:
        print('Errado 😞')
        print('Digite um número entre 1 e 10.')
        print('-' * 60)
        contador -= 1
        continue
      
    elif numero_digitado != numero:
        print('Errado 😞')
        
        if numero_digitado < numero:
            print('Tente um número maior!')
            print('-' * 60)
        
        elif numero_digitado > numero:
            print('Tente um número menor')
            print('-' * 60)
        
        contador -= 1
        continue
        
    else:
        print(f'Vitória: 🎉 Eu pensei no número {numero} e você ganhou em {6 - contador} tentativas!')      
        print('-' * 60)
        break

if contador == 0:
    print(f'Derrota: 😞 Acabaram as chances, o número era {numero}.')
    print('-' * 60)
