lista_num = []
lista_quadrado = []

contador = 0

'''
Usando o While
while contador <= 20:
    if contador % 2 == 0:
        quadrado = contador * contador
        lista_num.append(contador)
        lista_quadrado.append(quadrado)                
    contador += 1
'''
#Usando o for
for contador in range(0, 21, 2):
    lista_num.append(contador)
    lista_quadrado.append(contador ** 2)
    
print(f'Os números pares são {lista_num}')
print('-' * 90)
print(f'E o quadrado deles {lista_quadrado}')
print('-' * 90)

