"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

name = input('Type just your first name: ')

try:
    len(name) == None

    if len(name) < 2 and len(name) > 0:
        print('Your name is very short. Are you shure')

    elif len(name) <= 4:
        print('Your name is short.')
        
    elif len(name) >= 5 and len(name) <= 6:
        print('Your name is normal.')

    else:
        print('Your name its very big.')

except:
    print('Type anything')


